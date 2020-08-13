# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:37:14 2020

@author: ETHEL YAYRA HEHETROR
"""

import time
from ctypes import windll, create_unicode_buffer
from datetime import datetime, timedelta

def return_active_window_title():
    
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    if buf.value:
        return buf.value
    else:
        return None

    print(return_active_window_title())
    
if __name__ == "__main__":
    print('CURRENT WINDOW NAME:   {}'.format(return_active_window_title()))
    print('')
    time.sleep(1)

return_active_window_title()


def user_input():
    # take the start date of the project
    # start time
    # take the end date of the project
    # end time
    
    from datetime import datetime, date
    
    # take the start date and time from the user and store it as a list
    # 0 index corresponds to year, 1 index --> month, 2 --> day, 3 --> hours, 4 --> minutes
    #datetime.now().strftime("%d/%m/%y - %H:%M:%S")
    time_now = datetime.now().strftime("%Y-%m-%d-%H-%M").split("-")
    end_date_time = [int(val.replace(" ", "")) for val in time_now]
    #start_date_time = [int(val.replace(" ", "")) for val in input("Enter start date in this formart yy,mm,dd,hrs,min : ").split(",")]
    start_date_time = [int(val.replace(" ", "")) for val in input("Enter start date in this formart yy,mm,dd,hrs,min : ").split(",")]
    
    start = start_date_time
    end = end_date_time
    
    start_to_datetime = datetime(start[0], start[1], start[2], start[3], start[4])
    end_to_datetime = datetime(end[0], end[1], end[2], end[3], end[4])
    
    #print(start_to_datetime.date())
    
    #with open("text.csv", "a") as file:
        #file.write(str(start_to_datetime.date()))
        #file.write("\n")
    
    return start_to_datetime, end_to_datetime, start_to_datetime.date(), start_to_datetime.time(), end_to_datetime.date(), end_to_datetime.time(),

    


# In[213]:


def handle_input_error():
    pass


# In[225]:


def compute_time():
    
    # assigns the return values of the function user_input to start_date_time and end_date_time
    
    #tart_date_time, end_date_time = user_input()
    
    start_date_time, end_date_time, start_date, start_time, end_date, end_time = user_input()
    
    # computes the difference between the start_date_time of the user and the end_date_time of the user
   
    time_diff = abs(start_date_time - end_date_time)
    
    # converts days to seconds by dividing by 86400 
    # the result is added to the remaining seconds and divided by 3600 to convert into hours
    
    #otal_hours = (time_diff.days * 86400 + time_diff.seconds)/ 3600
    #rint(total_hours)

    return float((time_diff.days * 86400 + time_diff.seconds)/ 3600),  start_date, start_time, end_date, end_time


# In[226]:


compute_time, start_date, start_time, end_date, end_time = compute_time()


# In[227]:


def compute_income():
    amount_per_hr = 5
    return int(compute_time * amount_per_hr)
    


# In[228]:


compute_income()


# In[229]:


def to_file():
#pass
    import pandas as pd

    start_date_lst = [start_date]
    start_date_time = [start_time]
    end_date_lst = [end_date]
    end_date_time = [end_time]
    hrs_spent = [compute_time]
    income_lst = [compute_income()]

    df = pd.DataFrame(list(zip(start_date_lst, start_date_time, end_date_lst, end_date_time, hrs_spent, income_lst)),
                  columns=["Start_date", "Start_time", "End_date", "End_time", "Hours_spent", "Income"])
    
    #print(df)
    
    df.to_csv('text.csv', sep='\t', header=True, mode='a')


# In[230]:

        
def get_activity():
    #print('Activity monitor')
    #time.sleep(1)
    #print('')
    #time.sleep(1)
    print("Start_date\tStart_time\tEnd_date\tEnd_time\tHours_spent\tIncome")
    time.sleep(1)
    print("{}\t{}\t{}\t{}\t{} hrs\t        ${}".format(start_date, start_time, end_date, end_time, int(compute_time), compute_income()))
        


def main():
    print('')
    print('')
    print("****** Time and salary tracking program *******\n")
    time.sleep(1)
    get_activity()
    


# In[231]:


main()
