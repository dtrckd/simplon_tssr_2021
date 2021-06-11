import requests
import re

# Fetch the data
r = requests.get('https://www.wikipedia.org')
content = r.text

# Replace all the link in the html of the downloaded page
new_content = re.sub(r"href=\"[^\"]*\"", 'href="http://www.perdu.com"', content)

# Write the results in the file "file.html"
with open("file.html", "w") as f:
    f.write(new_content)

