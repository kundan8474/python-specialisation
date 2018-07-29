import random as r

# range function iterates from 0 to argument in range
# random generate a random number between 0.0 and 1.0 but excluding them
for i in range(5):
    print(r.random(),'\n')


# randint(min, max) will generate a random integer between min and max, including both
for i in range(5):
    print(r.randint(i,10))
