"""Various constants."""

from __future__ import unicode_literals

VK_PUBLIC_WALL_URL = 'https://api.vk.com/method/wall.get?domain={0}&count={1}'

TELEGRAM_URL = 'https://api.telegram.org/bot{0}/sendMessage'

DEBUG_SLEEP_TIME = 5
'''10 seconds between fetches for debug'''

SLEEP_TIME = 60
'''5 minutes between fetches'''
