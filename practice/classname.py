class shapes:
    def __init__(self,x):
        self.x = x
    def cube(self,cube):
        return cube*cube*cube

s=shapes(10)
print(s.cube(2))

print(s.__class__.__name__)
