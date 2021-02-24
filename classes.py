class Particle(object):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def kill(self):
        print("killed")


part1 = Particle(1.0, 2.0, 3.0)
print(part1.x)
print(part1.y)
print(part1.z)

# particle objects need sensible values entered in for arguments
# but if a default is set in constructor, that opens up options.
part2 = Particle(x=5.0, y =2.0)
print(part2.x)
print(part2.y)
print(part2.z)
