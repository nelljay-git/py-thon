from datetime import datetime, timedelta

today = datetime.now()
today_str = today.strftime("%B %d, %Y")

reah_birthday = datetime(today.year, 4, 15)
nell_birthday = datetime(today.year, 4, 18)

if today.day <= 5:
    monthsary = datetime(today.year, today.month, 5)
else:
    if today.month == 12:
        monthsary = datetime(today.year + 1, 1, 5)
    else:
        monthsary = datetime(today.year, today.month + 1, 5)

if today > reah_birthday:
    reah_birthday = datetime(today.year + 1, 4, 15)

if today > nell_birthday:
    nell_birthday = datetime(today.year + 1, 4, 18)

days_to_monthsary = (monthsary - today).days
days_to_reah_bday = (reah_birthday - today).days
days_to_nell_bday = (nell_birthday - today).days

print(f"\n📅 Today is {today_str}")
print("--------------------------------------------------")
print(f"💖 Days until your next Monthsary: {days_to_monthsary} day(s)")
if days_to_monthsary == 0:
    print("💌 Happy Monthsary, Nell & Reah! 🌸✨")

print(f"🎂 Days until Reah’s Birthday (April 15): {days_to_reah_bday} day(s)")
if days_to_reah_bday == 0:
    print("🎉 It’s Reah’s birthday! Make her feel extra loved! 💕")

print(f"🎉 Days until your Birthday (April 18): {days_to_nell_bday} day(s)")
if days_to_nell_bday == 0:
    print("🎂 Happy Birthday, Nell! You’re awesome 🥳")

print("--------------------------------------------------\n")
