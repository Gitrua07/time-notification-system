import asyncio
import time
import datetime
import json

current_date = datetime.datetime.now()
current_time = current_date.time().strftime("%I:%M%p")

def check_time() -> str:
    with open("reminder.json", "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    
    for obj in data:
        if obj["time"] == current_time:
            return True
    
    return None

async def wait_timer():
    while True:
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(None, check_time)

        if result:
            print(result)
            break
        
        await asyncio.sleep(10)

async def main():
    await wait_timer()
    

if __name__ == "__main__":
    asyncio.run(main())