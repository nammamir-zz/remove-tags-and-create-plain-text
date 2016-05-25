import re
from HTMLParser import HTMLParser

# This file contains HTML.
file = open('input-file.html', 'r')
temp = file.read()

# Replace all XML/HTML characters to ASCII ones.
temp = HTMLParser.unescape.__func__(HTMLParser, temp)

# Replace HTML tags with an empty string.
result = re.sub("<.*?>", "", temp)

# Encode the text to UTF-8 for preventing some errors.
result = result.encode('utf-8')
print(result)

# Write the result to a new file.
file = open("output-file.txt", "w")
file.write(result)
file.close()
