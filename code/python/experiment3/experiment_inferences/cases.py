import pandas as pd
import numpy as np

n_trees= 3
n_fish = 0
strengths = np.array([1,1,3])
#actions = np.array(['trees','trees','trees'])
actions = ['trees','trees','trees']
blames = ['high','high','low']

gum = situation_generator(n_trees=n_trees, n_fish=n_fish, strengths=strengths, actions=actions, blames=blames)
gum.show()


pp3 = pp2[pp2.reward.notnull()].sort_values('mean_kld',ascending=False).copy() 


pd.DataFrame('n_trees':[0, None, 0, 1, 1, 3, 'fish', 'fish', 'fish', 'high', 'high', 'low'],
	         'strength_a':[1, None, 0, 1, 1, 3, 'fish', 'fish', 'fish', 'medium', 'medium', 'low'],
	         'strength_b':[1, None, 0, 1, 1, 3, 'fish', 'fish', 'fish', 'low', 'low', 'high'])

# cases used in experiment
cases = [
	{'id':0, 'n_trees':0, 'strengths':[1,1,3], 'actions':['fish','fish','fish'], 'blames':['high','high','low']},           # implies n_trees=1
	{'id':1, 'n_trees':0, 'strengths':[3,1,1], 'actions':['fish','fish','fish'], 'blames':['low','medium','medium']},       # implies n_trees=2
	{'id':2, 'n_trees':0, 'strengths':[1,3,1], 'actions':['fish','fish','fish'], 'blames':['low','high','low']},		    # implies n_trees=3
	{'id':3, 'n_trees':0, 'strengths':[1,1,3], 'actions':['trees','trees','trees'], 'blames':['medium','medium','high']},   # implies n_trees=1
	{'id':4, 'n_trees':0, 'strengths':[3,1,1], 'actions':['trees','trees','trees'], 'blames':['high','low','low']},		    # implies n_trees=2
	{'id':5, 'n_trees':0, 'strengths':[1,3,1], 'actions':['trees','trees','trees'], 'blames':['high','low','high']},        # implies n_trees=3
	{'id':6, 'n_trees':2, 'strengths':[0,2,3], 'actions':['trees','trees','fish'], 'blames':['high','low','low']},          # implies 1 or 3 strength_a
	{'id':7, 'n_trees':2, 'strengths':[3,0,2], 'actions':['fish','trees','trees'], 'blames':['low','medium','medium']},     # implies 2 strength_a
	{'id':8, 'n_trees':2, 'strengths':[3,3,0], 'actions':['trees','fish','trees'], 'blames':['medium','medium','high']},    # implies 1 strength_a
	{'id':9, 'n_trees':2, 'strengths':[3,0,3], 'actions':['trees','trees','fish'], 'blames':['high','low','low']},          # implies 2 strength_a
	{'id':10,'n_trees':2, 'strengths':[3,3,0], 'actions':['fish','trees','trees'], 'blames':['low','high','high']},         # implies 3 strength_a
	{'id':11,'n_trees':1, 'strengths':[1,3,2], 'actions':[None,'trees','fish'], 'blames':['low','high','low']},             # implies A trees
	{'id':12,'n_trees':1, 'strengths':[1,2,3], 'actions':[None,'fish','trees'], 'blames':['high','low','high']},            # implies A fished
	{'id':13,'n_trees':3, 'strengths':[3,2,2], 'actions':['fish',None,'fish'], 'blames':['high','medium','low']},           # implies A trees
	{'id':14,'n_trees':3, 'strengths':[2,3,2], 'actions':['fish','fish',None], 'blames':['low','high','low']},              # implies A fished
	{'id':15,'n_trees':3, 'strengths':[3,1,2], 'actions':['fish',None,'trees'], 'blames':['medium','medium','medium']},     # implies A trees
	{'id':16,'n_trees':3, 'strengths':[2,3,1], 'actions':['trees','fish',None], 'blames':['medium','medium','high']},       # implies A fished

	{'id':17,'n_trees':0, 'strengths':[1,2,1], 'actions':[None,'fish',None], 'blames':['high','low','high']},               # 1 tree, A(A,B)=fish very tricky
	{'id':18,'n_trees':3, 'strengths':[0,0,3], 'actions':['trees','trees','trees'], 'blames':['medium','medium','low']},    # A and B prob had sub-3 strengths to be blamed for trees
	{'id':19,'n_trees':3, 'strengths':[1,0,1], 'actions':['fish',None,'fish'], 'blames':['low','high','low']},              # A almost definitely has 3 strength and went fishing
	{'id':20,'n_trees':3, 'strengths':[2,1,0], 'actions':['fish','fish','fish'], 'blames':['low','low','high']},            # A prob has 3 strength and should have cleared trees
	{'id':21,'n_trees':3, 'strengths':[1,1,2], 'actions':[None,None,'fish'], 'blames':['low','low','high']},                # Pivotality: one of A or B fished the other trees, rationality assigns medium to everyone
	{'id':22,'n_trees':0, 'strengths':[1,2,2], 'actions':['trees','trees','trees'], 'blames':['low','medium','medium']},    # implies n_trees=1
	{'id':23,'n_trees':0, 'strengths':[2,1,2], 'actions':['trees','trees','trees'], 'blames':['medium','medium','medium']}, # implies n_trees=2
	{'id':24,'n_trees':0, 'strengths':[2,2,1], 'actions':['trees','trees','trees'], 'blames':['high','high','low']},        # pivotality implies n_trees=3, rationality less committal
	{'id':25,'n_trees':1, 'strengths':[2,3,1], 'actions':['trees',None,'trees'], 'blames':['high','high','low']},           # easy, A went to trees
	{'id':26,'n_trees':1, 'strengths':[2,1,1], 'actions':[None,'fish','fish'], 'blames':['high','medium','medium']},        # rationality says A trees, pivotality says all medium
	{'id':27,'n_trees':1, 'strengths':[1,2,1], 'actions':['fish',None,'fish'], 'blames':['medium','low','medium']},         # rationality says A fish, pivotality wants low high high
	{'id':28,'n_trees':3, 'strengths':[1,2,3], 'actions':['fish',None,None], 'blames':['high','medium','medium']},          # pivotality says C gets lots of blame if A trees B fish <- tricky but cool
	{'id':29,'n_trees':3, 'strengths':[3,1,2], 'actions':[None,'fish',None], 'blames':['high','medium','medium']},          # pivotality says A gets lots of blame if A and B fish <- tricky but cool
	{'id':30,'n_trees':2, 'strengths':[1,1,2], 'actions':[None,None,'fish'], 'blames':['high','medium','medium']},          # pivotality says implies A fished and B trees
	{'id':31,'n_trees':2, 'strengths':[2,1,1], 'actions':['fish',None,None], 'blames':['high','medium','medium']},          # pivotality says implies A and B fished, stronger than rationality
	{'id':32,'n_trees':3, 'strengths':[1,3,0], 'actions':['trees','fish','fish'], 'blames':['medium','medium','low']},      # pivotality says S(A)=1, rationality prefers S(A)=2 but ambivalent
	{'id':33,'n_trees':3, 'strengths':[1,0,3], 'actions':['trees','fish','fish'], 'blames':['medium','high','medium']},     # pivotality says S(A)=2, rationality prefers S(A)=3
	{'id':34,'n_trees':3, 'strengths':[3,1,0], 'actions':['fish','trees','fish'], 'blames':['medium','medium','medium']},   # pivotality says S(A)=3, rationality ambivalent
	{'id':35,'n_trees':3, 'strengths':[3,3,1], 'actions':[None,'trees','fish'], 'blames':['high','high','low']}             # pivotality says A trees, rationality says A fished
]
# converting to a format for csv/running models
trials = pd.DataFrame.from_dict(cases)
trials.n_trees[trials.n_trees==0] = None
for e in range(trials.shape[0]):
	trials.strengths[e] = np.where(np.array(trials.strengths[e])==0, None, trials.strengths[e])
trials.to_csv('trials.csv')

for e in range(len(cases_img)):
	case = cases[e]
	gum = situation_generator(n_trees = case['n_trees'], 
						  strengths = case['strengths'],
						  actions = case['actions'],
						  blames = case['blames'])
	#gum.show()



dd2[(dd2.trees.isnull()*1 + dd2.strength_a.isnull()*1 + dd2.strength_b.isnull()*1) == 1]
ee_a2 = ee_a[(ee_a.trees.isnull()*1 + ee_a.strength_a.isnull()*1 + ee_a.action_a.isnull()*1) == 1]
pp2.sort_values('mean_kld',ascending=False).iloc[::40,:][51:100]



beta=1.5
trees = 3
strength_a = 1
strength_b = 3
strength_c = None
action_a = 1
action_b = 0
action_c = 0
blame_a = .5
blame_b = .5
blame_c = .2
reward = None
print('mixture')
print(situation_inf(a_mixture, beta=beta, trees=trees, strength_a=strength_a, strength_b=strength_b, strength_c=strength_c, 
	action_a=action_a, action_b=action_b, action_c=action_c, reward=reward, blame_a=blame_a, blame_b=blame_b, blame_c=blame_c) )
print('rationality')
print(situation_inf(a_rationality, beta=beta, trees=trees, strength_a=strength_a, strength_b=strength_b, strength_c=strength_c, 
	action_a=action_a, action_b=action_b, action_c=action_c, reward=reward, blame_a=blame_a, blame_b=blame_b, blame_c=blame_c) )
print('pivotality')
print(situation_inf(a_pivotality, beta=beta, trees=trees, strength_a=strength_a, strength_b=strength_b, strength_c=strength_c, 
	action_a=action_a, action_b=action_b, action_c=action_c, reward=reward, blame_a=blame_a, blame_b=blame_b, blame_c=blame_c) )
















