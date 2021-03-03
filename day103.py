import random
from time import sleep

def get_random_number():
    return random.randint(1,5)

def delay(seconds):
    for x in range(5):
        print(x)
        print(f"Sleeping for {seconds} second(s)")
        sleep(seconds)


def main ():
   delay(get_random_number())

if __name__ == "__main__":
    main()
