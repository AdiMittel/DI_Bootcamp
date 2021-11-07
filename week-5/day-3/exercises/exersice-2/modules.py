import datetime

def dis_curr_time():
    today = datetime.datetime.now()
    return today

print(dis_curr_time())

#---------------------
def time_left(today_date):
    jan1 = datetime.datetime(2022,1,1)
    return dis_curr_time() - jan1

print(time_left(dis_curr_time))