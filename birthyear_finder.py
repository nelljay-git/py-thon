from datetime import datetime

today = datetime.today()

format_date = today.strftime("%B %d, %Y")

print(format_date)