"""
if seconds passed
  compare and return english sentence of time

eg 
62 is 1 minute and 2 seconds
3662 is 1 hour, 1 minute and 2 seconds

"""

def solution(seconds):
    # constants
    min_1 = 60
    hour_1 = min_1 * 60
    day_1 = hour_1 * 24
    year_1 = day_1 * 365

    if not seconds or seconds==0:
        return "now"
    op_str = ""
    if seconds>= year_1:
        year = int(seconds/year_1)
        if year == 1:
           op_str+="1 year"
        else:
            op_str+=f"{year} years"
        seconds = seconds % year_1
    if seconds>= day_1:
        day = int(seconds/day_1)
        if op_str:
            op_str+=", "
        if day == 1:
           op_str+="1 day"
        else:
            op_str+=f"{day} days"
        seconds = seconds % day_1
    if seconds>= hour_1:
        hour = int(seconds/hour_1)
        if op_str:
            op_str+=", "
        if hour == 1:
           op_str+="1 hour"
        else:
            op_str+=f"{hour} hours"
        seconds = seconds % hour_1
    if seconds>= min_1:
        minute = int(seconds/min_1)
        if op_str:
            op_str+=", "
        if minute == 1:
           op_str+="1 minute"
        else:
            op_str+=f"{minute} minutes"
        seconds = seconds % min_1
    if seconds:
        if op_str:
            op_str+=" and "
        if seconds == 1:
           op_str+="1 second"
        else:
            op_str+=f"{seconds} seconds"
    return op_str
    
# case 1 : 0 then now
print(solution(0))

print(solution(62))

print(solution(3662))

print(solution(3660))

print(solution(15731080)) # 182 days, 1 hour, 44 minutes and 40 seconds

print(solution(31536000)) # 1 year

print(solution(31536001)) # 1 year and 1 second

print(solution(3601)) # 1 year and 1 second

print(solution(3600)) # 1 hour

print(solution(31536060))  # ❌ Gives: "1 year, 1 minute"


# right answer
def solution(seconds):
    # constants
    minute = 60
    hour = 60 * minute
    day = 24 * hour
    year = 365 * day

    if seconds == 0:
        return "now"

    units = []
    for unit_seconds, name in [
        (year, "year"),
        (day, "day"),
        (hour, "hour"),
        (minute, "minute"),
        (1, "second"),
    ]:
        count = seconds // unit_seconds
        if count:
            if count == 1:
                units.append(f"1 {name}")
            else:
                units.append(f"{count} {name}s")
            seconds %= unit_seconds

    if len(units) == 1:
        return units[0]
    elif len(units) == 2:
        return f"{units[0]} and {units[1]}"
    else:
        return f"{', '.join(units[:-1])} and {units[-1]}"
