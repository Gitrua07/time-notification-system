# time-notification-system

## Description
A program that allows users to set a timer. Asks users for 2-3 arguments (title, time, message)
The program will trigger a computer notification when the goal time is reached.
Utilizes the libraries: argparse, asyncio, winotify (notifications, audio), JSON.

Uses the JSON files to store the timer information while the timer goal has not been met. 
the library asyncio is used to create an background event loop which checks if the time has been met yet.
And eventually notifies the user using winotify. Uses the command line for user input. When entering the
program in Windows 10/11, it will be formatted like: ./timer.bat <title> <goal_time> <optional_message>

### main.py

Where all the main functionality resides. It sets the reminder based on the user input. Uses argparse
for CLI. 

### background_loop.py

Implements the background loop using asyncio. Checks every 10 seconds if the time condition has been met.

### reminder.json

This list is where all the reminder data is stored. Will be dumped when the time goal has been reached. 

### timer.bat

Executes whole program.

