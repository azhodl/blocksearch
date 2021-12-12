import collections
from datetime import datetime
from blocks import blocks_dict
from input import timeconv, child_name

#This is the primary file to execute. You need to have input.py and blocks.py for function calls.
#This will create a file wallet.txt as output.


#This block converts the normal timestaps in blocks_dictionary to unix based timestamps
#so that we can easily and accurately adjust for timezone variations in birth time.
dates = blocks_dict.keys()
heights = blocks_dict.values()
height_list = []
unix_list = []
def dict_conv():
    for i in dates:
        new_year = str(i)[0:4]
        new_year = int(new_year)
        new_month = str(i)[5:7]
        new_month = int(new_month)
        new_day = str(i)[8:10]
        new_day = int(new_day)
        new_hour = str(i)[11:13]
        new_hour = int(new_hour)
        new_minute = str(i)[14:16]
        new_minute = int(new_minute)
        new_date = datetime(new_year, new_month, new_day, new_hour,new_minute)
        unix_time = new_date.timestamp()
        values = int(unix_time)
        unix_list.append(values)
    for block_heights in heights:
        height_list.append(block_heights)
    time_stamp_dict = dict(zip(unix_list, height_list))
    return time_stamp_dict
time_stamp_dict = dict_conv()


#Here we import the organized user input information so that we can search the modified
#dictionary for the nearest matching keys.
time_dict = collections.OrderedDict()
birthdate = timeconv()
search_key = int(birthdate)

result_height = time_stamp_dict.get(search_key) or time_stamp_dict[
      min(time_stamp_dict.keys(), key = lambda key: abs(key-search_key))]
blockheight = str(result_height)


#Here we format the results and confirm the information is accurate before we print to file.
title = f"{child_name} Bitcoin Wallet"
body = f"Born at blockheight {blockheight}"

with open('Wallet.txt', 'a+') as external_file:
    add_text=f"{title}\n{body}"
    print(add_text, file=external_file)
    external_file.close()
