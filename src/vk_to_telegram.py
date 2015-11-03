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

    properties_file = realpath(args[0])
    properties_json = json.loads(open(properties_file).read())

    last_fetch_time = 0
    walls = properties_json['walls']
    bot_token = properties_json['telegram_bot_token']
    user_ids = properties_json['user_ids']

    while True:
        fetch_time = time.time()
        posts = vk_fetcher.fetch(walls, last_fetch_time)
        last_fetch_time = fetch_time
        telegram_sender.send(posts, bot_token, user_ids)
        time.sleep(constants.SLEEP_TIME)


if __name__ == '__main__':
    main(sys.argv[1:])
