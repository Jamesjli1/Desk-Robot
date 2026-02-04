# Entry point: runs the main robot loop and shows the task menu

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
        print("4) Calculator")
        print("5) Memory")
        print("6) Exit")

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
            print("More coming soon!")

        elif choice == "7":
            print("Shutting down. Bye!")
            running = False

        else:
            print("❓ Invalid option. Please choose from the menu.")

if __name__ == "__main__":
    main()
