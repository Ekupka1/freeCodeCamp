#13 EX pfe - Using the json

import json 

data = '''
{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
} '''

info = json.loads(data)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])

input = '''
[
    { "name" : "Chuck",
      "id" : "009",
      "x" : "2"
    },
    { "name" : "Jay",
      "id" : "007",
      "x" : "1"
    }
]'''

about = json.loads(input)
print("User count: ", len(about))

for item in about:
    print("name:", item['name'])
    print("id:", item['id'])
    print("x:", item['x'])
