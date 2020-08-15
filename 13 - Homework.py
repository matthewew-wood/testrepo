import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input('Enter a url: ')

# sets a defult url if none is entered.
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_804745.xml'

# Read URL and set equal to a string
xml = urllib.request.urlopen(url).read()

stuff = ET.fromstring(xml)

# Create a list of comment objects
user_list = stuff.findall('comments/comment')

sum = 0

# Loop through list of comment objects finding and adding up the value in the count tag.
for item in user_list:
    sum = sum + float(item.find('count').text)

print(sum)