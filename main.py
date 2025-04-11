"""This program sets a time and message. It triggers a desktop notification once the goal time is reached.

Users will input a time and message. The time will be the goal time. And the message will pop up
once the desktop notification is triggered.
"""
import argparse
import datetime
import json

def check_time(s: str) -> datetime.datetime:
    """Checks if the user inputted time is correct"""
    try:
        return datetime.datetime.strptime(s, "%I:%M%p")
    except ValueError:
        raise argparse.ArgumentTypeError(f"not a valid time")

def set_reminder(title: str, time: datetime, message: str) -> None:
    """Sets the reminder values, time and message. And dumps it into JSON."""
    
    with open("reminder.json", mode="r", encoding="utf-8") as read_file:
        reminder = json.load(read_file)

    reminder_data = {
        "title": title,
        "time": time,
        "message": message
    }
    
    reminder.append(reminder_data)

    with open("reminder.json", mode="w", encoding="utf-8") as write_file:
        json.dump(reminder, write_file, indent=2)

def main() -> None:
    parser=argparse.ArgumentParser(description="sets up a timer")
    parser.add_argument("title")
    parser.add_argument("time", help="The goal time - format HH:MM AM/PM",type=check_time)
    parser.add_argument("message", help="Add quotation marks", nargs="?",default="")
    args=parser.parse_args()

    title = args.title
    time = args.time.strftime("%I:%M%p")
    message = args.message

    set_reminder(title, time, message)

if __name__ == "__main__":
    main()