def add_time(start, duration, day=''):
    time = start.split()
    hour, minute = map(int, time[0].split(':'))
    hour1, minute1 = map(int, duration.split(':'))
    

    if time[1] == "PM":
        hour += 12

    sum_minute = minute + minute1
    extra_hour = sum_minute // 60
    sum_minute %= 60

    total_hours = hour + hour1 + extra_hour
    days_passed = total_hours // 24
    final_hour = total_hours % 24


    period = "AM" if final_hour < 12 else "PM"
    final_hour %= 12
    if final_hour == 0:
        final_hour = 12

    new_time = f"{final_hour}:{sum_minute:02d} {period}"
    
    if day:
        day = get_weekday(day, days_passed)
        new_time += f', {day}'

    if days_passed == 1:
        new_time += " (next day)"
    elif days_passed > 1:
        new_time += f" ({days_passed} days later)"

    return new_time

def get_weekday(start_day, days_later):
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    start_index = week.index(start_day.capitalize())
    return week[(start_index + days_later) % 7]
