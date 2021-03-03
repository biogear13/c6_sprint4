from time import sleep



def main ():
  x=0
  print(x)
  delay(seconds=2)

def delay(seconds):
    while x<5:
        print(f"Sleeping for {seconds} second(s)")
        sleep(seconds)
        x+=1
        print(x)

if __name__ == "__main__":
    main()
