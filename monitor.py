import json
import logging.config

import requests
from requests.exceptions import MissingSchema

logging.config.fileConfig("./etc/logging.conf")
logger = logging.getLogger(__name__)


def get_api_urls(filename):
    try:
        with open(filename, 'r') as f:
            target = json.load(f)
        return target['apis']
    except FileNotFoundError as e:
        logger.error(e)


def call_api(api):
    try:
        if api['method'] == "GET":
            res = requests.get(api['url'])
        else:
            res = requests.post(api['url'])
        return res
    except MissingSchema as e:
        logger.error(e)
    except KeyError as e:
        logger.error(e)