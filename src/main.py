# Main: runs the main robot loop and coordinates input, logic, and output 
def main():
    print("Hi, I'm your desk robot!")
    print("Type off to shut me down.\n")

    powered_on = True

    while powered_on:
        user_input = input("> ").strip().lower()

        if user_input == "off":
            print("Shutting down... goodbye!")
            powered_on = False
        else:
            print("I'm on!")

if __name__ == "__main__":
    main()
