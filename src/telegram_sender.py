"""Send new posts via telegram bot"""

import logging
import constants
import requests

logging.basicConfig(filename='vk_to_telegram.log', level=logging.DEBUG)
logger = logging.getLogger('telegram_sender')


def send(posts, bot_token, user_ids):
    for post in posts:
        for user_id in user_ids:
            url = constants.TELEGRAM_URL.format(bot_token)
            response = requests.post(url, data={'chat_id': user_id,
                                                'text': constants.TELEGRAM_MESSAGE_TEMPLATE.format(
                                                    post[0], post[1], post[2]
                                                )}
                                     )
            logger.debug('Send telegram status code : %s', response.status_code)
