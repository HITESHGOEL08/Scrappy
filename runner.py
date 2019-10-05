import datetime
from datetime import date
import json
import selenium
from main4 import avis,ace,thrifty
loc = "HNL"
lst = []
today = date.today()
today = today.strftime("%m/%d/%Y")
date_1 = datetime.datetime.strptime(today, "%m/%d/%Y")
end_date = date_1 + datetime.timedelta(days=1)
end_date1 = end_date.strftime("%m/%d/%Y")
print(today, end_date1)


date_7 = datetime.datetime.strptime(today, "%m/%d/%Y")
end_date = date_1 + datetime.timedelta(days=7)
end_date7 = end_date.strftime("%m/%d/%Y")
print(today, end_date7)

date_14 = datetime.datetime.strptime(today, "%m/%d/%Y")
end_date = date_1 + datetime.timedelta(days=14)
end_date14 = end_date.strftime("%m/%d/%Y")
print(today, end_date14)

date_30 = datetime.datetime.strptime(today, "%m/%d/%Y")
end_date = date_1 + datetime.timedelta(days=30)
end_date30 = end_date.strftime("%m/%d/%Y")
print(today, end_date30)


avi = {}
avi['1-day'] = ace(loc, today, end_date1)
print(avi)
# avi['7-day'] = avis(loc, today, end_date7)
# avi['14-day'] = avis(loc, today, end_date14)
# avi['30-day'] = avis(loc, today, end_date30)
# td = date.today()
# file_name = td.strftime("%m-%d-%Y")
# with open('data'+file_name+'.txt', 'a+') as outfile:
#     json.dump(avi, outfile)


# from main import expedia
# expedi = {}
# expedi['1-day'] = expedia('HNL',today,end_date1)
# expedi['7-day'] = expedia('HNL',today,end_date7)
# expedi['14-day'] = expedia('HNL',today,end_date14)
# expedi['30-day'] = expedia('HNL',today,end_date30)

# with open('data'+file_name+'.txt', 'a+') as outfile:
#     json.dump(expedi, outfile)
