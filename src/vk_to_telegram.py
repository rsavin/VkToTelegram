#!/usr/bin/python
"""The main module"""

import json
import getopt
import sys
import time
from os.path import realpath
import constants
import telegram_sender
import vk_fetcher

help_message = 'vk_to_telegram.py properties.json'


def _read_config(config_file):
    config_json = json.loads(open(config_file).read())

    walls = config_json['walls']
    bot_token = config_json['telegram_bot_token']
    user_ids = config_json['user_ids']
    return walls, bot_token, user_ids


def main(argv):
    try:
        (opts, args) = getopt.getopt(argv, 'h:')
    except getopt.GetoptError:
        print help_message
        sys.exit(1)

    if len(args) == 0:
        print help_message
        sys.exit(1)

    for (opt, arg) in opts:
        if opt == '-h':
            print help_message
            sys.exit()

    config_file = realpath(args[0])
    last_fetch_time = 0
    while True:
        walls, bot_token, user_ids = _read_config(config_file)

        fetch_time = time.time()
        posts = vk_fetcher.fetch(walls, last_fetch_time)
        last_fetch_time = fetch_time
        if posts:
            telegram_sender.send(posts, bot_token, user_ids)
        time.sleep(constants.SLEEP_TIME)


if __name__ == '__main__':
    main(sys.argv[1:])
