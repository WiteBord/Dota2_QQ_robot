# coding=utf-8

import json

import requests

from pythonbot.python.config import DataBaseConfig
from pythonbot.python.plugins.contents import PERSONID

from pythonbot.python.utils.SqlUtils import insert

playerIdList = PERSONID
testID = 442726378
game_mode = [1, 3, 22]


def insertMatchData(playerId):
    sql = 'INSERT INTO `dotaData`.`dota_match_list`(`match_id`, `player_slot`, `radiant_win`, `game_mode`, `duration`, `lobby_type`, `hero_id`, `start_time`, `version`, `kills`, `deaths`, `assists`, `skill`, `leaver_status`, `party_size`, `playerId`,`durationTime`,`is_win`,`start_timeStamp`,`playerId_matchId`) ' \
          'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)'
    a = []
    for i in game_mode:
        from pythonbot.python.utils.OfficialDataUtils import queryHistoryMatchData
        a += (queryHistoryMatchData(playerId, i))
    result = insert(sql, a)
    if (result == 1):
        print("{}比赛数据插入成功".format(playerId))
    else:
        print("{}比赛数据插入失败".format(playerId))


def insertDailyData():
    pass


if __name__ == '__main__':
    # insertMatchData(testID)

    # 2020.11.16
    for i in playerIdList:
        print("开始插入玩家%d的数据" % i)
        insertMatchData(i)
        print("玩家%d的数据插入结束" % i)
    DataBaseConfig.DataBaseConfig.server.close()

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
