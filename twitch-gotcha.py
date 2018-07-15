#!/usr/bin/env python3
# VAS ZAMETILI Kappa
# Catches twitch users visiting your twitch channel and notifying you via Telegram.

import json
import time
import requests
import arrow
import cfg

def get_chatters():
    r = requests.get(cfg.CHATTERS_URL)
    js = json.loads(r.text)
    chat_lst = js['chatters']['moderators'] + js['chatters']['viewers']
    return chat_lst


def notify_login(tlg_id, tw_chan, usr):
    url = 'https://api.telegram.org/bot%s/' % cfg.TKN_TLG  # Telegram API URL
    text = '<a href="http://twitch.tv/%s">%s</a> зашел(ла) на канал к ' \
           '<a href="http://twitch.tv/%s">%s</a>' % (usr, usr, tw_chan, tw_chan)
    data = {'chat_id': tlg_id, 'text': text, 'parse_mode': 'HTML', 'disable_web_page_preview': True}
    try:
        r = requests.post(url + 'sendMessage', data=data)
    except Exception as error:
        print('Something went wrong...')
        print(str(error))
    else:
        print(r.text)
        return r


def notify_logoff(tlg_id, tw_chan, usr, time):
    url = 'https://api.telegram.org/bot%s/' % cfg.TKN_TLG  # Telegram API URL
    diff = arrow.get(time)
    time_watched = diff.humanize(locale='ru_RU', only_distance=True)
    text = '<a href="http://twitch.tv/%s">%s</a> покинул(а) канал ' \
           '<a href="http://twitch.tv/%s">%s</a> и смотрел(а) его %s' % (usr, usr, tw_chan, tw_chan, time_watched)
    data = {'chat_id': tlg_id, 'text': text, 'parse_mode': 'HTML', 'disable_web_page_preview': True,
            'disable_notification': True}
    try:
        r = requests.post(url + 'sendMessage', data=data)
    except Exception as error:
        print('Something went wrong...')
        print(str(error))
    else:
        print(r.text)
        return r


def loop_check():
    not_first_run = False
    while True:
        chatters = get_chatters()
        catch = set(chatters).intersection(cfg.usr_lst)
        for s in catch:
            if s in usr_watching and s in catch:
                print('exists in both usr_watching and catch, do nothing')
            else:
                if s not in usr_watching:
                    print('notify user logged in')
                    usr_watching.update({s: time.time()})
                    if not_first_run:
                        notify_login(tlg_id=cfg.TLG_ID_WMW, tw_chan=cfg.TW_CHAN, usr=s)
        for s in usr_watching.copy():
            if s not in catch:
                print('user logged off, notify and remove from usr_watching')
                t = arrow.get(usr_watching.get(s))
                notify_logoff(tlg_id=cfg.TLG_ID_WMW, tw_chan=cfg.TW_CHAN, usr=s, time=t)
                usr_watching.pop(s, None)
        print('catch: ' + str(catch))
        print('usr_watching:' + str(usr_watching))
        print('\n')
        not_first_run = True
        time.sleep(60)

print('Ok, working')
usr_watching = {}
loop_check()


