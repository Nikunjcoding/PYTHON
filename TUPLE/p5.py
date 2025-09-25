#suppose a date is represented as a tupple (d,m,y).WAP to create two date tupple and finds the number of days between two dates.
# tpl=((1,8,2024),(8,8,2024))
# days=tpl[1][0]-tpl[0][0]
# print(f"The total number od days wetbeen two dates is={days}")


from datetime import date           #by chat gpt.

# create two date tuples
tpl1 = (1, 8, 2024)   # (day, month, year)
tpl2 = (1, 8, 2025)

# convert tuples into date objects
d1 = date(tpl1[2], tpl1[1], tpl1[0])  
d2 = date(tpl2[2], tpl2[1], tpl2[0])

# find difference in days
days = abs((d2 - d1).days)

print(f"The total number of days between two dates is = {days}")
