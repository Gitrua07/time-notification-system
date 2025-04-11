"""This program is an event loop implemented using the asyncio library.

This program uses an event loop which is interrupted if it equals the current time to the
assigned JSON time.
"""

import asyncio
import time
import datetime
import json
from winotify import Notification, audio

def check_time() -> str:
    """This functin checks if the current time is equal to the goal time
        if it is, then it will stop the loop.
    """
    current_time = datetime.datetime.now().time().strftime("%I:%M%p")
    dump_data = []
    select_data = []
    result = None

    with open("reminder.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)


    for obj in data:
        if obj["time"] != current_time:
            dump_data.append(obj)
        else:
            select_data.append(obj)
            result = True

    if result == True:
        for reminder in select_data:
            toast = Notification(
                app_id = "Timer Notifier",
                title = reminder["title"],
                msg = reminder["message"],
                duration="long"
            )

            toast.set_audio(audio.Default, loop=False)
            toast.show()

    with open("reminder.json", "w", encoding="utf-8") as write_file:
        json.dump(dump_data, write_file, indent=2)
    
    return result

async def wait_timer():
    """This program loops until it meets the goal time"""
    while True:
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, check_time)

        if result:
            print("Found the number")
            break
        
        await asyncio.sleep(10)

async def main():
    await wait_timer()

if __name__ == "__main__":
    asyncio.run(main())