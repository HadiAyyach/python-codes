time = '12:00 pm'
from typing import List
def convert_time(time: str) -> str:
    t = time.index(':')
    if time[-2:] == 'pm' :
        if int(time[:t]) == 12: result = '0' + time[t:t+3]
        else : result = str(int(time[:t])+12) + time[t:t+3]
    elif time[-2:] == 'am' :
        if int(time[:t]) == 12: result = '0'+ time[t:t+3]
        else:result = time[0:-2]
    elif int(time[:t]) >= 12 :
        if int(time[:t]) == 0: result = '12'+ time[t:t+3]
        else : result = str(int(time[:t])-12) + time[t:] + ' pm'
    else :
        if int(time[:t]) == 0: result = '12'+ time[t:t+3]
        else : result =  time + ' am'
    return result

print(convert_time(time))
