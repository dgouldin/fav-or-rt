#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import random

from emoji import UNICODE_EMOJI
from requests_oauthlib import OAuth1Session


if __name__ == '__main__':
    emojis = filter(
        lambda e: ' ' not in e,
        UNICODE_EMOJI.keys(),
    )
    status = 'fav for {}, rt for {}'.format(
        random.choice(emojis),
        random.choice(emojis),
    )

    twitter = OAuth1Session(
        os.environ['TWITTER_CONSUMER_KEY'],
        client_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        resource_owner_key=os.environ['TWITTER_ACCESS_TOKEN'],
        resource_owner_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
    )
    twitter.post('https://api.twitter.com/1.1/statuses/update.json', params={
        'status': status,
    })
