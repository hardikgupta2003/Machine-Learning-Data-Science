# datetime module

from datetime import datetime
current_datetime=datetime.now()
# Format a datetime object as a string
formatted_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)

# Parse a string into a datetime object
parsed_date = datetime.strptime("2023-01-01 12:30:00", "%Y-%m-%d %H:%M:%S")
print(parsed_date)