import datetime

# strftime('%Y.%m.%d. %H:%M:%S'))
def get_pub_date(hour = 0, days = 0):
    now_time = datetime.datetime.now()
    if hour != 0 :
        return (now_time + datetime.timedelta(hours=(-1) * hour)).strftime('%Y.%m.%d. %H:%M:%S')
    if days != 0 :
        return (now_time + datetime.timedelta(days=(-1) * days)).strftime('%Y.%m.%d. %H:%M:%S')

def make_pub_date(pub_date) :
    t = pub_date.split(".")
    return datetime.date(int(t[0]), int(t[1]), int(t[2])).strftime('%Y.%m.%d. %H:%M:%S')