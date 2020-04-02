curr_day,curr_month,curr_year=map(int,input().strip().split())
Due_day,Due_month,Due_year=map(int,input().strip().split())
if curr_year==Due_year:
    if curr_month==Due_month:
        if curr_day<=Due_day:
            fine=0
        else:
            fine=15*(curr_day-Due_day)
    else:
        if curr_month<Due_month:
            fine=0
        else:
            fine=500*(curr_month-Due_month)
else:
    if curr_year<Due_year:
        fine=0
    else:
        fine=10000
print(fine)
