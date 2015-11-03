"""Send new posts via telegram bot"""

import logging

import requests

import constants

logging.basicConfig(filename='vk_to_telegram.log', level=logging.DEBUG)
logger = logging.getLogger('telegram_sender')


def send(posts, bot_token, user_ids):
    for post in posts:
        for user_id in user_ids:
            url = constants.TELEGRAM_URL.format(bot_token)
            response = requests.post(url, data={'chat_id': user_id,
                                                'text': u'Community : {0}\nText : {1}\n'.format(post[0], post[1])})
            logger.debug('Send telegram status code : %s', response.status_code)
