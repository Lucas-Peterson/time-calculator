import os
from datetime import datetime, timedelta


def welcome_message():
    print("========================================")
    print("   Welcome to the Time Calculator App!   ")
    print("========================================")
    print("You can add or subtract time easily.")
    print("Let's get started!")
    print()


welcome_message()


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


class TimeCalculator:
    def __init__(self, hours=0, minutes=0, seconds=0, period="AM"):
        self.current_time = datetime.now().replace(hour=hours, minute=minutes, second=seconds, microsecond=0)
        if period == "PM" and hours < 12:
            self.current_time += timedelta(hours=12)

    def modify_time(self, time_str, adding=True):
        try:
            value = float(time_str[:-1])
            if not adding:
                value = -value

            if time_str.endswith("h"):
                self.current_time += timedelta(hours=value)
            elif time_str.endswith("m"):
                self.current_time += timedelta(minutes=value)
            elif time_str.endswith("s"):
                self.current_time += timedelta(seconds=value)
            else:
                print("\nError: Invalid format. Use 'h' for hours, 'm' for minutes, or 's' for seconds.")
        except (ValueError, IndexError):
            print("\nError: Enter a valid number before 'h', 'm', or 's'.")

    def get_current_time(self):
        return self.current_time.strftime("%I:%M:%S %p")


def input_time():
    while True:
        hours_input = input("Enter hours (0-12) [default 00]: ")
        hours = int(hours_input) if hours_input != "" else 0
        if 0 <= hours <= 12:
            break
        else:
            print("Invalid input. Please enter a value between 0 and 12.")

    while True:
        minutes_input = input("Enter minutes (0-59) [default 00]: ")
        minutes = int(minutes_input) if minutes_input != "" else 0
        if 0 <= minutes < 60:
            break
        else:
            print("Invalid input. Please enter a value between 0 and 59.")

    while True:
        seconds_input = input("Enter seconds (0-59) [default 00]: ")
        seconds = int(seconds_input) if seconds_input != "" else 0
        if 0 <= seconds < 60:
            break
        else:
            print("Invalid input. Please enter a value between 0 and 59.")

    while True:
        period_input = input("Enter AM or PM [default AM]: ").upper() or "AM"
        if period_input in ["AM", "PM"]:
            break
        else:
            print("Invalid input. Please enter 'AM' or 'PM'.")

    return hours, minutes, seconds, period_input


def main():
    print("Let's set the start time by entering hours, minutes, and seconds separately.")
    hours, minutes, seconds, period = input_time()

    calculator = TimeCalculator(hours, minutes, seconds, period)

    while True:

        print(f"Current time: {calculator.get_current_time()}")
        print("\nChoose an action:")
        print("1. Add time")
        print("2. Subtract time")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, 3): ")

        if choice == '1':
            clear_screen()
            time_input = input(f"{calculator.get_current_time()} \nEnter time to add (e.g., '1.5h', '90m', '45s'): ")
            calculator.modify_time(time_input, adding=True)
            clear_screen()
        elif choice == '2':
            clear_screen()
            time_input = input(f"{calculator.get_current_time()} \nEnter time to subtract (e.g., '1.5h', '90m', '45s'): ")
            calculator.modify_time(time_input, adding=False)
            clear_screen()
        elif choice == '3':
            clear_screen()
            print("Exiting...")
            break
        else:
            clear_screen()
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
