import schedule
import pymysql
import time
from datetime import datetime
from core import job


if __name__ == '__main__':
    print(f"现在是{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, 开始执行定时任务...")
    schedule.every().day.at("18:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
