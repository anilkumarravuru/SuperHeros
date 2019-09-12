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
    character_height = visual_stats[1].findAll('td')[1].text.split('•')[0]
    character_weight = visual_stats[2].findAll('td')[1].text.split('•')[1]
    print('\tHeight: ', character_height)
    print('\tWeight: ', character_weight)
    powers = character_content.find_all('div', {'class': 'stat-holder'})[0].find_all('div', {'class': 'stat-value'})
    power_stats = [powers[i].get_text() for i in range(6)]
    print('\tIntelligence: ', power_stats[0])
    print('\tStrength: ', power_stats[1])
    print('\tSpeed: ', power_stats[2])
    print('\tDurability: ', power_stats[3])
    print('\tPower: ', power_stats[4])
    print('\tCombat: ', power_stats[5])
    return visual_stats

def initializePlayerObjectWithStats(player_object, test_bat_stats, odi_bat_stats, test_bowl_stats, odi_bowl_stats):
    # raise Player name not initialized exception here if player_object.name is empty
    player_object.test_matches = test_bat_stats[0]
    player_object.test_not_outs = test_bat_stats[2]
    player_object.test_runs = test_bat_stats[3]
    player_object.test_high_score = test_bat_stats[4]
    player_object.test_bat_avg = test_bat_stats[5]
    player_object.test_strike_rate = test_bat_stats[7]
    player_object.test_hundreds = test_bat_stats[8]
    player_object.test_fifties = test_bat_stats[9]
    player_object.test_sixes = test_bat_stats[11]
    player_object.test_fours = test_bat_stats[10]
    player_object.test_wickets = test_bowl_stats[4]
    player_object.test_economy = test_bowl_stats[8]
    player_object.test_bowl_avg = test_bowl_stats[7]
    player_object.test_bbw = test_bowl_stats[6]
    player_object.test_bbr = test_bowl_stats[6]
    player_object.test_catches = test_bat_stats[12]
    player_object.test_stumpings = test_bat_stats[13]

    player_object.odi_matches = odi_bat_stats[0]
    player_object.odi_not_outs = odi_bat_stats[2]
    player_object.odi_runs = odi_bat_stats[3]
    player_object.odi_high_score = odi_bat_stats[4]
    player_object.odi_bat_avg = odi_bat_stats[5]
    player_object.odi_strike_rate = odi_bat_stats[7]
    player_object.odi_hundreds = odi_bat_stats[8]
    player_object.odi_fifties = odi_bat_stats[9]
    player_object.odi_sixes = odi_bat_stats[11]
    player_object.odi_fours = odi_bat_stats[10]
    player_object.odi_wickets = odi_bowl_stats[4]
    player_object.odi_economy = odi_bowl_stats[8]
    player_object.odi_bowl_avg = odi_bowl_stats[7]
    player_object.odi_bbw = odi_bowl_stats[6]
    player_object.odi_bbr = odi_bowl_stats[6]
    player_object.odi_catches = odi_bat_stats[12]
    player_object.odi_stumpings = odi_bat_stats[13]


def dbConnection():
    config = {
    'mysql': {
        'driver': 'postgres',
        'host': 'localhost',
        'database': 'postgres',
        'user': 'anilkumar',
        'password': '',
        # 'log_queries': True
    }
    }
    db = DatabaseManager(config)
    user = db.table('details').first()
    print(user)
    # db.table('details').insert({'id': 3, 'name': 'Asra', 'last_name': 'Shaik'})
    # db.table('details').where({'id': 3}).update({'name': 'Asra', 'last_name': 'Md'})


def main():
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
            # player_object = player.Player(name=player_name)
            # initializePlayerObjectWithStats(player_object, test_bat_stats, odi_bat_stats, test_bowl_stats, odi_bowl_stats)
            # print(vars(player_object))


if __name__ == '__main__':
    main()
