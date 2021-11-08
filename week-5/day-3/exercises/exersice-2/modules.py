import datetime
import time

def dis_curr_time():
    today = datetime.datetime.now()
    return today

print('time now: ',dis_curr_time())

#---------------------
def time_left(time_now):
    jan1 = datetime.datetime(2022,1,1)
    return  jan1 - time_now 

print(time_left(dis_curr_time()))

#-----------------------------
def minutes_alive():
    time_now = datetime.date.now()
    date_of_birth = datetime.date(1999,4,21)
    diff = time_now - date_of_birth
    print(diff)

minutes_alive()

#--------------------------
def today_date():
    today = datetime.datetime.now()
    return today

# def time_to_holiday(holiday_date):

