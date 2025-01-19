// 25 most popular male and female US names of the past 100 years
var names = [{name: "James", gender: "male"},
			 {name: "John", gender: "male"},
			 {name: "Robert", gender: "male"},
			 {name: "Michael", gender: "male"},
			 {name: "William", gender: "male"},
			 {name: "David", gender: "male"},
			 {name: "Richard", gender: "male"},
			 {name: "Joseph", gender: "male"},
			 {name: "Thomas", gender: "male"},
			 {name: "Charles", gender: "male"},
			 {name: "Christopher", gender: "male"},
			 {name: "Daniel", gender: "male"},
			 {name: "Matthew", gender: "male"},
			 {name: "Anthony", gender: "male"},
			 {name: "Donald", gender: "male"},
			 {name: "Mark", gender: "male"},
			 {name: "Paul", gender: "male"},
			 {name: "Steven", gender: "male"},
			 {name: "Andrew", gender: "male"},
			 {name: "Kenneth", gender: "male"},
			 {name: "Joshua", gender: "male"},
			 {name: "Kevin", gender: "male"},
			 {name: "Brian", gender: "male"},
			 {name: "George", gender: "male"},
			 {name: "Edward", gender: "male"},
			 {name: "Mary", gender: "female"},
			 {name: "Patricia", gender: "female"},
			 {name: "Jennifer", gender: "female"},
			 {name: "Linda", gender: "female"},
			 {name: "Elizabeth", gender: "female"},
			 {name: "Barbara", gender: "female"},
			 {name: "Susan", gender: "female"},
			 {name: "Jessica", gender: "female"},
			 {name: "Sarah", gender: "female"},
			 {name: "Karen", gender: "female"},
			 {name: "Nancy", gender: "female"},
			 {name: "Lisa", gender: "female"},
			 {name: "Margaret", gender: "female"},
			 {name: "Betty", gender: "female"},
			 {name: "Sandra", gender: "female"},
			 {name: "Ashley", gender: "female"},
			 {name: "Dorothy", gender: "female"},
			 {name: "Kimberly", gender: "female"},
			 {name: "Emily", gender: "female"},
			 {name: "Donna", gender: "female"},
			 {name: "Michelle", gender: "female"},
			 {name: "Carol", gender: "female"},
			 {name: "Amanda", gender: "female"},
			 {name: "Melissa", gender: "female"},
			 {name: "Deborah", gender: "female"}]


var pronouns = {female: {"subjective": "she",
						 "objective": "her",
						 "possessive": "her",
						 "reflexive": "herself"},
				male: {"subjective": "he",
					   "objective": "him",
					   "possessive": "his",
					   "reflexive": "himself"} }

var scenarios = [{trial: 1,
				  type: "ability",
				  prompt: "__requester__ needed help fixing __possessive__ flat tire. <br> __requester__ asked __firsthelper__ and __secondhelper__ for help, but neither did. <br> __requester__ didn't manage to fix the tire by __reflexive__.", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for not helping.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for not helping."],
				  query: ["Who is better at fixing tires?", "Who is worse at fixing tires?"], 
				  image: "images/noun_flat tire_982179.png"},
				 {trial: 2,
				  type: "ability",
				  prompt: "__requester__ needed help carrying a very heavy couch. <br> __requester__ asked __firsthelper__ and __secondhelper__ for help, but both said no. <br> __requester__ wasn’t able to move the couch on __possessive__ own.", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for not helping.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for not helping."],
				  query: ["Who is stronger?", "Who is weaker?"], 
				  image: "images/noun_Mover Services_1917486.png"},
				 {trial: 3,
				  type: "ability",
				  prompt: "__requester__ needed help reaching something on a high shelf. <br> __requester__ asked __firsthelper__ and __secondhelper__ for help, but both said no. <br> __requester__ wasn’t able to reach the item.", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for not helping.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for not helping."],
				  query: ["Who is taller?", "Who is shorter?"], 
				  image: "images/noun_reach_2900937.png"},
				 {trial: 4,
				  type: "knowledge",
				  prompt: "__requester__ texted __firsthelper__ and __secondhelper__ to pick __objective__ up from the airport. <br> Neither responded to __possessive__ text. <br> __requester__ later learned that only one of them saw __possessive__ message.", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for not helping.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for not helping."],
				  query: ["Who saw the text message?", "Who didn't see the text message?"], 
				  image: "images/noun_Airport_1109705.png"},
				 {trial: 5,
				  type: "knowledge",
				  prompt: "__firsthelper__, __secondhelper__, and __requester__ were having a picnic. <br> Both __firsthelper__ and __secondhelper__ brought snacks with peanuts in them, even though __requester__ was allergic to peanuts. <br>", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for bringing snacks with peanuts to the picnic.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for bringing snacks with peanuts to the picnic."],
				  query: ["Who knew that __requester__ was allergic to peanuts?", "Who didn't know that __requester__ was allergic to peanuts?"], 
				  image: "images/noun_Picnic_2799323.png"},
				 {trial: 6,
				  type: "knowledge",
				  prompt: "__requester__ needed help making dinner. <br> Neither __firsthelper__ nor __secondhelper__ helped. <br>", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for not helping.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for not helping."],
				  query: ["Who knew that __requester__ needed help making dinner?", "Who didn't know that __requester__ needed help making dinner?"], 
				  image: "images/noun_cooking_1176750.png"},
				 {trial: 7,
				  type: "social_roles",
				  prompt: "__requester__ had a birthday party. <br> __requester__ asked __firsthelper__ and __secondhelper__ to come, but neither came. <br>", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for not coming.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for not coming."],
				  query: ["Who is __requester__'s closer friend?", "Who is __requester__'s less close friend?"], 
				  image: "images/noun_birthday party_3315880.png"},
				 {trial: 8,
				  type: "social_roles",
				  prompt: "__requester__ needed help moving. <br> __requester__ asked __firsthelper__ and __secondhelper__ for help, but both said no. <br> __requester__ wasn't able to move __possessive__ stuff on __possessive__ own. <br>", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for not helping.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for not helping."],
				  query: ["Who is __requester__'s closer friend?", "Who is __requester__'s less close friend?"], 
				  image: "images/noun_Mover Services_1917486.png"},
				 {trial: 9,
				  type: "social_roles",
				  prompt: "__requester__ needed help practicing for the school play. <br> __requester__ asked __firsthelper__ and __secondhelper__ for help, but both said no. <br>", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for not helping.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for not helping."],
				  query: ["Who is __requester__'s closer friend?", "Who is __requester__'s less close friend?"], 
				  image: "images/noun_acting_2368308.png"},
				 {trial: 10,
				  type: "intentionality",
				  prompt: "__requester__ fell over while playing soccer with __firsthelper__ and __secondhelper__. <br> Both __firsthelper__ and __secondhelper__ stepped on __requester__. <br>", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for stepping on __objective__.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for stepping on __objective__."],
				  query: ["Who stepped on __requester__ on purpose?", "Who stepped on __requester__ by accident?"], 
				  image: "images/noun_soccer_1751392.png"},
				 {trial: 11,
				  type: "intentionality",
				  prompt: "__requester__ always packs __reflexive__ a lunch to bring to work. <br> One day, __firsthelper__ ate __requester__'s lunch. <br> A different day, __secondhelper__ ate __requester__'s lunch. <br>", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for eating __possessive__ lunch.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for eating __possessive__ lunch."],
				  query: ["Who ate __requester__'s lunch on purpose?", "Who ate __requester__'s lunch accidentally?"], 
				  image: "images/noun_lunch bag_380959.png"},
				 {trial: 12,
				  type: "intentionality",
				  prompt: "__firsthelper__ and __secondhelper__ each had a birthday party in separate weeks. <br> Neither invited __requester__ to the party. <br> __requester__ later learned from a friend that one of them intentionally didn't invite __objective__, and another forgot to invite __objective__. <br>", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for not inviting __objective__ to __firsthelperpossessive__ birthday party.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for not inviting __objective__ to __firsthelperpossessive__ birthday party."],
				  query: ["Who intentionally didn't invite __requester__?", "Who forgot to invite __requester__?"], 
				  image: "images/noun_birthday party_3315880.png"},
				 {trial: 13,
				  type: "effort",
				  prompt: "__requester__ was on a tug of war team with __firsthelper__ and __secondhelper__. <br> Their team lost the game of tug of war. <br> ", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for their loss.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for their loss."],
				  query: ["Who tried very hard?", "Who didn't try very hard?"], 
				  image: "images/noun_We Can Do It_146922.png"},
				 {trial: 14,
				  type: "effort",
				  prompt: "__requester__ was assigned to do a group project with __firsthelper__ and __secondhelper__. <br> Their group did a bad job and received a failing grade for the assignment. <br> ", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for the group's failing grade.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for the group's failing grade."],
				  query: ["Who tried very hard on the assignment?", "Who didn't try very hard on the assignment?"], 
				  image: "images/noun_presentation_1616165.png"},
				 {trial: 15,
				  type: "effort",
				  prompt: "__requester__ needed someone to make an appointment for __objective__. <br> __requester__ asked __firsthelper__ and __secondhelper__ to call and wait on hold for __objective__. <br> __firsthelper__ and __secondhelper__ both gave up before their call was picked up. <br> __requester__ later learned that one of them waited for a few minutes, and another waited for hours. <br>", 
				  blame_assignments: ["__requester__ blamed __firsthelper__ more than __secondhelper__ for hanging up.", "__requester__ blamed __firsthelper__ less than __secondhelper__ for hanging up."],
				  query: ["Who waited for hours before giving up?", "Who waited a few minutes before giving up?"], 
				  image: "images/noun_wait phone_769182.png"},
];
var attention_check = {
	trial: "attention_check",
	prompt: "__requester__ needed someone to mow the lawn. <br> __firsthelper__ mowed the lawn. <br> __secondhelper__ did not mow the lawn. <br>",
	blame_assignments: ["__requester__ blamed __secondhelper__ for not mowing the lawn."],
	query: ["Who mowed the lawn?", "Who mowed the lawn?"],
	image: "images/noun_Man Cutting Grass_637630.png"
}

var all_images = [
	"images/noun_flat tire_982179.png",
	"images/noun_Mover Services_1917486.png",
	"images/noun_reach_2900937.png",
	"images/noun_Airport_1109705.png",
	"images/noun_Picnic_2799323.png",
	"images/noun_cooking_1176750.png",
	"images/noun_birthday party_3315880.png",
	"images/noun_acting_2368308.png",
	"images/noun_soccer_1751392.png",
	"images/noun_lunch bag_380959.png",
	"images/noun_We Can Do It_146922.png",
	"images/noun_presentation_1616165.png",
	"images/noun_wait phone_769182.png"
]






























