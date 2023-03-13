import sys
import time
import os

def AnimPayment():
    print("Payment process ")
    time.sleep(0.4)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process .")
    time.sleep(0.4)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process ..")
    time.sleep(0.4)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process ...")
    time.sleep(0.4)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process .. ")
    time.sleep(0.4)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process .  ")
    time.sleep(0.5)
    sys.stdout.write("\033[F")  # Move cursor up one line
    print("Payment process    ")
    time.sleep(0.5)
    print("Success !")
    time.sleep(0.5)


def AnimCheck(hasAccount):
    print("Checking if the user is in the system : ")
    sys.stdout.write("\033[F")  # Move cursor up one line
    time.sleep(0.5) # Delay process only 0.5 second
    print("Checking if the user is in the system : ", hasAccount)
    time.sleep(0.8)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_prev_lines():
    sys.stdout.write("\033[F")  # Move cursor up one line
    sys.stdout.write("\033[K")  # Clear the line