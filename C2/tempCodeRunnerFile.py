
point2 = Point()

point1.reset()
point2.move(5, 0)

print(point2.calculate_distance(point1))
assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))

point1.move(5, 1)
print(point1.calculate_distance(point2))
print(point2.calculate_distance(point1))