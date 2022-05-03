# Initialize Point Class
class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()

Point.reset(p)

# p.reset()

print(p.x, p.y)

# Instances of Class Point
p1 = Point()
p2 = Point()

# Add attributes to instance
p1.x = 5
p1.y = 10

p2.x = 10
p2.y = 20

print(p1.x, p1.y)
print(p2.x, p2.y)