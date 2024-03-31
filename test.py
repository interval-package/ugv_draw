import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Create a rotated rectangle
rectangle = Rectangle((1, 1), 4, 2, angle=45)

# Get the path of the rectangle
path = rectangle.get_path()

# Extract the vertices and rotation angle
vertices = path.vertices
angle = rectangle.angle

# Print the vertices and rotation angle
for vertex in vertices:
    print("Corner:", vertex)

print("Rotation angle:", angle)