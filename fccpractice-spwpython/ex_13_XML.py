#13 EX pfe - Using the xml

import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide = "yes"/>
</person>
'''

tree = ET.fromstring(data) #blows up if the string above has a mistake
print("Name: ", tree.find('name').text)
print("Attr: ", tree.find('email').get('hide'))

input = '''
<stuff> 
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>002</id>
            <name>Pat</name>
        </user>
    </users>
</stuff>
'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count:', len(lst))

for item in lst:
    print("Name", item.find('name').text)
    print("ID", item.find('id').text)
    print("x", item.get('x'))
