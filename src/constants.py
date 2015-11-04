"""Various constants."""

from __future__ import unicode_literals

VK_PUBLIC_WALL_URL = 'https://api.vk.com/method/wall.get?domain={0}&count={1}'

VK_POST_URL = 'https://vk.com/{0}?w=wall{1}_{2}'

TELEGRAM_URL = 'https://api.telegram.org/bot{0}/sendMessage'

TELEGRAM_MESSAGE_TEMPLATE = u'_COMMUNITY_ : {0}\n\n_TEXT_ : {1}\n\n_PHOTOS_ : {2}\n\n_LINK_ : {3}'

DEBUG_SLEEP_TIME = 5
'''10 seconds between fetches for debug'''

SLEEP_TIME = 60
'''5 minutes between fetches'''
