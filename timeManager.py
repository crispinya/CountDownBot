from datetime import datetime
from dateutil.relativedelta import relativedelta
import fileManager

UPDATED_COUNTDOWN_TXT = 'lastTimeUpdatedCountdown.txt'
LAST_REPLIED_TWEET_TXT = 'lastRepliedTweet.txt'

FINISH_DATE = '2021-05-03 17:03:05'


def get_last_replied_mention_time():
    return fileManager.getTimeFromFile(LAST_REPLIED_TWEET_TXT, '%Y-%m-%d %H:%M:%S')


def get_last_updated_countdown_time():
    return fileManager.getTimeFromFile(UPDATED_COUNTDOWN_TXT, '%Y-%m-%d %H:%M:%S.%f')


def set_reply_mention_time(reply_time):
    fileManager.writeInFile(LAST_REPLIED_TWEET_TXT, reply_time)


def set_update_countdown_time(update_time):
    fileManager.writeInFile(UPDATED_COUNTDOWN_TXT, update_time)


def setUnachievableDates():
    set_reply_mention_time("2070-01-01 11:11:11")
    set_update_countdown_time("2070-01-01 11:11:11.111000")


# difference between current time and the finish date
def calculateDifferenceCurrentDate_FinalDate():
    current_date = datetime.now()
    end_date = datetime.strptime(FINISH_DATE, '%Y-%m-%d %H:%M:%S')

    delta = end_date - current_date
    days = delta.days

    # we return two values, the relative delta (which includes months, days...
    # and the total days (instead of months, days)
    return relativedelta(end_date, current_date), days


# the countdown only updates itself it the las update was 8 hours or more ago
def checkLastUpdateTime():
    last_update_time = get_last_updated_countdown_time()
    time_now = datetime.now()
    diff = relativedelta(time_now, last_update_time)

    if diff.days > 1 or diff.hours > 8:
        set_update_countdown_time(str(time_now))
        return 0

    return -1
