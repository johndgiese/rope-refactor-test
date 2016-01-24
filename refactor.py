import rope.base.project
from rope.refactor.move import create_move

p = rope.base.project.Project('./exproject')

source = p.get_resource('./exproject/a.py')
dest = p.get_resource('./exproject/b.py')

m = create_move(p, source)

p.do(m.get_changes(dest))
