import json
import os
from datetime import date
import time
import sys
from plyer import notification

APP_DIR = os.path.expanduser("~/.time-tracker")
FILE_NAME = os.path.join(APP_DIR,"time-tracker.json")
MAX_DAYS = 3

def ensure_storage():
    """Ensure the storage folder and file exists"""
    if not os.path.exists(APP_DIR):
        os.makedirs(APP_DIR)
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME,"w") as f:
            json.dump([],f)

def load_data():
    ensure_storage()
    with open(FILE_NAME,"r") as f:
        return json.load(f)

def save_data(data):
   with open(FILE_NAME,"w") as f:
       json.dump(data,f,indent=4)

def add_entry(minutes,entry_date=None):
    if(entry_date is None):
        entry_date = str(date.today())

    data = load_data()

    # increment the time if already exists

    for entry in data:
        if entry["date"] == entry_date:
            entry["totalTime"]=str(int(entry["totalTime"])+minutes)
            break

    else:
        data.append({"date":entry_date,"totalTime":str(minutes)})
    
    # Keep only last MAX_DAYS
    data = sorted(data, key=lambda x: x["date"], reverse=True)[:MAX_DAYS]
    data = sorted(data, key=lambda x: x["date"])  # keep chronological order

    save_data(data)

def get_entry(entry_date=None):
    """Retrieve data for a specific date"""
    if entry_date is None:
        entry_date = str(date.today())
    data = load_data()
    for entry in data:
        if entry["date"]==entry_date:
            return entry
    return None        

def start_timer(minutes):
    """Start a timer for X minutes. Ctrl+C to stop early."""
    if not isinstance(minutes,int):
         print("❌ Only whole minutes are allowed. Please pass an integer.")
         return
    
    # if(minutes<2):
    #     print("Can not set timer for less than one min")
    #     return

    print(f"⏳ Timer started for {minutes} minutes. Press Ctrl+C to stop early")
    start_time = time.time()
    total_seconds = minutes*60

    try:
        for remaining in range(total_seconds,0,-1):
           mins,secs = divmod(remaining,60)
           timer_display = f"{mins:02d}:{secs:02d}"
           sys.stdout.write(f"\rTime left: {timer_display}") # overrite same line
           sys.stdout.flush()
           time.sleep(1) # wait for 1 sec 
           elapsed=minutes
        print("\n✅ Timer finished!")
        notification.notify(
    title="Timer Finished",
    message=f"⏳ Your {minutes}-minute timer is complete.",
    timeout=5  # seconds the notification stays visible
)

    except KeyboardInterrupt:
        elapsed_seconds = int(time.time() - start_time)
        elapsed = elapsed_seconds // 60  # convert to full minutes
        print(f"\n⏹ Stopped early at {elapsed} minutes.")
    
    if elapsed > 0:
       add_entry(elapsed)
       print(f"Elapsed: {elapsed} minutes")

def main():
    """Main CLI entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Focus Timer CLI - Track your productive time",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  focus 25              Start a 25-minute timer
  focus 60              Start a 60-minute timer
  focus --show          Show today's total time
  focus --show --date 2025-10-05
                        Show time for specific date
        """
    )
    
    parser.add_argument(
        'minutes', 
        type=int, 
        nargs='?',  # Makes it optional
        help='Number of minutes for the timer'
    )
    parser.add_argument(
        '--show', 
        action='store_true', 
        help='Show total time for a date'
    )
    parser.add_argument(
        '--date', 
        type=str, 
        help='Date for the entry (YYYY-MM-DD)', 
        default=None
    )
    
    args = parser.parse_args()
    
    # Show mode
    if args.show:
        entry = get_entry(args.date)
        if entry:
            print(f"📅 {entry['date']}: {entry['totalTime']} minutes")
        else:
            date_str = args.date or str(date.today())
            print(f"❌ No entry found for {date_str}")
        return
    
    # Timer mode - minutes is required here
    if args.minutes is None:
        parser.error("minutes argument is required when not using --show")
    
    start_timer(args.minutes)

if __name__ == "__main__":
    main()
