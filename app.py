import logging.config

import monitor


logging.config.fileConfig("./etc/logging.conf")
logger = logging.getLogger(__name__)

ERRORS = ['NotFound', 'ParamError', 'InternalError']

if __name__ == "__main__":
    apis = monitor.get_api_urls("./etc/target.json")
    for api in apis:
        res = monitor.call_api(api)
        res.encoding = "utf-8"
        result = res.json()
        try:
            if result['status'] in ERRORS:
                logger.error("{} API failed. Please check".format(api['name']))
            else:
                logger.info("{} API succeed.".format(api['name']))
        except AttributeError as e:
            logger.error(e)