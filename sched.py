import schedule
import time

def job():
    print("I am doing this job!")

time_str = '22:31'
schedule.every().monday.at(time_str).do(job)
schedule.every().tuesday.at(time_str).do(job)
schedule.every().wednesday.at(time_str).do(job)
schedule.every().thursday.at(time_str).do(job)
schedule.every().friday.at(time_str).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)