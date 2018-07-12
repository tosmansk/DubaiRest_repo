import logging

from phptravels_tests.read_config_data import ReadConfigData


class Logger():
    """ This class configures basic logging """

    def __init__(self, file_path):

        logging_format = '%(levelname)-15s %(asctime)s %(funcName)s %(message)s'
        logging.basicConfig(filename=file_path, level=logging.DEBUG, format=logging_format)
        self.log = logging.getLogger(__name__)


class SomeUsefulUtils(object):
    """This class consists some functions from utils"""

    read_config = ReadConfigData()

    def prepare_url(self, suffix):
        """This function retrieves and construct url to be used"""

        # Obtain url from ini config file
        url = self.read_config.read_config_ini()['url']

        return url.rstrip('/') + '/' + suffix.lstrip('/')