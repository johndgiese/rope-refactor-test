import rope.base.project
from rope.refactor.move import create_move

p = rope.base.project.Project('/Users/david/Desktop/ropetest/exproject')

source = p.get_resource('a/b.py')
dest = p.get_resource('.')

m = create_move(p, source)

p.do(m.get_changes(dest))
p.close()
