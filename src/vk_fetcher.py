"""Fetch new posts from vk communities walls"""

import collections
import logging
import requests
import constants

logging.basicConfig(filename='vk_to_telegram.log', level=logging.DEBUG)
logger = logging.getLogger('vk_fetcher')


def fetch(walls, last_fetch_time):
    logger.debug('fetch(%s, %s)', walls, last_fetch_time)

    posts = []

    for wall in walls:
        posts.extend(_get_wall_posts(wall, last_fetch_time))

    return posts


def _get_wall_posts(wall, last_fetch_time):
    logger.debug('_get_wall_posts(%s, %s)', wall, last_fetch_time)

    new_posts = []
    url = constants.VK_PUBLIC_WALL_URL.format(wall, 5)
    response = requests.get(url)

    logger.debug(response.status_code)
    if response.status_code == requests.codes.ok:
        new_posts = map(lambda x: (wall, x['text'], _get_photos(x), _format_post_url(wall, x)),
                        filter(lambda x:
                               isinstance(x, collections.Iterable) and 'date' in x and x['date'] > last_fetch_time,
                               response.json()['response']
                               )
                        )

    logger.debug('new posts count : %s', len(new_posts))

    logger.debug(new_posts)
    return new_posts


def _format_post_url(wall, post):
    return constants.VK_POST_URL.format(wall, post['to_id'], post['id'])


def _get_photos(post):
    if 'attachments' in post:
        return map(lambda x: x['photo']['src_big'], filter(lambda x: x['type'] == 'photo', post['attachments']))
