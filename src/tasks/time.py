from datetime import datetime

def time ():
    # Get the current time and date from datetime module
    time = datetime.now().strftime("%I:%M:%S %p")
    date = datetime.now().strftime("%A, %B %d, %Y")

    # Print the current time and date
    print("Current time:", time.lstrip("0"))
    print("Current date:", date)
    
