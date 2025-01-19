import re
import numpy as np
import math
import random
#Script to shuffle trials for second AMT experiment
#Want to make CSV file with:
#ID Views OnView Trials

def makeImage(trial_str,agent,choice,fname):

	trial_match = re.search('t(\d)\_a(\d)b(\d)c(\d)',trial_str)
	trial = [trial_match.group(2),trial_match.group(3),trial_match.group(4),trial_match.group(1)]
	
	A = 'a'+str(trial[0]) + '.pdf'
	B = 'b'+str(trial[1]) + '.pdf'
	C = 'c'+str(trial[2]) + '.pdf'
	
	import subprocess
	if choice[0] == 0:
		AC = 'AF.pdf'
	else:
		AC = 'AT.pdf'
	if choice[1] == 0:
		BC = 'BF.pdf'
	else:
		BC = 'BT.pdf'
	if choice[2] == 0:
		CC = 'CF.pdf'
	else:
		CC = 'CT.pdf'
	if agent == 0:
		base = 'A.pdf'
	if agent == 1:
		base = 'B.pdf'
	if agent == 2:
		base = 'C.pdf'
		
	check = subprocess.check_call(["sh","gen_map.sh",'t'+str(trial[3])+'.pdf',A,B,C,AC,BC,CC,base,fname])
	if check == 0:
		'BAD! NOT WORKING!'
		
def makeImage3(trial_str,choice,fname):
	trial_match = re.search('t(\d)\_a(\d)b(\d)c(\d)',trial_str)
	trial = [trial_match.group(2),trial_match.group(3),trial_match.group(4),trial_match.group(1)]
	
	A = 'a'+str(trial[0]) + '.pdf'
	B = 'b'+str(trial[1]) + '.pdf'
	C = 'c'+str(trial[2]) + '.pdf'
	
	import subprocess
	if choice[0] == 0:
		AC = 'AF.pdf'
	else:
		AC = 'AT.pdf'
	if choice[1] == 0:
		BC = 'BF.pdf'
	else:
		BC = 'BT.pdf'
	if choice[2] == 0:
		CC = 'CF.pdf'
	else:
		CC = 'CT.pdf'

	base = '.pdf'
	check = subprocess.check_call(["sh","gen_map3.sh",'t'+str(trial[3])+'.pdf',A,B,C,AC,BC,CC,fname])

	if check == 0:
		'BAD! NOT WORKING!'
def getRewards(trial):
	trial_match = re.search('t(\d)\_a(\d)b(\d)c(\d)',trial_str)
	strA = int(trial_match.group(2))
	strB = int(trial_match.group(3))
	strC = int(trial_match.group(4))
	tree = int(trial_match.group(1))
	R = np.zeros((2,2,2))
	if strC >= tree:
		R[0,0,1] = strA+strB
	if strB >= tree:
		R[0,1,0] = strA+strC
	if strB+strC >= tree:
		R[0,1,1] = strA
	if strA >= tree:
		R[1,0,0] = strB+strC
	if strA+strC >= tree:
		R[1,0,1] = strB
	if strA+strB >= tree:
		R[1,1,0] = strC
	return R
		
def getBestAndActual(R,choice):

	best = np.amax(R)
	actual = R[choice]
	return int(best),int(actual)

#ID Views OnView Trials		
def writeCSVfile(file_name,num_trials,num_participants,num_trials_per):
	
	f_out = open(file_name,'w')
	
	pool = set(range(1,num_trials+1))
	print len(pool)
	slen = num_trials_per
	print num_trials
	print num_trials_per
	i=1
	while i <= num_participants:
		set1 = set(random.sample(pool, slen))
		set2 = set(random.sample(list(pool - set1),slen))
		set3 = pool - set1- set2
				
		set1 = list(set1)
		set2 = list(set2)
		set3 = list(set3)
		
		random.shuffle(set1)
		random.shuffle(set2)
		random.shuffle(set3)
		
		print >> f_out, str(i) + ",0,0,"+ " ".join(str(x) for x in set1)
		i = i+1
		print >> f_out, str(i) + ",0,0,"+ " ".join(str(x) for x in set2)
		i = i+1
		print >> f_out, str(i) + ",0,0," + " ".join(str(x) for x in set3)
		i = i+1
	f_out.close()

def writeCSVfileUpdate(file_name,num_trials,num_participants,num_trials_per):
	f_out = open(file_name,'w')
	total_count = [0]*num_trials
	points_per_trial = math.floor(num_participants*num_trials_per/num_trials)
	print points_per_trial
	pool = set(range(1,num_trials+1))
	second_pool = set(range(1,num_trials+1))
	for i in range(0,num_participants):
	  if len(pool) >= num_trials_per:
		set_rand = set(random.sample(list(pool),num_trials_per))
		for item in set_rand:
			total_count[item-1] = total_count[item-1]+1
			if total_count[item-1] >= points_per_trial:
				pool = pool - set([item])
	  else:
		set_rand = pool
		leftover = set(random.sample(second_pool - pool,num_trials_per - len(pool)))
		set_rand = set_rand.union(leftover)
		
		for item in set_rand:
			total_count[item-1] = total_count[item-1]+1
			if total_count[item-1] >= points_per_trial and item in pool:
				pool = pool - set([item])
		for item in leftover:
			second_pool = second_pool - set([item])
			
	  random.shuffle(list(set_rand))
	  print >> f_out, str(i+1) + ",0,0," + " ".join(str(x) for x in set_rand)
	  
	f_out.close()

def switchFishermen(trial,choice,agent):
	trial_match = re.search('t(\d)\_a(\d)b(\d)c(\d)',trial_str)
	if agent == 0:
		trial_out = 't'+trial_match.group(1)+'_a'+trial_match.group(4) + 'b' + trial_match.group(3) + 'c' + trial_match.group(2)
		choice_out = (choice[2],choice[1],choice[0])
		agent_out = 2
	elif agent == 1:
		trial_out = 't'+trial_match.group(1)+ '_a'+trial_match.group(2)+'b'+trial_match.group(4)+'c'+trial_match.group(3)
		choice_out = (choice[0],choice[2],choice[1])
		agent_out = 2
	else:
		agent_out = 2
		trial_out = trial
		choice_out = choice
	return trial_out,choice_out,agent_out

def removeDups(trials,choices):
	trials_nd = []
	choices_nd = []
	i = 0
	print trials
	print choices
	for trial in trials:
		
		if trial in trials_nd and choices[i] == choices_nd[trials_nd.index(trial)]:
			i = i+1
			print 'skipped!'
		else:
			trials_nd.append(trial)
			choices_nd.append(choices[i])
			i = i+1
	return trials_nd, choices_nd
			
#Random select from first part	
trials_r = ['t1_a3b1c2', 't1_a3b1c3', 't2_a3b1c2', 't3_a1b3c3', 't2_a1b2c3','t1_a1b1c1', 't3_a2b2c3', 't2_a2b2c3','t1_a3b3c3', 't2_a2b2c2', 't3_a3b2c3', 't1_a1b2c3', 't3_a3b2c2', 't1_a1b3c3']
agents_r = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]
choices_r = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]

#Pivotal cases with nobody going
trials_pn = ['t2_a1b1c1','t2_a1b1c2','t2_a1b1c2','t2_a1b1c3','t3_a1b1c2','t3_a1b1c2','t3_a2b1c2','t3_a2b1c2','t3_a2b1c3','t3_a2b1c3','t3_a2b2c2']
choices_pn = [(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
agents_pn = [1,0,2,1,0,2,1,2,1,2,2]

#Pivotal cases where pivotality is invoked
trials_p = ['t2_a1b1c1','t2_a1b1c2','t2_a1b1c2','t2_a1b1c3','t3_a1b1c2','t3_a1b1c2','t3_a2b1c2','t3_a2b1c2','t3_a2b1c3','t3_a2b1c3','t3_a2b2c2']
choices_p = [(0,1,0),(0,1,0),(0,1,0),(1,0,0),(0,0,1),(0,1,0),(0,0,1),(0,1,0),(0,1,0),(1,0,0),(0,0,1)]
agents_p = [0,0,2,1,1,0,1,0,0,1,1]

#non-optimal cases that were not obvious for agents
trials_no= ['t2_a2b2c1','t2_a2b2c2','t2_a2b2c2','t2_a1b1c1','t2_a1b1c2','t2_a1b1c2','t1_a1b1c3','t1_a1b1c3','t1_a1b1c1','t1_a1b1c1','t3_a2b1c2','t3_a2b1c2','t3_a3b1c2','t3_a3b1c2','t3_a3b1c2','t3_a3b1c2','t3_a3b3c1','t3_a3b3c3','t3_a3b3c3']
agents_no = [0,0,0,0,0,1,0,2,0,2,1,2,0,1,0,2,0,0,0]
choices_no = [(1,1,0),(1,1,1),(1,1,0),(1,1,1),(1,0,1),(1,0,1),(0,0,1),(0,0,1),(1,1,0),(1,1,0),(1,0,1),(1,0,1),(1,1,0),(1,1,0),(1,0,1),(1,0,1),(1,1,0),(1,1,0),(1,1,1)]
 
#non-optimal but more obvious cases
trials_mo = ['t1_a3b1c2','t1_a3b1c3', 't2_a3b1c2', 't3_a1b3c3', 't3_a2b3c3', 't2_a1b2c3', 't2_a1b2c3','t3_a2b2c3', 't1_a1b2c3','t1_a1b2c3', 't3_a3b2c2','t3_a3b2c2', 't1_a1b3c3','t1_a1b3c3','t1_a1b3c3','t2_a1b2c2','t2_a1b1c3','t2_a1b1c3','t2_a1b1c3','t2_a1b1c3']
choices_mo = [(1,1,0)   ,(0,1,1)    ,(1,0,1)     ,(1,1,0)     ,(1,1,0)     ,(1,1,0)     ,(1,0,0)     ,(0,1,1)    ,(1,0,1)     ,(1,1,0)    ,(0,1,1)     ,(0,1,1)    ,(1,1,0)     ,(0,1,0)    ,(0,1,0)    ,(1,0,1)    ,(0,0,1)    ,(0,0,1)    ,(1,0,1)    ,    (1,0,1)]
agents_mo =  [0         ,2          ,0           ,0           ,0           ,0           ,0           ,2          ,2           ,1          ,0           ,1          ,0           ,1          ,0          ,0          ,1          ,2          ,1           ,         2]
print len(trials_mo)
print len(choices_mo)
print len(agents_mo)

print len(choices_r) == len(agents_r) and len(trials_r) == len(choices_r)
print len(choices_p) == len(agents_p) and len(trials_p) == len(choices_p)
print len(choices_pn) == len(agents_pn) and len(trials_pn) == len(choices_pn)
print len(choices_no) == len(agents_no) and len(trials_no) == len(choices_no)
print len(choices_mo) == len(agents_mo) and len(trials_mo) == len(choices_mo)

num_participants = 15
num_trials = len(trials_r)+len(trials_p)+len(trials_pn)+len(trials_no) + len(trials_mo)
file_name = 'randomized_trials_SQL.csv'
writeCSVfile(file_name,num_trials,num_participants,25)

num_trials_3 = 63
num_participants = 45
file_name3 = 'randomized_trials_SQL_all3.csv'
writeCSVfile(file_name3,num_trials_3,num_participants,21)

f_out_reward = open('reward_vals_C.csv','w')
f_out_reward3 = open('reward_vals_3.csv','w')
all_best = []
all_actual = []
all_best3 = []
all_actual3 = []
all_trials_3 = []
all_choices_3 = []
j = 1
k = 1

#Normal trials
(trials_3, choices_3) = removeDups(trials_r,choices_r)
all_trials_3.append(trials_3)
all_choices_3.append(choices_3)
for i in range(0,len(trials_3)):
	trial_str = trials_3[i]
	choice = choices_3[i]
	makeImage3(trial_str,choice,trial_str + str(choice) + '.pdf')
	R = getRewards(trial_str)
	best_3,actual_3 = getBestAndActual(R,choice)
	all_best3.append(best_3)
	all_actual3.append(actual_3)
	k = k+1
	
for i in range(0,len(trials_r)):
	trial_str = trials_r[i]
	agent = agents_r[i]
	choice = choices_r[i]
	
	trial_o,choice_o,agent_o = switchFishermen(trial_str,choice,agent)

	#makeImage(trial_o,agent_o,choice_o,str(j)+'.pdf')

	R = getRewards(trial_o)
	best,actual = getBestAndActual(R,choice_o)
	all_best.append(best)
	all_actual.append(actual)
	
	j = j+1
#Pivotal trials
(trials_3, choices_3) = removeDups(trials_p,choices_p)
all_trials_3.append(trials_3)
all_choices_3.append(choices_3)
for i in range(0,len(trials_3)):
	trial_str = trials_3[i]
	choice = choices_3[i]
	makeImage3(trial_str,choice,trial_str + str(choice) + '.pdf')
	R = getRewards(trial_str)
	best_3,actual_3 = getBestAndActual(R,choice)
	all_best3.append(best_3)
	all_actual3.append(actual_3)
	k = k+1
for i in range(0,len(trials_p)):
	trial_str = trials_p[i]
	agent = agents_p[i]
	choice = choices_p[i]
	
	trial_o,choice_o,agent_o = switchFishermen(trial_str,choice,agent)
	makeImage(trial_o,agent_o,choice_o,trial_o + str(choice_o)+'.pdf')

	R = getRewards(trial_o)
	best,actual = getBestAndActual(R,choice_o)
	all_best.append(best)
	all_actual.append(actual)

	j = j+1

#Pivotal trials
(trials_3, choices_3) = removeDups(trials_pn,choices_pn)
all_trials_3.append(trials_3)
all_choices_3.append(choices_3)
for i in range(0,len(trials_3)):
	trial_str = trials_3[i]
	choice = choices_3[i]
	makeImage3(trial_str,choice,trial_str + str(choice)  + '.pdf')
	R = getRewards(trial_str)
	best_3,actual_3 = getBestAndActual(R,choice)
	all_best3.append(best_3)
	all_actual3.append(actual_3)
	k = k+1	
for i in range(0,len(trials_pn)):
	trial_str = trials_pn[i]
	agent = agents_pn[i]
	choice = choices_pn[i]
	
	trial_o,choice_o,agent_o = switchFishermen(trial_str,choice,agent)
	makeImage(trial_o,agent_o,choice_o,trial_o + str(choice_o)+'.pdf')

	R = getRewards(trial_o)
	best,actual = getBestAndActual(R,choice_o)	
	all_best.append(best)
	all_actual.append(actual)
	j = j+1

	#Pivotal trials
(trials_3, choices_3) = removeDups(trials_no,choices_no)
all_trials_3.append(trials_3)
all_choices_3.append(choices_3)
for i in range(0,len(trials_3)):
	trial_str = trials_3[i]
	choice = choices_3[i]
	makeImage3(trial_str,choice,trial_str + str(choice) + '.pdf')
	R = getRewards(trial_str)
	best_3,actual_3 = getBestAndActual(R,choice)
	all_best3.append(best_3)
	all_actual3.append(actual_3)
	k = k+1
for i in range(0,len(trials_no)):
	trial_str = trials_no[i]
	agent = agents_no[i]
	choice = choices_no[i]
	
	trial_o,choice_o,agent_o = switchFishermen(trial_str,choice,agent)
	makeImage(trial_o,agent_o,choice_o,trial_o + str(choice_o)+'.pdf')

	R = getRewards(trial_o)
	best,actual = getBestAndActual(R,choice_o)
	all_best.append(best)
	all_actual.append(actual)
	j = j+1
	
#Pivotal trials
(trials_3, choices_3) = removeDups(trials_mo,choices_mo)
all_trials_3.append(trials_3)
all_choices_3.append(choices_3)
for i in range(0,len(trials_3)):
	trial_str = trials_3[i]
	choice = choices_3[i]
	
	makeImage3(trial_str,choice,trial_str + str(choice) +'.pdf')
	R = getRewards(trial_str)
	best_3,actual_3 = getBestAndActual(R,choice)
	all_best3.append(best_3)
	all_actual3.append(actual_3)
	k = k+1
for i in range(0,len(trials_mo)):
	trial_str = trials_mo[i]
	agent = agents_mo[i]
	choice = choices_mo[i]
	
	trial_o,choice_o,agent_o = switchFishermen(trial_str,choice,agent)
	makeImage(trial_o,agent_o,choice_o,str(j)+'.pdf')

	R = getRewards(trial_o)
	best,actual = getBestAndActual(R,choice_o)
	all_best.append(best)
	all_actual.append(actual)
	j = j+1

print >> f_out_reward, " ".join(str(x) for x in all_actual) + "," + " ".join(str(x) for x in all_best)
print len(all_actual3)
print >> f_out_reward3, " ".join(str(x) for x in all_actual3) + "," + " ".join(str(x) for x in all_best3)
f_out_reward.close()
'''
f_test = open('testfile','w')
print >> f_test, all_trials_3
print >> f_test, all_choices_3
f_test.close()

#Both go even though only oen has to
t2_a2b2c1: (1,1,0)
t2_a2b2c2: (1,1,1)
t2_a2b2c2: (1,1,0)
t2_a1b1c1: (1,1,1)
t2_a1b1c2: (1,0,1) 0,1
t1_a1b1c3: (0,0,1) 0,2
t1_a1b1c1: (1,1,0) 0,2
t3_a2b1c2: (1,0,1) 1,2
t3_a3b1c2: (1,1,0) 0,1
t3_a3b1c2: (1,0,1) 0,2
t3_a3b3c1: (1,1,0) 0
t3_a3b3c3: (1,1,0) 0
t3_a3b3c3: (1,1,1) 0
'''
