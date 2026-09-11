# hello_universe.py
# Day 1: First Python script in the python-foundations repo

import datetime

def about_me():
    print("\nAbout Me:")
    print("1. I'm building the 111 cognitive engine.")
    print("2. I'm learning Python to power autonomous systems.")
    print("3. I live in Golden Valley, AZ.")

def main():
    name = "Sean"
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    location = "Golden Valley, AZ"
    mission = "Become a systems engineer and build autonomous resilience systems."

    print("Hello, Universe!")
    print(f"My name is {name}.")
    print(f"Today's date is {today}.")
    print(f"The current time is {current_time}.")
    print(f"I'm coding from {location}.")
    print("And I'm ready to rock.")
    print("This is the beginning of something huge.")
    print(f"My mission: {mission}")

    about_me()

if __name__ == "__main__":
    main()
