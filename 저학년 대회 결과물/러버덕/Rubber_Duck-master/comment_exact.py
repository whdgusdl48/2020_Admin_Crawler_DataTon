import json
from pprint import pprint

data_list = ['./data/Cyberpunk_2077.json',
             './data/Dota_2.json',
             "./data/PLAYERUNKNOWN'S_BATTLEGROUNDS.json",
             './data/Grand_Theft_Auto_V.json']

for data in data_list:
    with open(data) as json_file:
        f = open(data.replace('.json', '.txt'), 'w', encoding='UTF8')
        json_data = json.load(json_file)
        for user in json_data['reviews']:
            # print()
            f.write(str(json_data['reviews'][user]['review']) + '\n')
        f.close()
