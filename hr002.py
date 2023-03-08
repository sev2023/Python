# https://www.hackerrank.com/challenges/calendar-module/problem

import datetime
mm,dd,yy = map(int, input().split())
print(datetime.datetime(yy,mm,dd).strftime('%A').upper())
