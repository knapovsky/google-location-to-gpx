import os
import datetime

# Generate the registration data
start = datetime.date(2010,1,1)

# initializing K
numdays = 365 * 2

base = datetime.datetime(2019, 7, 30)
date_list = [base - datetime.timedelta(days=x) for x in range(numdays)]
next_day = datetime.datetime.today()
for date in date_list:
    # python location_history_json_converter.py input output [-h] [-f {format, see below}]
    start = str(date.year) + '-' + str(date.month).rjust(2, "0") + "-" + str(date.day).rjust(2, "0")
    end = str(next_day.year) + '-' + str(next_day.month).rjust(2, "0") + "-" + str(next_day.day).rjust(2, "0")
    command = "python location_history_json_converter.py data.json " + start + ".gpx -s " + start + " -e " + end + " -f gpxtracks"
    print(command)
    os.system(command) 
    next_day = date