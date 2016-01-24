from a.b import c

c()

def tester():
    from a.b import x as xx
    xx()

tester()
