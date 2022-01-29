#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pyshorteners

BITLY_KEY = 'insert your bit.ly key here.'

url = 'https://github.com/brtiago'
s = pyshorteners.Shortener(api_key = BITLY_KEY)
print(s.bitly.short(url))