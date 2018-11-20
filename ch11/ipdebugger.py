# d comes from a JSON payload we don't control
d = {'first': 'v1', 'second': 'v2', 'fourth': 'v4'}
# keys also comes from a JSON payload we don't control
keys = ('first', 'second', 'third', 'fourth')

def do_something_with_value(value):
    print(value)

from IPython.core.debugger import Pdb
ipdb = Pdb()
ipdb.set_trace()  # we place a breakpoint her

for key in keys:
    do_something_with_value(d[key])

print('Validation done.')
