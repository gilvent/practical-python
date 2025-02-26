# bounce.py
#
# Exercise 1.5

height = 100
next_bounce_multiplier = 3 / 5
bounce_count = 1

while (bounce_count <= 10):
    height = height * next_bounce_multiplier
    print(bounce_count, round(height, 4))
    bounce_count = bounce_count + 1