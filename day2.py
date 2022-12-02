filepath = 'data/day2.txt'

ROCK = 'Rock'
PAPER = 'Paper'
SCISSORS = 'Scissors'
WIN = 'win'
DRAW = 'draw'
LOSS = 'loss'

default_play = {
	'X': ROCK,
	'Y': PAPER,
	'Z': SCISSORS,
	'A': ROCK,
	'B': PAPER,
	'C': SCISSORS
}

result_points = {
	WIN: 6,
	DRAW: 3,
	LOSS: 0
}

default_points = {
	ROCK: 1,
	PAPER: 2,
	SCISSORS: 3
}

class Guide:
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
    self.win_matrix = {
    	'X': {
    		'A': result_points[DRAW],
    		'B': result_points[LOSS],
    		'C': result_points[WIN]
    	},
    	'Y': {
    		'A': result_points[WIN],
    		'B': result_points[DRAW],
    		'C': result_points[LOSS]
    	},
    	'Z': {
    		'A': result_points[LOSS],
    		'B': result_points[WIN],
    		'C': result_points[DRAW]
    	}
    }
    # A=rock, B=paper, C=scissors
    # X=lose, Y=draw, Z=win
    self.part2_matrix = {
    	'A': {
    		'X': default_points[SCISSORS] + result_points[LOSS],
    		'Y': default_points[ROCK] + result_points[DRAW],
    		'Z': default_points[PAPER] + result_points[WIN]
    	},
    	'B': {
    		'X': default_points[ROCK] + result_points[LOSS],
    		'Y': default_points[PAPER] + result_points[DRAW],
    		'Z': default_points[SCISSORS] + result_points[WIN]
    	},
    	'C': {
    		'X': default_points[PAPER] + result_points[LOSS],
    		'Y': default_points[SCISSORS] + result_points[DRAW],
    		'Z': default_points[ROCK] + result_points[WIN]
    	}
    }

  def play(self):
  	return self.win_matrix[self.p2][self.p1]

  def play2(self):
  	return self.part2_matrix[self.p1][self.p2]

with open(filepath) as f:
    rounds = f.read().split('\n')

part1_points = 0
part2_points = 0

for rnd in rounds:
	rndsplit = rnd.split(' ')
	g = Guide(rndsplit[0], rndsplit[1])
	part1_points += g.play() + default_points[default_play[rndsplit[1]]]
	part2_points += g.play2()

print(part1_points)
print(part2_points)
