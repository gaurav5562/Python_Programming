import json
with open("data_file.json", "w") as write_file:
    data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
                },
    "employee": {
        "name": "ravi",
        "gender": "male"
                },
    "Owner": {
        "name": "Vishal",
        "gender": "male"
                }
            }

    json.dump(data, write_file)#indent=? is optional where ? may be from 1 to ......
