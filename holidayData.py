from gsheets import Sheets
import datetime
from datetime import timedelta

# Enter your google sheet id
sheet_id = ''
sheet = None


def init():
    global sheet, sheet_id
    sheets = Sheets.from_files('./google_api_client_keys/credentials.json')
    sheet = sheets[sheet_id]


def ordinal(num):
    suffix = {1: 'st', 2: 'nd', 3: 'rd', 31: 'st',
              21: 'st', 22: 'nd', 23: 'rd', 31: 'st'}
    if num in suffix.keys():
        return str(num) + suffix[num]

    return str(num) + 'th'


month_name = {1: 'Jan',
              2: 'Feb',
              3: 'Mar',
              4: 'Apr',
              5: 'May',
              6: 'Jun',
              7: 'Jul',
              8: 'Aug',
              9: 'Sep',
              10: 'Oct',
              11: 'Nov',
              12: 'Dec'}


day_name = {0: 'Monday',
            1: 'Tuesday',
            2: 'Wednesday',
            3: 'Thursday',
            4: 'Friday',
            5: 'Saturday',
            6: 'Sunday'}


def getData():
    global month_name
    global sheet

    companies = {}
    for ws in sheet:
        for row in range(1, ws.nrows):
            # Company
            company = ws.at(row, 1)
            # Location
            location = ws.at(row, 0).replace("/", "-")
            # date
            dt = ws.at(row, 2)

            date_arr = dt.split('/')
            date = datetime.date(int(date_arr[2]), int(
                date_arr[1]), int(date_arr[0]))
            holiday = {}
            holiday['date'] = date.day
            holiday['month'] = month_name[date.month]
            holiday['day'] = day_name[date.weekday()]
            holiday['event'] = ws.at(row, 3)

            wknd_arr = ['Monday', 'Friday']
            prev_day = date - timedelta(days=2)
            pprev_day = date - timedelta(days=1)
            nextday = date + timedelta(days=1)
            nnextday = date + timedelta(days=2)

            previous = ordinal(prev_day.day) + ' ' + month_name[prev_day.month] + ' ' + str(
                prev_day.year) + ' (' + day_name[prev_day.weekday()] + ')'
            pprevious = ordinal(pprev_day.day) + ' ' + month_name[pprev_day.month] + ' ' + str(
                pprev_day.year) + ' (' + day_name[pprev_day.weekday()] + ')'
            nextdy = ordinal(nextday.day) + ' ' + month_name[nextday.month] + ' ' + str(
                nextday.year) + ' (' + day_name[nextday.weekday()] + ')'
            nnextdy = ordinal(nnextday.day) + ' ' + month_name[nnextday.month] + ' ' + str(
                nnextday.year) + ' (' + day_name[nnextday.weekday()] + ')'

            if holiday['day'] in wknd_arr:
                if holiday['day'] == wknd_arr[0]:
                    holiday['longwknd'] = str(previous) + ' , ' + str(pprevious) + ' , ' + str(ordinal(
                        holiday['date'])) + ' ' + str(holiday['month']) + ' ' + str(nextday.year) + ' (' + str(holiday['day']) + ')'
                elif holiday['day'] == wknd_arr[1]:
                    holiday['longwknd'] = str(ordinal(holiday['date'])) + ' ' + str(holiday['month']) + ' ' + str(
                        nextday.year) + ' (' + str(holiday['day']) + ') , ' + str(nextdy) + ' , ' + str(nnextdy)
            else:
                holiday['longwknd'] = ''

            if company not in companies.keys():
                companies[company] = {}

            if location not in companies[company].keys():
                companies[company][location] = []

            companies[company][location].append(holiday)

    for c in companies.keys():
        for l in companies[c].keys():
            yield c, l, companies[c][l]
