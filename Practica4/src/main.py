import random

def main():
  for i in range(0,10):
    n = random.randint(2,1000)
    randomlist = random.sample(range(-1000, 1000), 10)
    print(randomlist)

if "__main__" == __name__:
  main()
