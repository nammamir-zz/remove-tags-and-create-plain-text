# -*- coding: utf-8 -*-
import re

# This file contains HTML.
file = open('input-file.html', 'r')
temp = file.read()

# Replace Some Unicodes to ASCII.
temp = temp.replace ('&lsquo;',"""'""")
temp = temp.replace ('&rsquo;',"""'""")
temp = temp.replace ('&ldquo;',"""\"""")
temp = temp.replace ('&rdquo;',"""\"""")
temp = temp.replace ('&sbquo;',""",""")
temp = temp.replace ('&prime;',"""'""")
temp = temp.replace ('&Prime;',"""\"""")
temp = temp.replace ('&laquo;',"""«""")
temp = temp.replace ('&raquo;',"""»""")
temp = temp.replace ('&lsaquo;',"""‹""")
temp = temp.replace ('&rsaquo;',"""›""")
temp = temp.replace ('&amp;',"""&""")
temp = temp.replace ('&ndash;',""" – """)
temp = temp.replace ('&mdash;',""" — """)
temp = temp.replace ('&reg;',"""®""")
temp = temp.replace ('&copy;',"""©""")
temp = temp.replace ('&trade;',"""™""")
temp = temp.replace ('&para;',"""¶""")
temp = temp.replace ('&bull;',"""•""")
temp = temp.replace ('&middot;',"""·""")

# Replace HTML tags with an empty string.
result = re.sub("<.*?>", "", temp)
print(result)

# Write the result to a new file.
file = open("output-file.txt", "w")
file.write(result)
file.close()
