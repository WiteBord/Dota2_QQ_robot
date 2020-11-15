# coding=utf-8

import json
import pandas as pd
import requests
from numpy import nan

from pythonbot.python.plugins.contents import PERSONID

playerIdList = PERSONID
testID = 442726378
game_mode = [1, 3, 22]


def queryHistoryMatchData(playerId, mode):
    url = "https://api.opendota.com/api/players/{}/matches?game_mode={}".format(playerId, mode)
    r = requests.get(url)
    if r.ok:
        result = json.loads(r.content.decode('utf-8'))

        return result
    else:
        print('get uid: {} matches fail, status code: {}'.format(playerId, r.status_code))


def matchDetails(matchid):
    url = 'https://api.opendota.com/api/matches/{}'.format(matchid)
    r = requests.get(url)
    if r.ok:
        result = json.loads(r.content.decode('utf-8'))

        return result.get("players")
    else:
        print('get match: {} matches fail, status code: {}'.format(matchid, r.status_code))


def insertMatchData(matchData):
    sql='INSERT INTO `dotaData`.`dota_match_list`(`match_id`, `player_slot`, `radiant_win`, `game_mode`, `duration`, `lobby_type`, `hero_id`, `start_time`, `version`, `kills`, `deaths`, `assists`, `skill`, `leaver_status`, `party_size`, `playerId`) ' \
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    pass


def insertDailyData():
    pass


def getPlayerName(playerId):
    if playerId != playerId:
        return None
    else:
        playerId = int(playerId)
    url = 'https://api.opendota.com/api/players/{}'.format(playerId)
    r = requests.get(url)
    if r.ok:
        result = json.loads(r.content.decode('utf-8'))
        return result.get("profile").get("personaname")
    else:
        return None


if __name__ == '__main__':
    a=[]
    for i in game_mode:
        a+=(queryHistoryMatchData(testID,i))
    print(a[0])


    # players = matchDetails(5698007640)[0].keys()
    # purchase = matchDetails(5698007640)[0].get("purchase")
    #
    # details = pd.DataFrame(matchDetails(5698007640))
    # drop_list = ["match_id",
    #              "account_id",
    #              "firstblood_claimed",
    #              'gold',
    #              "gold_per_min",
    #              "hero_damage",
    #              "hero_healing",
    #              "party_size",
    #              "stuns",
    #              "tower_damage",
    #              "towers_killed",
    #              "start_time",
    #              "game_mode",
    #              "total_gold",
    #              "total_xp",
    #              "kills_per_min",
    #              "neutral_kills",
    #              "tower_kills",
    #              "courier_kills",
    #              "lane_kills",
    #              "hero_kills",
    #              "observer_kills",
    #              "sentry_kills",
    #              "roshan_kills",
    #              "necronomicon_kills",
    #              "ancient_kills",
    #              "actions_per_min",
    #              "is_roaming"
    #              ]
    # # 删除包含NaN值得任何行
    # details["player"] = details.apply(lambda x: getPlayerName(x['account_id']), axis=i)
    #
    # a = details[drop_list]

    # print(a["actions_per_min"])
    # matchCount = []
    # for i in playerIdList:
    #     matchCount.append([[i[i],len(queryHistoryMatchData(i[0]))]])
    #     print(str(i[i])+'竞技场数:'+str(len(queryHistoryMatchData(i[0]))))
