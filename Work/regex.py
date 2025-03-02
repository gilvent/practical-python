# Docs https://docs.python.org/library/re.html.
import re

text = 'Today is 3/27/2018. Tomorrow is 3/28/2018.'

# Find all occurences of dates
dates = re.findall(r'\d+/\d+/\d+', text)


# Replace occurences of dates with other format
text_with_formatted_date = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(text_with_formatted_date)

