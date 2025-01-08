from action_blame import *
from random import shuffle
from draw_images import draw_image
from exp_cases import *
import pdb
COLOR = [(0, 100), (240, 100), (330, 100), (280, 100), (22, 100), (55, 100)]

w = 0.6		
k = 2
beta = 1.5

lam = 1
cases = [item for sublist in all_cases for subsublist in sublist for item in subsublist ]
for i, trial in enumerate(cases):
	print i

	shuffle(COLOR)
	COLOR
	color = [c for x, c in enumerate(COLOR) if x < 3]
	pdb.set_trace()
	R = rewards_multi(trial['strengths'], trial['trees'])
	
	probs = probability_k(R,k,beta)

	strengths =  trial['strengths']
	trees = trial['trees']
	choices = trial['choices']
	agents = len(strengths)
	if not os.path.exists('./figures/stimuli/'):
		os.makedirs('./figures/stimuli/')
	fig = draw_image(strengths, trees, color, file='./figures/stimuli/%d.png'%i, outcome=choices)

	fig = plt.figure(figsize=(12, 3))

	prob = []
	q = []
	r = []
	rs0 = []
	rs05 = []
	rs1 = []

	rm0 = []
	rm05 = []
	rm1 = []

	for agent in range(agents):
		pdb.set_trace()
		prob.append(rationality(R, k, beta, choices, agent))
		q.append(rationality_pivotality_opt(R, k, beta, choices, agent, w))
		r.append( rewards(strengths, trees, choices))
		rs0.append( kemp_model_reward_exp_conditioned(R, k, beta, strengths, trees, choices, agent, 0.))
		rs05.append( kemp_model_reward_exp_conditioned(R, k, beta, strengths, trees, choices, agent, 0.5))
		rs1.append(kemp_model_reward_exp_conditioned(R, k, beta, strengths, trees, choices, agent, 1.))
