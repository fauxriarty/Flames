import os
import time
name1= input("Enter your name: ")
name2= input("Enter the name of the person you want to check your flames determined relationship with: ")

print("Calculating...")
os.system('cls')
print(f"Your relationship with {name2} is: ", flames(name1,name2))
