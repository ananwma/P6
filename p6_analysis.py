from p6_game import Simulator

def analyze(design):
    sim = Simulator(design)
    ANALYSIS = {}

	sim = Simulator(design)
	init = sim.get_initial_state()
	moves = sim.get_moves()
	next_state = sim.get_next_state(init, moves[0])

	position, abilities = next_state # or None if character dies
	i, j = position
    raise NotImplementedError

def inspect((i,j), draw_line):
    # TODO: use ANALYSIS and (i,j) draw some lines
    raise NotImplementedError