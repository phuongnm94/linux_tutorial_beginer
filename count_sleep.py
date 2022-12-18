
import time
if __name__=="__main__":
    print("This program will run in about 15 minutes.")
    for i in range (1, 1000):
        time.sleep(1) 
        print(i)
    print("Finished")
