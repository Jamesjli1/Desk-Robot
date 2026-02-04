# Entry point: runs the main robot loop and shows the task menu

# Import task modules
from tasks.timer import timer
from tasks.time import time
from tasks.music import music
from tasks.jokes import jokes
from tasks.weather import weather
import tasks.speeches  # farting

def main():
    print("Hi, I'm your desk robot!")
    print("TURN ME ON MOMMY")

    running = True

    while running:
        print("\nChoose a task:")
        print("----------------")
        print("1) Timer")
        print("2) Time")
        print("3) Music")
        print("4) Jokes")
        print("5) Weather")
        print("6) Speeches")
        print("7) coming soon!")
        print("8) Exit")

        choice = input("").strip()

        if choice == "1":
            print("Timer selected (not implemented yet).")

        elif choice == "2":
            print("Time selected (not implemented yet).")

        elif choice == "3":
            print("Music selected (not implemented yet).")

        elif choice == "4":
            print("Jokes selected (not implemented yet).")

        elif choice == "5":
            print("Weather selected (not implemented yet).")

        elif choice == "6":
            print("fart")

        elif choice == "7":
            print("More coming soon!")
        
        elif choice == "8":
            print("Shutting down. Bye!")
            running = False

        elif choice == "67":
            print("SIXSEVENNNNNNNN Twerk for me")

        else:
            print("Invalid option. Please choose from the menu.")

if __name__ == "__main__":
    main()
