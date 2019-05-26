import logging.config
import monitor

logging.config.fileConfig("./etc/logging.conf")
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    apis = monitor.get_api_urls("./etc/target.json")
    for api in apis:
        res = monitor.call_api(api)
        try:
            if res.ok:
                logger.info("{} API succeed.".format(api['name']))
            else:
                logger.error("{} API failed. Please check".format(api['name']))
        except AttributeError as e:
            logger.error(e)