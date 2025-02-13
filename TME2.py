from datetime import datetime


date_input = input("Enter the date (mm/dd/yyyy): ")


input_format = "%m/%d/%Y"

output_format = "%B %d, %Y"

try:
    date_object = datetime.strptime(date_input, input_format)
  
    human_readable_date = date_object.strftime(output_format)
    print("Date Output:", human_readable_date)
except ValueError:
    print("Invalid date format. Please use mm/dd/yyyy.")