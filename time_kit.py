import datetime
#  input format : YYYY.MM.DD.
# output format : ('%Y.%m.%d. %H:%M:%S')
def get_pub_date(minute = 0, hour = 0, days = 0):
    now_time = datetime.datetime.now()
    if minute != 0 :
        return str((now_time + datetime.timedelta(minutes=(-1) * int(minute))).strftime('%Y.%m.%d. %H:%M:%S'))
    if hour != 0 :
        return str((now_time + datetime.timedelta(hours=(-1) * int(hour))).strftime('%Y.%m.%d. %H:%M:%S'))
    if days != 0 :
        return str((now_time + datetime.timedelta(days=(-1) * int(days))).strftime('%Y.%m.%d. %H:%M:%S'))

def make_pub_date(pub_date) :
    t = pub_date.split(".")
    return str(datetime.date(int(t[0]), int(t[1]), int(t[2])).strftime('%Y.%m.%d. %H:%M:%S'))

def get_days_distance(start_day, end_day):
    end_day = [int(t) for t in end_day.split(".")]
    start_day = [int(t) for t in start_day.split(".")]

    end_datetime = datetime.datetime(end_day[0], end_day[1], end_day[2])
    start_datetime = datetime.datetime(start_day[0], start_day[1], start_day[2])

    duration_time = end_datetime - start_datetime
    return duration_time.days

def get_crawling_date(start_day, duration_day) :
    # start_day format : '2020.09.26'
    start_day = [int(t) for t in start_day.split(".")]
    start_datetime = datetime.datetime(start_day[0], start_day[1], start_day[2])

    crawling_day = start_datetime + datetime.timedelta(days = duration_day)
    return crawling_day.strftime("%Y.%m.%d")

if __name__ == "__main__" :
    print(get_crawling_date("2020.09.26", 4))