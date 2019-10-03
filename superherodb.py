# AnilKumarRavuru

import character
import urllib.request
from bs4 import BeautifulSoup
from orator import DatabaseManager

superhero_character_filename = 'superhero_character_list.txt'
superhero_db_base_url = 'https://www.superherodb.com/'


def getProperStatFromString(stat_string):
    if stat_string == '' or stat_string == u'' or stat_string == u'-':
        return -1
    if '*' in stat_string or '/' in stat_string:
        return str(stat_string)
    return float(stat_string)


def getCharacterStats(superhero_url):
    # print(superhero_url)
    hdr = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) Chrome/23.0.1271.64 Safari/537.11'
    }
    superhero_request = urllib.request.Request(superhero_url, headers=hdr)
    try:
        character_content = BeautifulSoup(urllib.request.urlopen(superhero_request).read(), features='lxml')
    except Exception as e:
        print('Network Error...', e)
        return -1
    visual_stats = character_content.findAll('table')[2].findAll('tr')[1:]
    character_height = visual_stats[1].findAll('td')[1].text#.split('•')[0]
    character_weight = visual_stats[2].findAll('td')[1].text#.split('•')[1]
    powers = character_content.find_all('div', {'class': 'stat-holder'})[0].find_all('div', {'class': 'stat-value'})
    power_stats = [powers[i].get_text() for i in range(6)]
    return {
        'intelligence': int(power_stats[0]),
        'strength': power_stats[1],
        'speed': int(power_stats[2]),
        'durability': int(power_stats[3]),
        'power': int(power_stats[4]),
        'combat': int(power_stats[5]),
        'height': character_height,
        'weight': character_weight
    }


def dbConnection():
    config = {
        'mysql': {
            'driver': 'postgres',
            'host': 'localhost',
            'database': 'cards',
            'user': 'postgres',
            'password': 'postgres',
            # 'log_queries': True
        }
    }
    return DatabaseManager(config)


def main():
    db = dbConnection()
    with open(superhero_character_filename, 'r') as superheros:
        for line in superheros:
            line_split = line.split()
            character_url = line_split[-1]
            character_name = ' '.join(line_split[:-1])
            print(character_name)
            superhero_url = superhero_db_base_url + character_url
            character_stats = getCharacterStats(superhero_url)
            if character_stats == -1:
                return
            if db.table('characters').where({'name': character_name}).count() > 0:
                db.table('characters').where({'name': character_name}).update(character_stats)
            else:
                character_stats['name'] = character_name
                db.table('characters').insert(character_stats)


if __name__ == '__main__':
    main()
