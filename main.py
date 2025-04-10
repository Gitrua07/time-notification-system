"""This program sets a time and message. It triggers a desktop notification once the goal time is reached.

Users will input a time and message. The time will be the goal time. And the message will pop up
once the desktop notification is triggered.
"""

import argparse
import datetime

def set_reminder():
    """Sets the reminder values, time and message."""

def set_message():
    """Sets up the message string value."""

def set_time():
    """Sets the goal time for the notification."""

def get_time():
    """Gets the time that the notification will be triggered on."""

def get_message():
    """Gets the message for a specific goal time."""

def get_reminder():
    """Gets the message and time that a time will trigger."""

def main():
    parser=argparse.ArgumentParser(description="sets up a timer")
    parser.add_argument("time", type=float) #Fix this so it takes in time type
    parser.add_argument("message", nargs="?",default="")
    args=parser.parse_args()

if __name__ == "__main__":
    main()