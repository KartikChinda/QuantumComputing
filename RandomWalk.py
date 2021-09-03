import random


def random_walk(n):
    # Here n is used to return the coordinates after any n random walks.
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        # dx and dy represent the change in the difference, say for each decision, x or y gets incremented or decremented by 1 unit.
        x += dx
        y += dy
    return (x, y)

# now, say that we have to calculate, what is the probability that the walk you do results in you being less than 4 units from your origin. That means, since you can either be farther than 4 units or closer than it, there is a 50% chance for the same to happen. So we need to see which value is the highest for a probability higher than 50%.


number_of_walks = 10000
for walk_length in range(1, 31):
    less_than_4 = 0
    for i in range(number_of_walks):
        (x, y) = random_walk(walk_length)
        distance = abs(x) + abs(y)
        if distance <= 4:
            less_than_4 += 1
    less_than_4_percentage = float(less_than_4)/number_of_walks
    print("Walk size =  ", walk_length,
          " and the % of the size being less than 4 is ", 100*less_than_4_percentage)
