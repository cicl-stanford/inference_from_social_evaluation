import os
import numpy as np
import pandas as pd
import itertools
from scipy.stats import norm, entropy
from scipy.special import logsumexp

"""
compute reward outcomes and blame for all possible combination of situations and choices in those situations
parameters:
	n_trees			int		# trees that could block the way
	n_strengths		int		# strengths a fisher could have
	n_actions  		int		# actions fisher could take (trees or fish)
	n_people		int		# fishers
	blame_func		fn 		function to determine blame
return:
	ee 				pd df   all possible situations and choices in them, as well as blame judgments

TODO: 
	general cleaning
	make compatible with more functions than the one I've got now
	symmetries
"""
def situations_df(n_trees, n_strengths, n_actions, n_people, w=.6, rationality_beta=1.5, k=2, graded_piv=False):
	# enumerating all possible combinations of number of trees, strengths, and actions for n people
	# 648 for standard possibilities of 3 trees, 3 strengths, 2 actions, and 3 people
	dd = pd.DataFrame(
		np.asarray(list(itertools.product(range(1, n_trees+1),
		np.asarray(list(itertools.product(range(1, n_strengths+1), repeat=n_people))),
		np.asarray(list(itertools.product(range(n_actions-1, -1, -1), repeat=n_people)))))))
	ee = pd.concat((
		pd.DataFrame(dd[0]),
		pd.DataFrame(dd[1].to_list()),
		pd.DataFrame(dd[2].to_list())),
		axis=1)
	ee.columns = ['trees', 'strength_a', 'strength_b', 'strength_c', 'action_a', 'action_b', 'action_c']

	# getting reward for each state ----------------
	rewards_store = []
	for situation_ix in range(ee.shape[0]):
		situation = ee.iloc[situation_ix]
		rewards_store.append(rewards(
			strengths= situation[['strength_a','strength_b','strength_c']].values, 
			trees=     situation[['trees']].values, 
			choices=   situation[['action_a','action_b','action_c']].values))
	ee['reward'] = rewards_store

	# blame for each state ----------------
	blame_array = np.empty((ee.shape[0], n_people))
	blame_array[:] = np.NaN

	for situation_ix in range(ee.shape[0]):
		situation = ee.iloc[situation_ix]

		# all possible rewards for different actions given trees and strengths 'situation'
		if situation_ix % 8 == 0:
			R_table = ee.iloc[situation_ix:situation_ix+8][['action_a','action_b','action_c','reward']]

		# blame judgments for each agent
		for agent_ix in range(n_people):
			blame_array[situation_ix,agent_ix] = rationality_pivotality_opt(R_table=R_table, 
				k=k, 
				beta=rationality_beta, 
				choices=situation[['action_a','action_b','action_c']].values, 
				agent=agent_ix, 
				w=w,
				graded_piv=graded_piv)

	# combining blame with the situations df
	blame_array = pd.DataFrame(blame_array, columns=['blame_a','blame_b','blame_c'])
	situations_concat = pd.concat((ee, blame_array), axis=1)

	return situations_concat

"""
Takes blame judgments and outputs a posterior over situations
parameters:
	df 			df 			dataframe of situations and blame
	other		int			situation-specific parameters to condition on
	blame 		float		blame judgments
return:
	blame_df	df 			posterior over blame
"""
def situation_inf(df, 
	trees      = None, 
	strength_a = None, 
	strength_b = None, 
	strength_c = None, 
	action_a   = None, 
	action_b   = None, 
	action_c   = None, 
	reward     = None, 
	blame_a    = None, 
	blame_b    = None, 
	blame_c    = None,
	scale      = .1,
	decision_beta = 1,
	prior = prior):
	
	# setting prior probability (where it's not possible for the group to get max reward)
	df = df.copy()
	df = pd.merge(df, prior, on=['trees','strength_a','strength_b','strength_c','action_a','action_b','action_c','reward'], how='left')
	df.rename(columns={'prior':'post'}, inplace=True)

	# removing conditioned-upon states
	variables = ['trees','strength_a','strength_b','strength_c','action_a','action_b','action_c']
	for variable in variables:
		if eval(variable) is not None:
			df = df[df[variable] == eval(variable)]

	# conditioning on reported blame
	blames = ['blame_a','blame_b','blame_c']
	for blame_idx in blames:
		if eval(blame_idx) is not None:
			tmp_lk = norm.pdf(eval(blame_idx), loc=df[blame_idx], scale=scale)
			df['post'] = df['post'] * tmp_lk
	df['post'] = df['post']/np.nansum(df['post'])

	# softmaxing by decision
	if decision_beta is not None:
		for variable in variables:
			if eval(variable) is None:
				tmp = df[[variable,'post']].groupby(variable).sum()
				tmp2 = np.exp(tmp*decision_beta)/np.sum(np.exp(tmp*decision_beta))
				tmp2 = tmp2.rename(columns = {'post':'post_' + variable})
				df = df.merge(tmp2, on=variable)	
		# finding all columns and multiplying to get softmaxed posterior
		post_names = df.filter(regex='^post_',axis=1)
		df['softmax'] = df.filter(post_names, axis=1).apply(np.prod, axis=1)
		df.drop(['post'], axis=1, inplace=True)
		df.drop(list(df.filter(regex = '^post_')), axis=1, inplace=True)
		df.rename(columns = {'softmax':'post'}, inplace=True)

	# correcting for underflow
	if any(np.isnan(df['post'])):
			df['post'] = 1e-10

	return df
	
"""
for a given situation with unknowns, outputs the kl divergence between models
parameters:
	dfs 				array of pd dfs 		different models with predictions about allocation of blame
	situation params 	ints/floats 			givens about the situation
return:
	out 				pd df 					description of sit. and mean kl-divergence among models
"""
def model_kld(dfs, 
	decision_beta = 1, 
	trees      = None, 
	strength_a = None, 
	strength_b = None, 
	strength_c = None, 
	action_a   = None, 
	action_b   = None, 
	action_c   = None, 
	reward     = None, 
	blame_a    = None, 
	blame_b    = None, 
	blame_c    = None):
	
	store_posts = []
	for blame_model in range(len(dfs)):
		tmp = situation_inf(df=dfs[blame_model], 
			decision_beta = decision_beta, 
			trees      = trees, 
			strength_a = strength_a, 
			strength_b = strength_b, 
			strength_c = strength_c, 
			action_a   = action_a, 
			action_b   = action_b, 
			action_c   = action_c, 
			reward     = reward, 
			blame_a    = blame_a, 
			blame_b    = blame_b, 
			blame_c    = blame_c)
		store_posts.append(tmp['post'])

	kl_divs = []
	for combo in list(itertools.combinations(range(len(store_posts)),2)): 
		kl_divs.append(entropy(store_posts[combo[0]].values)) #entropy of the posterior

	return np.mean(kl_divs)

# helper function to calculate kl-divergence
def kl_divergence(p, q):
	return sum(p[i] * np.log2(p[i]/q[i]) for i in range(len(p)))

"""
finding the divergence in model predictions by situation
parameters:
	dfs 				array of pd dfs 		models that assign blame by situation
return:
	situations_div 		pd df 					kl divergences between models for all situations w diff amounts of hiddenness
"""
def situations_looper(dfs, decision_beta=1):
	# need to create an empty dataframe of trees, strengths, actions, rewards, blames, and kl_divs
	situations_div = pd.DataFrame(columns=['trees','strength_a','strength_b','strength_c','action_a','action_b','action_c','reward','blame_a','blame_b','blame_c'])

	# looping over situations
	for situation_ix in range(dfs[0].shape[0]):
		# one situation at a time
		situation = dfs[0][situation_ix: situation_ix+1]

		# choosing things to drop or not
		# not looping over C for computational savings, symmetries might help
		hide_mat = pd.DataFrame(np.asarray(list(
			itertools.product(
				[situation['trees'].values[0], None], 
				[situation['strength_a'].values[0], None],
				[situation['strength_b'].values[0]],
				[situation['strength_c'].values[0]],
				[situation['action_a'].values[0], None],
				[situation['action_b'].values[0]],
				[situation['action_c'].values[0]],
				[situation['reward'].values[0]],
				[.2, .5, .8],
				[.2, .5, .8],
				[.2, .5, .8]))))
		hide_mat.columns = ['trees', 'strength_a', 'strength_b', 'strength_c', 'action_a', 'action_b', 'action_c', 'reward', 'blame_a', 'blame_b', 'blame_c']

		situations_div = situations_div.append(hide_mat)

	situations_div['mean_kld'] = situations_div.apply(lambda x: model_kld(
			dfs, 
			decision_beta=1, 
			trees=x['trees'], 
			strength_a=x['strength_a'], 
			strength_b=x['strength_b'],
			strength_c=x['strength_c'],
			action_a=x['action_a'],
			action_b=x['action_b'],
			action_c=x['action_c'],
			reward=x['reward'],
			blame_a=x['blame_a'],
			blame_b=x['blame_b'],
			blame_c=x['blame_c']), axis=1)  

	return(situations_div)