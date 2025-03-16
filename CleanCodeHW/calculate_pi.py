import random

# Constant settings
RADIUS = 1
NUM_POINTS = 1000000
AREA_FACTOR = 4
SQUARE_EXPONENT = 2
POINT_COUNT_INCREMENT = 1

inside_circle_points = 0

# Randomly generate points and count those inside the circle
for _ in range(NUM_POINTS):
    x = random.uniform(-RADIUS, RADIUS)
    y = random.uniform(-RADIUS, RADIUS)
    if x**SQUARE_EXPONENT + y**2 <= RADIUS**SQUARE_EXPONENT:
        inside_circle_points += POINT_COUNT_INCREMENT

# Estimate pi based on the number of points inside the circle
PI_VALUE = (inside_circle_points / NUM_POINTS) * AREA_FACTOR

print(f"Estimated value of pi is: {PI_VALUE}")
