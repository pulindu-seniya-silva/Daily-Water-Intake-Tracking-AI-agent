import datetime
import os

# File to store water intake records
DATA_FILE = "water_intake_log.txt"

def log_water_intake(amount_ml):
    """Log water intake amount (in milliliters) with timestamp."""
    with open(DATA_FILE, "a") as file:
        now = datetime.datetime.now()
        file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {amount_ml} ml\n")
    print(f"Logged {amount_ml} ml of water.")

def get_today_total():
    """Calculate total water intake for today."""
    if not os.path.exists(DATA_FILE):
        return 0
    total = 0
    today = datetime.datetime.now().date()
    with open(DATA_FILE, "r") as file:
        for line in file:
            date_str, amount_str = line.split(" - ")
            date_time = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
            if date_time.date() == today:
                amount = int(amount_str.replace(" ml\n", ""))
                total += amount
    return total

def main():
    print("Welcome to Daily Water Intake Tracker!")
    print("Enter the amount of water you drank in ml (e.g., 250), or 'q' to quit.")

    while True:
        user_input = input("Amount (ml): ").strip()
        if user_input.lower() == 'q':
            break
        if not user_input.isdigit():
            print("Please enter a valid number or 'q' to quit.")
            continue

        amount = int(user_input)
        log_water_intake(amount)
        total_today = get_today_total()
        print(f"Total water intake today: {total_today} ml\n")

    print("Stay hydrated! See you tomorrow.")

if __name__ == "__main__":
    main()
