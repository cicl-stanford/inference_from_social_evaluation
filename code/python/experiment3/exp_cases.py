import numpy as np

all_cases = [
[
[{
'strengths': (3, 1, 2),
'trees': 1,
'choices': (0, 0, 0)
}],
[{
'strengths': (3, 1, 3),
'trees': 1,
'choices': (0, 0, 0)
}],
[{
'strengths': (1, 3, 3),
'trees': 3,
'choices': (0, 0, 0)
}],
[{
'strengths': (1, 2, 3),
'trees': 2,
'choices': (0, 0, 0)
}],
[{
'strengths': (1, 1, 1),
'trees': 1,
'choices': (0, 0, 0)
}],
[{
'strengths': (2, 2, 3),
'trees': 3,
'choices': (0, 0, 0)
}],
[{
'strengths': (3, 3, 3),
'trees': 1,
'choices': (0, 0, 0)
}],
[{
'strengths': (2, 2, 2),
'trees': 2,
'choices': (0, 0, 0)
}],
[{
'strengths': (3, 2, 3),
'trees': 3,
'choices': (0, 0, 0)
}],
[{
'strengths': (1, 2, 3),
'trees': 1,
'choices': (0, 0, 0)
}],
[{
'strengths': (3, 2, 2),
'trees': 3,
'choices': (0, 0, 0)
}],
[{
'strengths': (1, 3, 3),
'trees': 1,
'choices': (0, 0, 0)
}]
],
# pivotal cases where nobodys going
[
[{
'strengths': (1, 1, 1),
'trees': 2,
'choices': (0, 0, 0)
}],
[{
'strengths': (1, 2, 2),
'trees': 2,
'choices': (0, 0, 0)
}],
[{
'strengths': (1, 1, 2),
'trees': 2,
'choices': (0, 0, 0)
}],
[{
'strengths': (1, 1, 3),
'trees': 2,
'choices': (0, 0, 0)
}],
[{
'strengths': (1, 1, 2),
'trees': 3,
'choices': (0, 0, 0)
}],
[{
'strengths': (2, 1, 2),
'trees': 3,
'choices': (0, 0, 0)
}],
[{
'strengths': (2, 1, 3),
'trees': 3,
'choices': (0, 0, 0)
}],
[{
'strengths': (2, 2, 2),
'trees': 3,
'choices': (0, 0, 0)
}]
],
# pivotal cases where pivotality is invoked
[
[{
'strengths': (1, 1, 1),
'trees': 2,
'choices': (0, 1, 0)
}],
[{
'strengths': (1, 1, 2),
'trees': 2,
'choices': (0, 1, 0)
}],
[{
'strengths': (1, 1, 3),
'trees': 2,
'choices': (1, 0, 0)
}],
[{
'strengths': (1, 1, 2),
'trees': 3,
'choices': (0, 0, 1)
}],
[{
'strengths': (1, 1, 2),
'trees': 3,
'choices': (0, 1, 0)
}],
[{
'strengths': (2, 1, 2),
'trees': 3,
'choices': (0, 0, 1)
}],
[{
'strengths': (2, 1, 2),
'trees': 3,
'choices': (0, 1, 0)
}],
[{
'strengths': (2, 1, 3),
'trees': 3,
'choices': (0, 1, 0)
}],
[{
'strengths': (2, 1, 3),
'trees': 3,
'choices': (1, 0, 0)
}],
[{
'strengths': (2, 2, 2),
'trees': 3,
'choices': (0, 0, 1)
}]
],
# non-optimal cases that were not obvious for agents
[
[{
'strengths': (2, 2, 1),
'trees': 2,
'choices': (1, 1, 0)
}],
[{
'strengths': (2, 2, 2),
'trees': 2,
'choices': (1, 1, 1)
}],
[{
'strengths': (2, 2, 2),
'trees': 2,
'choices': (1, 1, 0)
}],
[{
'strengths': (1, 1, 1),
'trees': 2,
'choices': (1, 1, 1)
}],
[{
'strengths': (1, 1, 2),
'trees': 2,
'choices': (1, 0, 1)
}],
[{
'strengths': (1, 1, 3),
'trees': 1,
'choices': (0, 0, 1)
}],
[{
'strengths': (1, 1, 1),
'trees': 1,
'choices': (1, 1, 0)
}],
[{
'strengths': (2, 1, 2),
'trees': 3,
'choices': (1, 0, 1)
}],
[{
'strengths': (3, 1, 2),
'trees': 3,
'choices': (1, 1, 0)
}],
[{
'strengths': (3, 1, 2),
'trees': 3,
'choices': (1, 0, 1)
}],
[{
'strengths': (3, 3, 1),
'trees': 3,
'choices': (1, 1, 0)
}],
[{
'strengths': (3, 3, 3),
'trees': 3,
'choices': (1, 1, 0)
}],
[{
'strengths': (3, 3, 3),
'trees': 3,
'choices': (1, 1, 1)
}]
],	
# non-optimal but more obvious cases
[
[{
'strengths': (3, 1, 2),
'trees': 1,
'choices': (1, 1, 0)
}],
[{
'strengths': (3, 1, 3),
'trees': 1,
'choices': (0, 1, 1)
}],
[{
'strengths': (3, 1, 2),
'trees': 2,
'choices': (1, 0, 1)
}],
[{
'strengths': (1, 3, 3),
'trees': 3,
'choices': (1, 1, 0)
}],
[{
'strengths': (2, 3, 3),
'trees': 3,
'choices': (1, 1, 0)
}],
[{
'strengths': (1, 2, 3),
'trees': 2,
'choices': (1, 1, 0)
}],
[{
'strengths': (1, 2, 3),
'trees': 2,
'choices': (1, 0, 0)
}],
[{
'strengths': (2, 2, 3),
'trees': 3,
'choices': (0, 1, 1)
}],
[{
'strengths': (1, 2, 3),
'trees': 1,
'choices': (1, 0, 1)
}],
[{
'strengths': (1, 2, 3),
'trees': 1,
'choices': (1, 1, 0)
}],
[{
'strengths': (3, 2, 2),
'trees': 3,
'choices': (0, 1, 1)
}],
[{
'strengths': (1, 3, 3),
'trees': 1,
'choices': (1, 1, 0)
}],
[{
'strengths': (1, 3, 3),
'trees': 1,
'choices': (0, 1, 0)
}],
[{
'strengths': (1, 2, 2),
'trees': 1,
'choices': (1, 0, 1)
}],
[{
'strengths': (1, 1, 3),
'trees': 2,
'choices': (0, 0, 1)
}],
[{
'strengths': (1, 1, 3),
'trees': 2,
'choices': (1, 0, 1)
}]
]
]

for i in all_cases:
	for case in i:
		strengths = case[0]['strengths']
		trees = case[0]['trees']
		choices = case[0]['choices']

		# add mid range
		case.append({'strengths':tuple(a*2 for a in strengths), 'trees':trees*2, 'choices':choices})

		# add high range
		case.append({'strengths':tuple(a*3 for a in strengths), 'trees':trees*3, 'choices':choices})