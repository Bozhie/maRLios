ACTION_SPACE = [
    ['A'], 
    ['A', 'B'], 
    ['A', 'B', 'down'], 
    ['A', 'B', 'down', 'left'], 
    ['A', 'B', 'down', 'right'], 
    ['A', 'B', 'left'], 
    ['A', 'B', 'right'], 
    ['A', 'down'], 
    ['A', 'down', 'left'], 
    ['A', 'down', 'right'], 
    ['A', 'left'], 
    ['A', 'right'], 
    ['B'], 
    ['B', 'down'], 
    ['B', 'down', 'left'], 
    ['B', 'down', 'right'], 
    ['B', 'left'], 
    ['B', 'right'], 
    ['NOOP'], 
    ['down'], 
    ['down', 'left'], 
    ['down', 'right'], 
    ['left'], 
    ['right']
]

BUTTONS = ['A',
            'B', 
            'down', 
            'left', 
            'right']

BUTTON_MAP = {'A' : 0,
            'B': 1,
            'down': 2,
            'left': 3 ,
            'right': 4}

TWO_ACTIONS_SET = [
    [['A'], ['A']], 
    [['A'], ['A', 'B']], 
    [['A'], ['A', 'B', 'down']], 
    [['A'], ['A', 'B', 'down', 'left']], 
    [['A'], ['A', 'B', 'down', 'right']], 
    [['A'], ['A', 'B', 'left']], 
    [['A'], ['A', 'B', 'right']], 
    [['A'], ['A', 'down']], 
    [['A'], ['A', 'down', 'left']], 
    [['A'], ['A', 'down', 'right']], 
    [['A'], ['A', 'left']], 
    [['A'], ['A', 'right']], 
    [['A'], ['B']], 
    [['A'], ['B', 'down']], 
    [['A'], ['B', 'down', 'left']], 
    [['A'], ['B', 'down', 'right']], 
    [['A'], ['B', 'left']], 
    [['A'], ['B', 'right']], 
    [['A'], ['NOOP']], 
    [['A'], ['down']], 
    [['A'], ['down', 'left']], 
    [['A'], ['down', 'right']], 
    [['A'], ['left']], 
    [['A'], ['right']], 
    [['A', 'B'], ['A']], 
    [['A', 'B'], ['A', 'B']], 
    [['A', 'B'], ['A', 'B', 'down']], 
    [['A', 'B'], ['A', 'B', 'down', 'left']], 
    [['A', 'B'], ['A', 'B', 'down', 'right']], 
    [['A', 'B'], ['A', 'B', 'left']], 
    [['A', 'B'], ['A', 'B', 'right']], 
    [['A', 'B'], ['A', 'down']], 
    [['A', 'B'], ['A', 'down', 'left']], 
    [['A', 'B'], ['A', 'down', 'right']], 
    [['A', 'B'], ['A', 'left']], 
    [['A', 'B'], ['A', 'right']], 
    [['A', 'B'], ['B']], 
    [['A', 'B'], ['B', 'down']], 
    [['A', 'B'], ['B', 'down', 'left']], 
    [['A', 'B'], ['B', 'down', 'right']], 
    [['A', 'B'], ['B', 'left']], 
    [['A', 'B'], ['B', 'right']], 
    [['A', 'B'], ['NOOP']], 
    [['A', 'B'], ['down']], 
    [['A', 'B'], ['down', 'left']], 
    [['A', 'B'], ['down', 'right']], 
    [['A', 'B'], ['left']], 
    [['A', 'B'], ['right']], 
    [['A', 'B', 'down'], ['A']], 
    [['A', 'B', 'down'], ['A', 'B']], 
    [['A', 'B', 'down'], ['A', 'B', 'down']], 
    [['A', 'B', 'down'], ['A', 'B', 'down', 'left']], 
    [['A', 'B', 'down'], ['A', 'B', 'down', 'right']], 
    [['A', 'B', 'down'], ['A', 'B', 'left']], 
    [['A', 'B', 'down'], ['A', 'B', 'right']], 
    [['A', 'B', 'down'], ['A', 'down']], 
    [['A', 'B', 'down'], ['A', 'down', 'left']], 
    [['A', 'B', 'down'], ['A', 'down', 'right']], 
    [['A', 'B', 'down'], ['A', 'left']], 
    [['A', 'B', 'down'], ['A', 'right']], 
    [['A', 'B', 'down'], ['B']], 
    [['A', 'B', 'down'], ['B', 'down']], 
    [['A', 'B', 'down'], ['B', 'down', 'left']], 
    [['A', 'B', 'down'], ['B', 'down', 'right']], 
    [['A', 'B', 'down'], ['B', 'left']], 
    [['A', 'B', 'down'], ['B', 'right']], 
    [['A', 'B', 'down'], ['NOOP']], 
    [['A', 'B', 'down'], ['down']], 
    [['A', 'B', 'down'], ['down', 'left']], 
    [['A', 'B', 'down'], ['down', 'right']], 
    [['A', 'B', 'down'], ['left']], 
    [['A', 'B', 'down'], ['right']], 
    [['A', 'B', 'down', 'left'], ['A']], 
    [['A', 'B', 'down', 'left'], ['A', 'B']], 
    [['A', 'B', 'down', 'left'], ['A', 'B', 'down']], 
    [['A', 'B', 'down', 'left'], ['A', 'B', 'down', 'left']], 
    [['A', 'B', 'down', 'left'], ['A', 'B', 'down', 'right']], 
    [['A', 'B', 'down', 'left'], ['A', 'B', 'left']], 
    [['A', 'B', 'down', 'left'], ['A', 'B', 'right']], 
    [['A', 'B', 'down', 'left'], ['A', 'down']], 
    [['A', 'B', 'down', 'left'], ['A', 'down', 'left']], 
    [['A', 'B', 'down', 'left'], ['A', 'down', 'right']], 
    [['A', 'B', 'down', 'left'], ['A', 'left']], 
    [['A', 'B', 'down', 'left'], ['A', 'right']], 
    [['A', 'B', 'down', 'left'], ['B']], 
    [['A', 'B', 'down', 'left'], ['B', 'down']], 
    [['A', 'B', 'down', 'left'], ['B', 'down', 'left']], 
    [['A', 'B', 'down', 'left'], ['B', 'down', 'right']], 
    [['A', 'B', 'down', 'left'], ['B', 'left']], 
    [['A', 'B', 'down', 'left'], ['B', 'right']], 
    [['A', 'B', 'down', 'left'], ['NOOP']], 
    [['A', 'B', 'down', 'left'], ['down']], 
    [['A', 'B', 'down', 'left'], ['down', 'left']], 
    [['A', 'B', 'down', 'left'], ['down', 'right']], 
    [['A', 'B', 'down', 'left'], ['left']], 
    [['A', 'B', 'down', 'left'], ['right']], 
    [['A', 'B', 'down', 'right'], ['A']], 
    [['A', 'B', 'down', 'right'], ['A', 'B']], 
    [['A', 'B', 'down', 'right'], ['A', 'B', 'down']], 
    [['A', 'B', 'down', 'right'], ['A', 'B', 'down', 'left']], 
    [['A', 'B', 'down', 'right'], ['A', 'B', 'down', 'right']], 
    [['A', 'B', 'down', 'right'], ['A', 'B', 'left']], 
    [['A', 'B', 'down', 'right'], ['A', 'B', 'right']], 
    [['A', 'B', 'down', 'right'], ['A', 'down']], 
    [['A', 'B', 'down', 'right'], ['A', 'down', 'left']], 
    [['A', 'B', 'down', 'right'], ['A', 'down', 'right']], 
    [['A', 'B', 'down', 'right'], ['A', 'left']], 
    [['A', 'B', 'down', 'right'], ['A', 'right']], 
    [['A', 'B', 'down', 'right'], ['B']], 
    [['A', 'B', 'down', 'right'], ['B', 'down']], 
    [['A', 'B', 'down', 'right'], ['B', 'down', 'left']], 
    [['A', 'B', 'down', 'right'], ['B', 'down', 'right']], 
    [['A', 'B', 'down', 'right'], ['B', 'left']], 
    [['A', 'B', 'down', 'right'], ['B', 'right']], 
    [['A', 'B', 'down', 'right'], ['NOOP']], 
    [['A', 'B', 'down', 'right'], ['down']], 
    [['A', 'B', 'down', 'right'], ['down', 'left']], 
    [['A', 'B', 'down', 'right'], ['down', 'right']], 
    [['A', 'B', 'down', 'right'], ['left']], 
    [['A', 'B', 'down', 'right'], ['right']], 
    [['A', 'B', 'left'], ['A']], 
    [['A', 'B', 'left'], ['A', 'B']], 
    [['A', 'B', 'left'], ['A', 'B', 'down']], 
    [['A', 'B', 'left'], ['A', 'B', 'down', 'left']], 
    [['A', 'B', 'left'], ['A', 'B', 'down', 'right']], 
    [['A', 'B', 'left'], ['A', 'B', 'left']], 
    [['A', 'B', 'left'], ['A', 'B', 'right']], 
    [['A', 'B', 'left'], ['A', 'down']], 
    [['A', 'B', 'left'], ['A', 'down', 'left']], 
    [['A', 'B', 'left'], ['A', 'down', 'right']], 
    [['A', 'B', 'left'], ['A', 'left']], 
    [['A', 'B', 'left'], ['A', 'right']], 
    [['A', 'B', 'left'], ['B']], 
    [['A', 'B', 'left'], ['B', 'down']], 
    [['A', 'B', 'left'], ['B', 'down', 'left']], 
    [['A', 'B', 'left'], ['B', 'down', 'right']], 
    [['A', 'B', 'left'], ['B', 'left']], 
    [['A', 'B', 'left'], ['B', 'right']], 
    [['A', 'B', 'left'], ['NOOP']], 
    [['A', 'B', 'left'], ['down']], 
    [['A', 'B', 'left'], ['down', 'left']], 
    [['A', 'B', 'left'], ['down', 'right']], 
    [['A', 'B', 'left'], ['left']], 
    [['A', 'B', 'left'], ['right']], 
    [['A', 'B', 'right'], ['A']], 
    [['A', 'B', 'right'], ['A', 'B']], 
    [['A', 'B', 'right'], ['A', 'B', 'down']], 
    [['A', 'B', 'right'], ['A', 'B', 'down', 'left']], 
    [['A', 'B', 'right'], ['A', 'B', 'down', 'right']], 
    [['A', 'B', 'right'], ['A', 'B', 'left']], 
    [['A', 'B', 'right'], ['A', 'B', 'right']], 
    [['A', 'B', 'right'], ['A', 'down']], 
    [['A', 'B', 'right'], ['A', 'down', 'left']], 
    [['A', 'B', 'right'], ['A', 'down', 'right']], 
    [['A', 'B', 'right'], ['A', 'left']], 
    [['A', 'B', 'right'], ['A', 'right']], 
    [['A', 'B', 'right'], ['B']], 
    [['A', 'B', 'right'], ['B', 'down']], 
    [['A', 'B', 'right'], ['B', 'down', 'left']], 
    [['A', 'B', 'right'], ['B', 'down', 'right']], 
    [['A', 'B', 'right'], ['B', 'left']], 
    [['A', 'B', 'right'], ['B', 'right']], 
    [['A', 'B', 'right'], ['NOOP']], 
    [['A', 'B', 'right'], ['down']], 
    [['A', 'B', 'right'], ['down', 'left']], 
    [['A', 'B', 'right'], ['down', 'right']], 
    [['A', 'B', 'right'], ['left']], 
    [['A', 'B', 'right'], ['right']], 
    [['A', 'down'], ['A']], 
    [['A', 'down'], ['A', 'B']], 
    [['A', 'down'], ['A', 'B', 'down']], 
    [['A', 'down'], ['A', 'B', 'down', 'left']], 
    [['A', 'down'], ['A', 'B', 'down', 'right']], 
    [['A', 'down'], ['A', 'B', 'left']], 
    [['A', 'down'], ['A', 'B', 'right']], 
    [['A', 'down'], ['A', 'down']], 
    [['A', 'down'], ['A', 'down', 'left']], 
    [['A', 'down'], ['A', 'down', 'right']], 
    [['A', 'down'], ['A', 'left']], 
    [['A', 'down'], ['A', 'right']], 
    [['A', 'down'], ['B']], 
    [['A', 'down'], ['B', 'down']], 
    [['A', 'down'], ['B', 'down', 'left']], 
    [['A', 'down'], ['B', 'down', 'right']], 
    [['A', 'down'], ['B', 'left']], 
    [['A', 'down'], ['B', 'right']], 
    [['A', 'down'], ['NOOP']], 
    [['A', 'down'], ['down']], 
    [['A', 'down'], ['down', 'left']], 
    [['A', 'down'], ['down', 'right']], 
    [['A', 'down'], ['left']], 
    [['A', 'down'], ['right']], 
    [['A', 'down', 'left'], ['A']], 
    [['A', 'down', 'left'], ['A', 'B']], 
    [['A', 'down', 'left'], ['A', 'B', 'down']], 
    [['A', 'down', 'left'], ['A', 'B', 'down', 'left']], 
    [['A', 'down', 'left'], ['A', 'B', 'down', 'right']], 
    [['A', 'down', 'left'], ['A', 'B', 'left']], 
    [['A', 'down', 'left'], ['A', 'B', 'right']], 
    [['A', 'down', 'left'], ['A', 'down']], 
    [['A', 'down', 'left'], ['A', 'down', 'left']], 
    [['A', 'down', 'left'], ['A', 'down', 'right']], 
    [['A', 'down', 'left'], ['A', 'left']], 
    [['A', 'down', 'left'], ['A', 'right']], 
    [['A', 'down', 'left'], ['B']], 
    [['A', 'down', 'left'], ['B', 'down']], 
    [['A', 'down', 'left'], ['B', 'down', 'left']], 
    [['A', 'down', 'left'], ['B', 'down', 'right']], 
    [['A', 'down', 'left'], ['B', 'left']], 
    [['A', 'down', 'left'], ['B', 'right']], 
    [['A', 'down', 'left'], ['NOOP']], 
    [['A', 'down', 'left'], ['down']], 
    [['A', 'down', 'left'], ['down', 'left']], 
    [['A', 'down', 'left'], ['down', 'right']], 
    [['A', 'down', 'left'], ['left']], 
    [['A', 'down', 'left'], ['right']], 
    [['A', 'down', 'right'], ['A']], 
    [['A', 'down', 'right'], ['A', 'B']], 
    [['A', 'down', 'right'], ['A', 'B', 'down']], 
    [['A', 'down', 'right'], ['A', 'B', 'down', 'left']], 
    [['A', 'down', 'right'], ['A', 'B', 'down', 'right']], 
    [['A', 'down', 'right'], ['A', 'B', 'left']], 
    [['A', 'down', 'right'], ['A', 'B', 'right']], 
    [['A', 'down', 'right'], ['A', 'down']], 
    [['A', 'down', 'right'], ['A', 'down', 'left']], 
    [['A', 'down', 'right'], ['A', 'down', 'right']], 
    [['A', 'down', 'right'], ['A', 'left']], 
    [['A', 'down', 'right'], ['A', 'right']], 
    [['A', 'down', 'right'], ['B']], 
    [['A', 'down', 'right'], ['B', 'down']], 
    [['A', 'down', 'right'], ['B', 'down', 'left']], 
    [['A', 'down', 'right'], ['B', 'down', 'right']], 
    [['A', 'down', 'right'], ['B', 'left']], 
    [['A', 'down', 'right'], ['B', 'right']], 
    [['A', 'down', 'right'], ['NOOP']], 
    [['A', 'down', 'right'], ['down']], 
    [['A', 'down', 'right'], ['down', 'left']], 
    [['A', 'down', 'right'], ['down', 'right']], 
    [['A', 'down', 'right'], ['left']], 
    [['A', 'down', 'right'], ['right']], 
    [['A', 'left'], ['A']], 
    [['A', 'left'], ['A', 'B']], 
    [['A', 'left'], ['A', 'B', 'down']], 
    [['A', 'left'], ['A', 'B', 'down', 'left']], 
    [['A', 'left'], ['A', 'B', 'down', 'right']], 
    [['A', 'left'], ['A', 'B', 'left']], 
    [['A', 'left'], ['A', 'B', 'right']], 
    [['A', 'left'], ['A', 'down']], 
    [['A', 'left'], ['A', 'down', 'left']], 
    [['A', 'left'], ['A', 'down', 'right']], 
    [['A', 'left'], ['A', 'left']], 
    [['A', 'left'], ['A', 'right']], 
    [['A', 'left'], ['B']], 
    [['A', 'left'], ['B', 'down']], 
    [['A', 'left'], ['B', 'down', 'left']], 
    [['A', 'left'], ['B', 'down', 'right']], 
    [['A', 'left'], ['B', 'left']], 
    [['A', 'left'], ['B', 'right']], 
    [['A', 'left'], ['NOOP']], 
    [['A', 'left'], ['down']], 
    [['A', 'left'], ['down', 'left']], 
    [['A', 'left'], ['down', 'right']], 
    [['A', 'left'], ['left']], 
    [['A', 'left'], ['right']], 
    [['A', 'right'], ['A']], 
    [['A', 'right'], ['A', 'B']], 
    [['A', 'right'], ['A', 'B', 'down']], 
    [['A', 'right'], ['A', 'B', 'down', 'left']], 
    [['A', 'right'], ['A', 'B', 'down', 'right']], 
    [['A', 'right'], ['A', 'B', 'left']], 
    [['A', 'right'], ['A', 'B', 'right']], 
    [['A', 'right'], ['A', 'down']], 
    [['A', 'right'], ['A', 'down', 'left']], 
    [['A', 'right'], ['A', 'down', 'right']], 
    [['A', 'right'], ['A', 'left']], 
    [['A', 'right'], ['A', 'right']], 
    [['A', 'right'], ['B']], 
    [['A', 'right'], ['B', 'down']], 
    [['A', 'right'], ['B', 'down', 'left']], 
    [['A', 'right'], ['B', 'down', 'right']], 
    [['A', 'right'], ['B', 'left']], 
    [['A', 'right'], ['B', 'right']], 
    [['A', 'right'], ['NOOP']], 
    [['A', 'right'], ['down']], 
    [['A', 'right'], ['down', 'left']], 
    [['A', 'right'], ['down', 'right']], 
    [['A', 'right'], ['left']], 
    [['A', 'right'], ['right']], 
    [['B'], ['A']], 
    [['B'], ['A', 'B']], 
    [['B'], ['A', 'B', 'down']], 
    [['B'], ['A', 'B', 'down', 'left']], 
    [['B'], ['A', 'B', 'down', 'right']], 
    [['B'], ['A', 'B', 'left']], 
    [['B'], ['A', 'B', 'right']], 
    [['B'], ['A', 'down']], 
    [['B'], ['A', 'down', 'left']], 
    [['B'], ['A', 'down', 'right']], 
    [['B'], ['A', 'left']], 
    [['B'], ['A', 'right']], 
    [['B'], ['B']], 
    [['B'], ['B', 'down']], 
    [['B'], ['B', 'down', 'left']], 
    [['B'], ['B', 'down', 'right']], 
    [['B'], ['B', 'left']], 
    [['B'], ['B', 'right']], 
    [['B'], ['NOOP']], 
    [['B'], ['down']], 
    [['B'], ['down', 'left']], 
    [['B'], ['down', 'right']], 
    [['B'], ['left']], 
    [['B'], ['right']], 
    [['B', 'down'], ['A']], 
    [['B', 'down'], ['A', 'B']], 
    [['B', 'down'], ['A', 'B', 'down']], 
    [['B', 'down'], ['A', 'B', 'down', 'left']], 
    [['B', 'down'], ['A', 'B', 'down', 'right']], 
    [['B', 'down'], ['A', 'B', 'left']], 
    [['B', 'down'], ['A', 'B', 'right']], 
    [['B', 'down'], ['A', 'down']], 
    [['B', 'down'], ['A', 'down', 'left']], 
    [['B', 'down'], ['A', 'down', 'right']], 
    [['B', 'down'], ['A', 'left']], 
    [['B', 'down'], ['A', 'right']], 
    [['B', 'down'], ['B']], 
    [['B', 'down'], ['B', 'down']], 
    [['B', 'down'], ['B', 'down', 'left']], 
    [['B', 'down'], ['B', 'down', 'right']], 
    [['B', 'down'], ['B', 'left']], 
    [['B', 'down'], ['B', 'right']], 
    [['B', 'down'], ['NOOP']], 
    [['B', 'down'], ['down']], 
    [['B', 'down'], ['down', 'left']], 
    [['B', 'down'], ['down', 'right']], 
    [['B', 'down'], ['left']], 
    [['B', 'down'], ['right']], 
    [['B', 'down', 'left'], ['A']], 
    [['B', 'down', 'left'], ['A', 'B']], 
    [['B', 'down', 'left'], ['A', 'B', 'down']], 
    [['B', 'down', 'left'], ['A', 'B', 'down', 'left']], 
    [['B', 'down', 'left'], ['A', 'B', 'down', 'right']], 
    [['B', 'down', 'left'], ['A', 'B', 'left']], 
    [['B', 'down', 'left'], ['A', 'B', 'right']], 
    [['B', 'down', 'left'], ['A', 'down']], 
    [['B', 'down', 'left'], ['A', 'down', 'left']], 
    [['B', 'down', 'left'], ['A', 'down', 'right']], 
    [['B', 'down', 'left'], ['A', 'left']], 
    [['B', 'down', 'left'], ['A', 'right']], 
    [['B', 'down', 'left'], ['B']], 
    [['B', 'down', 'left'], ['B', 'down']], 
    [['B', 'down', 'left'], ['B', 'down', 'left']], 
    [['B', 'down', 'left'], ['B', 'down', 'right']], 
    [['B', 'down', 'left'], ['B', 'left']], 
    [['B', 'down', 'left'], ['B', 'right']], 
    [['B', 'down', 'left'], ['NOOP']], 
    [['B', 'down', 'left'], ['down']], 
    [['B', 'down', 'left'], ['down', 'left']], 
    [['B', 'down', 'left'], ['down', 'right']], 
    [['B', 'down', 'left'], ['left']], 
    [['B', 'down', 'left'], ['right']], 
    [['B', 'down', 'right'], ['A']], 
    [['B', 'down', 'right'], ['A', 'B']], 
    [['B', 'down', 'right'], ['A', 'B', 'down']], 
    [['B', 'down', 'right'], ['A', 'B', 'down', 'left']], 
    [['B', 'down', 'right'], ['A', 'B', 'down', 'right']], 
    [['B', 'down', 'right'], ['A', 'B', 'left']], 
    [['B', 'down', 'right'], ['A', 'B', 'right']], 
    [['B', 'down', 'right'], ['A', 'down']], 
    [['B', 'down', 'right'], ['A', 'down', 'left']], 
    [['B', 'down', 'right'], ['A', 'down', 'right']], 
    [['B', 'down', 'right'], ['A', 'left']], 
    [['B', 'down', 'right'], ['A', 'right']], 
    [['B', 'down', 'right'], ['B']], 
    [['B', 'down', 'right'], ['B', 'down']], 
    [['B', 'down', 'right'], ['B', 'down', 'left']], 
    [['B', 'down', 'right'], ['B', 'down', 'right']], 
    [['B', 'down', 'right'], ['B', 'left']], 
    [['B', 'down', 'right'], ['B', 'right']], 
    [['B', 'down', 'right'], ['NOOP']], 
    [['B', 'down', 'right'], ['down']], 
    [['B', 'down', 'right'], ['down', 'left']], 
    [['B', 'down', 'right'], ['down', 'right']], 
    [['B', 'down', 'right'], ['left']], 
    [['B', 'down', 'right'], ['right']], 
    [['B', 'left'], ['A']], 
    [['B', 'left'], ['A', 'B']], 
    [['B', 'left'], ['A', 'B', 'down']], 
    [['B', 'left'], ['A', 'B', 'down', 'left']], 
    [['B', 'left'], ['A', 'B', 'down', 'right']], 
    [['B', 'left'], ['A', 'B', 'left']], 
    [['B', 'left'], ['A', 'B', 'right']], 
    [['B', 'left'], ['A', 'down']], 
    [['B', 'left'], ['A', 'down', 'left']], 
    [['B', 'left'], ['A', 'down', 'right']], 
    [['B', 'left'], ['A', 'left']], 
    [['B', 'left'], ['A', 'right']], 
    [['B', 'left'], ['B']], 
    [['B', 'left'], ['B', 'down']], 
    [['B', 'left'], ['B', 'down', 'left']], 
    [['B', 'left'], ['B', 'down', 'right']], 
    [['B', 'left'], ['B', 'left']], 
    [['B', 'left'], ['B', 'right']], 
    [['B', 'left'], ['NOOP']], 
    [['B', 'left'], ['down']], 
    [['B', 'left'], ['down', 'left']], 
    [['B', 'left'], ['down', 'right']], 
    [['B', 'left'], ['left']], 
    [['B', 'left'], ['right']], 
    [['B', 'right'], ['A']], 
    [['B', 'right'], ['A', 'B']], 
    [['B', 'right'], ['A', 'B', 'down']], 
    [['B', 'right'], ['A', 'B', 'down', 'left']], 
    [['B', 'right'], ['A', 'B', 'down', 'right']], 
    [['B', 'right'], ['A', 'B', 'left']], 
    [['B', 'right'], ['A', 'B', 'right']], 
    [['B', 'right'], ['A', 'down']], 
    [['B', 'right'], ['A', 'down', 'left']], 
    [['B', 'right'], ['A', 'down', 'right']], 
    [['B', 'right'], ['A', 'left']], 
    [['B', 'right'], ['A', 'right']], 
    [['B', 'right'], ['B']], 
    [['B', 'right'], ['B', 'down']], 
    [['B', 'right'], ['B', 'down', 'left']], 
    [['B', 'right'], ['B', 'down', 'right']], 
    [['B', 'right'], ['B', 'left']], 
    [['B', 'right'], ['B', 'right']], 
    [['B', 'right'], ['NOOP']], 
    [['B', 'right'], ['down']], 
    [['B', 'right'], ['down', 'left']], 
    [['B', 'right'], ['down', 'right']], 
    [['B', 'right'], ['left']], 
    [['B', 'right'], ['right']], 
    [['NOOP'], ['A']], 
    [['NOOP'], ['A', 'B']], 
    [['NOOP'], ['A', 'B', 'down']], 
    [['NOOP'], ['A', 'B', 'down', 'left']], 
    [['NOOP'], ['A', 'B', 'down', 'right']], 
    [['NOOP'], ['A', 'B', 'left']], 
    [['NOOP'], ['A', 'B', 'right']], 
    [['NOOP'], ['A', 'down']], 
    [['NOOP'], ['A', 'down', 'left']], 
    [['NOOP'], ['A', 'down', 'right']], 
    [['NOOP'], ['A', 'left']], 
    [['NOOP'], ['A', 'right']], 
    [['NOOP'], ['B']], 
    [['NOOP'], ['B', 'down']], 
    [['NOOP'], ['B', 'down', 'left']], 
    [['NOOP'], ['B', 'down', 'right']], 
    [['NOOP'], ['B', 'left']], 
    [['NOOP'], ['B', 'right']], 
    [['NOOP'], ['NOOP']], 
    [['NOOP'], ['down']], 
    [['NOOP'], ['down', 'left']], 
    [['NOOP'], ['down', 'right']], 
    [['NOOP'], ['left']], 
    [['NOOP'], ['right']], 
    [['down'], ['A']], 
    [['down'], ['A', 'B']], 
    [['down'], ['A', 'B', 'down']], 
    [['down'], ['A', 'B', 'down', 'left']], 
    [['down'], ['A', 'B', 'down', 'right']], 
    [['down'], ['A', 'B', 'left']], 
    [['down'], ['A', 'B', 'right']], 
    [['down'], ['A', 'down']], 
    [['down'], ['A', 'down', 'left']], 
    [['down'], ['A', 'down', 'right']], 
    [['down'], ['A', 'left']], 
    [['down'], ['A', 'right']], 
    [['down'], ['B']], 
    [['down'], ['B', 'down']], 
    [['down'], ['B', 'down', 'left']], 
    [['down'], ['B', 'down', 'right']], 
    [['down'], ['B', 'left']], 
    [['down'], ['B', 'right']], 
    [['down'], ['NOOP']], 
    [['down'], ['down']], 
    [['down'], ['down', 'left']], 
    [['down'], ['down', 'right']], 
    [['down'], ['left']], 
    [['down'], ['right']], 
    [['down', 'left'], ['A']], 
    [['down', 'left'], ['A', 'B']], 
    [['down', 'left'], ['A', 'B', 'down']], 
    [['down', 'left'], ['A', 'B', 'down', 'left']], 
    [['down', 'left'], ['A', 'B', 'down', 'right']], 
    [['down', 'left'], ['A', 'B', 'left']], 
    [['down', 'left'], ['A', 'B', 'right']], 
    [['down', 'left'], ['A', 'down']], 
    [['down', 'left'], ['A', 'down', 'left']], 
    [['down', 'left'], ['A', 'down', 'right']], 
    [['down', 'left'], ['A', 'left']], 
    [['down', 'left'], ['A', 'right']], 
    [['down', 'left'], ['B']], 
    [['down', 'left'], ['B', 'down']], 
    [['down', 'left'], ['B', 'down', 'left']], 
    [['down', 'left'], ['B', 'down', 'right']], 
    [['down', 'left'], ['B', 'left']], 
    [['down', 'left'], ['B', 'right']], 
    [['down', 'left'], ['NOOP']], 
    [['down', 'left'], ['down']], 
    [['down', 'left'], ['down', 'left']], 
    [['down', 'left'], ['down', 'right']], 
    [['down', 'left'], ['left']], 
    [['down', 'left'], ['right']], 
    [['down', 'right'], ['A']], 
    [['down', 'right'], ['A', 'B']], 
    [['down', 'right'], ['A', 'B', 'down']], 
    [['down', 'right'], ['A', 'B', 'down', 'left']], 
    [['down', 'right'], ['A', 'B', 'down', 'right']], 
    [['down', 'right'], ['A', 'B', 'left']], 
    [['down', 'right'], ['A', 'B', 'right']], 
    [['down', 'right'], ['A', 'down']], 
    [['down', 'right'], ['A', 'down', 'left']], 
    [['down', 'right'], ['A', 'down', 'right']], 
    [['down', 'right'], ['A', 'left']], 
    [['down', 'right'], ['A', 'right']], 
    [['down', 'right'], ['B']], 
    [['down', 'right'], ['B', 'down']], 
    [['down', 'right'], ['B', 'down', 'left']], 
    [['down', 'right'], ['B', 'down', 'right']], 
    [['down', 'right'], ['B', 'left']], 
    [['down', 'right'], ['B', 'right']], 
    [['down', 'right'], ['NOOP']], 
    [['down', 'right'], ['down']], 
    [['down', 'right'], ['down', 'left']], 
    [['down', 'right'], ['down', 'right']], 
    [['down', 'right'], ['left']], 
    [['down', 'right'], ['right']], 
    [['left'], ['A']], 
    [['left'], ['A', 'B']], 
    [['left'], ['A', 'B', 'down']], 
    [['left'], ['A', 'B', 'down', 'left']], 
    [['left'], ['A', 'B', 'down', 'right']], 
    [['left'], ['A', 'B', 'left']], 
    [['left'], ['A', 'B', 'right']], 
    [['left'], ['A', 'down']], 
    [['left'], ['A', 'down', 'left']], 
    [['left'], ['A', 'down', 'right']], 
    [['left'], ['A', 'left']], 
    [['left'], ['A', 'right']], 
    [['left'], ['B']], 
    [['left'], ['B', 'down']], 
    [['left'], ['B', 'down', 'left']], 
    [['left'], ['B', 'down', 'right']], 
    [['left'], ['B', 'left']], 
    [['left'], ['B', 'right']], 
    [['left'], ['NOOP']], 
    [['left'], ['down']], 
    [['left'], ['down', 'left']], 
    [['left'], ['down', 'right']], 
    [['left'], ['left']], 
    [['left'], ['right']], 
    [['right'], ['A']], 
    [['right'], ['A', 'B']], 
    [['right'], ['A', 'B', 'down']], 
    [['right'], ['A', 'B', 'down', 'left']], 
    [['right'], ['A', 'B', 'down', 'right']], 
    [['right'], ['A', 'B', 'left']], 
    [['right'], ['A', 'B', 'right']], 
    [['right'], ['A', 'down']], 
    [['right'], ['A', 'down', 'left']], 
    [['right'], ['A', 'down', 'right']], 
    [['right'], ['A', 'left']], 
    [['right'], ['A', 'right']], 
    [['right'], ['B']], 
    [['right'], ['B', 'down']], 
    [['right'], ['B', 'down', 'left']], 
    [['right'], ['B', 'down', 'right']], 
    [['right'], ['B', 'left']], 
    [['right'], ['B', 'right']], 
    [['right'], ['NOOP']], 
    [['right'], ['down']], 
    [['right'], ['down', 'left']], 
    [['right'], ['down', 'right']], 
    [['right'], ['left']], 
    [['right'], ['right']]
]

SUFFICIENT_ACTIONS = [
 [['A'], ['A', 'B', 'down', 'right']],
 [['A'], ['A', 'B', 'right']],
 [['A'], ['A', 'down', 'right']],
 [['A'], ['A', 'right']],
 [['A'], ['B', 'down', 'right']],
 [['A'], ['B', 'right']],
 [['A'], ['down', 'right']],
 [['A'], ['right']],
 [['A', 'B'], ['A', 'B', 'down', 'right']],
 [['A', 'B'], ['A', 'B', 'right']],
 [['A', 'B'], ['A', 'down', 'right']],
 [['A', 'B'], ['A', 'right']],
 [['A', 'B'], ['B', 'down', 'right']],
 [['A', 'B'], ['B', 'right']],
 [['A', 'B'], ['down', 'right']],
 [['A', 'B'], ['right']],
 [['A', 'B', 'down'], ['A', 'B', 'down', 'right']],
 [['A', 'B', 'down'], ['A', 'B', 'right']],
 [['A', 'B', 'down'], ['A', 'down', 'right']],
 [['A', 'B', 'down'], ['A', 'right']],
 [['A', 'B', 'down'], ['B', 'down', 'right']],
 [['A', 'B', 'down'], ['B', 'right']],
 [['A', 'B', 'down'], ['down', 'right']],
 [['A', 'B', 'down'], ['right']],
 [['A', 'B', 'down', 'right'], ['A']],
 [['A', 'B', 'down', 'right'], ['A', 'B']],
 [['A', 'B', 'down', 'right'], ['A', 'B', 'down']],
 [['A', 'B', 'down', 'right'], ['A', 'B', 'down', 'right']],
 [['A', 'B', 'down', 'right'], ['A', 'B', 'right']],
 [['A', 'B', 'down', 'right'], ['A', 'down']],
 [['A', 'B', 'down', 'right'], ['A', 'down', 'right']],
 [['A', 'B', 'down', 'right'], ['A', 'right']],
 [['A', 'B', 'down', 'right'], ['B']],
 [['A', 'B', 'down', 'right'], ['B', 'down']],
 [['A', 'B', 'down', 'right'], ['B', 'down', 'right']],
 [['A', 'B', 'down', 'right'], ['B', 'right']],
 [['A', 'B', 'down', 'right'], ['NOOP']],
 [['A', 'B', 'down', 'right'], ['down']],
 [['A', 'B', 'down', 'right'], ['down', 'right']],
 [['A', 'B', 'down', 'right'], ['right']],
 [['A', 'B', 'right'], ['A']],
 [['A', 'B', 'right'], ['A', 'B']],
 [['A', 'B', 'right'], ['A', 'B', 'down']],
 [['A', 'B', 'right'], ['A', 'B', 'down', 'right']],
 [['A', 'B', 'right'], ['A', 'B', 'right']],
 [['A', 'B', 'right'], ['A', 'down']],
 [['A', 'B', 'right'], ['A', 'down', 'right']],
 [['A', 'B', 'right'], ['A', 'right']],
 [['A', 'B', 'right'], ['B']],
 [['A', 'B', 'right'], ['B', 'down']],
 [['A', 'B', 'right'], ['B', 'down', 'right']],
 [['A', 'B', 'right'], ['B', 'right']],
 [['A', 'B', 'right'], ['NOOP']],
 [['A', 'B', 'right'], ['down']],
 [['A', 'B', 'right'], ['down', 'right']],
 [['A', 'B', 'right'], ['right']],
 [['A', 'down'], ['A', 'B', 'down', 'right']],
 [['A', 'down'], ['A', 'B', 'right']],
 [['A', 'down'], ['A', 'down', 'right']],
 [['A', 'down'], ['A', 'right']],
 [['A', 'down'], ['B', 'down', 'right']],
 [['A', 'down'], ['B', 'right']],
 [['A', 'down'], ['down', 'right']],
 [['A', 'down'], ['right']],
 [['A', 'down', 'right'], ['A']],
 [['A', 'down', 'right'], ['A', 'B']],
 [['A', 'down', 'right'], ['A', 'B', 'down']],
 [['A', 'down', 'right'], ['A', 'B', 'down', 'right']],
 [['A', 'down', 'right'], ['A', 'B', 'right']],
 [['A', 'down', 'right'], ['A', 'down']],
 [['A', 'down', 'right'], ['A', 'down', 'right']],
 [['A', 'down', 'right'], ['A', 'right']],
 [['A', 'down', 'right'], ['B']],
 [['A', 'down', 'right'], ['B', 'down']],
 [['A', 'down', 'right'], ['B', 'down', 'right']],
 [['A', 'down', 'right'], ['B', 'right']],
 [['A', 'down', 'right'], ['NOOP']],
 [['A', 'down', 'right'], ['down']],
 [['A', 'down', 'right'], ['down', 'right']],
 [['A', 'down', 'right'], ['right']],
 [['A', 'right'], ['A']],
 [['A', 'right'], ['A', 'B']],
 [['A', 'right'], ['A', 'B', 'down']],
 [['A', 'right'], ['A', 'B', 'down', 'right']],
 [['A', 'right'], ['A', 'B', 'right']],
 [['A', 'right'], ['A', 'down']],
 [['A', 'right'], ['A', 'down', 'right']],
 [['A', 'right'], ['A', 'right']],
 [['A', 'right'], ['B']],
 [['A', 'right'], ['B', 'down']],
 [['A', 'right'], ['B', 'down', 'right']],
 [['A', 'right'], ['B', 'right']],
 [['A', 'right'], ['NOOP']],
 [['A', 'right'], ['down']],
 [['A', 'right'], ['down', 'right']],
 [['A', 'right'], ['right']],
 [['B'], ['A', 'B', 'down', 'right']],
 [['B'], ['A', 'B', 'right']],
 [['B'], ['A', 'down', 'right']],
 [['B'], ['A', 'right']],
 [['B', 'down'], ['A', 'B', 'down', 'right']],
 [['B', 'down'], ['A', 'B', 'right']],
 [['B', 'down'], ['A', 'down', 'right']],
 [['B', 'down'], ['A', 'right']],
 [['B', 'down', 'right'], ['A']],
 [['B', 'down', 'right'], ['A', 'B']],
 [['B', 'down', 'right'], ['A', 'B', 'down']],
 [['B', 'down', 'right'], ['A', 'B', 'down', 'right']],
 [['B', 'down', 'right'], ['A', 'B', 'right']],
 [['B', 'down', 'right'], ['A', 'down']],
 [['B', 'down', 'right'], ['A', 'down', 'right']],
 [['B', 'down', 'right'], ['A', 'right']],
 [['B', 'right'], ['A']],
 [['B', 'right'], ['A', 'B']],
 [['B', 'right'], ['A', 'B', 'down']],
 [['B', 'right'], ['A', 'B', 'down', 'right']],
 [['B', 'right'], ['A', 'B', 'right']],
 [['B', 'right'], ['A', 'down']],
 [['B', 'right'], ['A', 'down', 'right']],
 [['B', 'right'], ['A', 'right']],
 [['NOOP'], ['A', 'B', 'down', 'right']],
 [['NOOP'], ['A', 'B', 'right']],
 [['NOOP'], ['A', 'down', 'right']],
 [['NOOP'], ['A', 'right']],
 [['down'], ['A', 'B', 'down', 'right']],
 [['down'], ['A', 'B', 'right']],
 [['down'], ['A', 'down', 'right']],
 [['down'], ['A', 'right']],
 [['down', 'right'], ['A']],
 [['down', 'right'], ['A', 'B']],
 [['down', 'right'], ['A', 'B', 'down']],
 [['down', 'right'], ['A', 'B', 'down', 'right']],
 [['down', 'right'], ['A', 'B', 'right']],
 [['down', 'right'], ['A', 'down']],
 [['down', 'right'], ['A', 'down', 'right']],
 [['down', 'right'], ['A', 'right']],
 [['right'], ['A']],
 [['right'], ['A', 'B']],
 [['right'], ['A', 'B', 'down']],
 [['right'], ['A', 'B', 'down', 'right']],
 [['right'], ['A', 'B', 'right']],
 [['right'], ['A', 'down']],
 [['right'], ['A', 'down', 'right']],
 [['right'], ['A', 'right']]]