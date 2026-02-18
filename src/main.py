# Entry point: runs the main robot loop and shows the task menu

# Import task modules
from tasks.timer import NormalTimer # not used
from tasks.time import time
from tasks.music import music
from tasks.jokes import jokes # not used
from tasks.weather import weather
import tasks.speeches # not used

def main():
    print("Hi, I'm your desk robot!")
    print("TURN ME ON MOMMY")

    running = True

    while running:
        print("\nChoose a task:")
        print("----------------")
        print("1) Timer")
        print("2) Time")
        print("3) Weather")
        print("4) Music")
        print("5) Jokes")
        print("6) Speeches")
        print("7) coming soon!")
        print("8) Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            print("Timer selected (not implemented yet).")

        elif choice == "2":
            time()

        elif choice == "3":
            weather()

        elif choice == "4":
            music()

        elif choice == "5":
            print("Jokes selected (not implemented yet).")

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
