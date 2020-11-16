# coding=utf-8
from pythonbot.python.plugins.discord_webhook import analyse_match_win_or_lose
from pythonbot.python.utils.TimeUtils import timeStamp
import json
import requests


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


def queryHistoryMatchData(playerId, mode):
    url = "https://api.opendota.com/api/players/{}/matches?game_mode={}".format(playerId, mode)
    r = requests.get(url)
    if r.ok:
        ak = list()
        result = json.loads(r.content.decode('utf-8'))
        for i in result:
            match_id = i['match_id']
            player_slot = i['player_slot']
            m, s = divmod(i['duration'], 60)
            durationTime = "%02d:%02d" % (m, s)
            start_time = timeStamp(i['start_time'])
            if i['radiant_win'] == True:
                radiant_win = 1
            else:
                radiant_win = 0
            if (analyse_match_win_or_lose(i) == True):
                is_win = 1
            else:
                is_win = 0
            game_mode = i['game_mode']
            duration = i['duration']
            lobby_type = i['lobby_type']
            hero_id = i['hero_id']
            start_timeStamp = i['start_time'] * 1000
            version = i['version']
            kills = i['kills']
            deaths = i['deaths']
            assists = i['assists']
            skill = i['skill']
            leaver_status = i['leaver_status']
            party_size = i['party_size']
            playerId = playerId

            temp = (
                match_id,
                player_slot,
                radiant_win,
                game_mode,
                duration,
                lobby_type,
                hero_id,
                start_time,
                version,
                kills,
                deaths,
                assists,
                skill,
                leaver_status,
                party_size,
                playerId,
                durationTime,
                is_win,
                start_timeStamp
            )
            ak.append(temp)
        return ak
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
