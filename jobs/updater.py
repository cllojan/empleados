from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import delete_data

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(delete_data,'interval', seconds=5)
    scheduler.start()