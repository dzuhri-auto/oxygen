from .logger import logger, info, warning, debug, success, error, critical

import os

if not os.path.exists('query_ids.txt'):
    with open('query_ids.txt', 'w'): pass

if not os.path.exists('profiles.json'):
    with open('profiles.json', 'w'): pass
