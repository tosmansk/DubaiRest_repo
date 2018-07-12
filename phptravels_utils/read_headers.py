from phptravels_utils.some_useful_utils import Logger


class ReadHeadersFromFile(Logger):

    def __init__(self):
        super(ReadHeadersFromFile, self).__init__('../phptravels_logs/utils.log')

    def read_header_file(self, method):
        """This method read from the file to dict output"""

        request_method = method

        if request_method == "GET":

            get_file_path = '../phptravels_conf/get_headers'

            try:
                with open(get_file_path, 'r') as get_conf_file:
                    get_data  = eval(get_conf_file.read())
                    self.log.info('GET HEADERS CORRECTLY OBTAINED')

                    return get_data
            except:
                self.log.critical("Not able to read the {} file".format(get_file_path))

            finally:
                get_conf_file.close()

        elif request_method == "POST":

            post_file_path = '../phptravels_conf/post_headers'

            try:
                with open(post_file_path, 'r') as post_conf_file:
                    post_data = eval(post_conf_file.read())
                    self.log.info('POST HEADERS CORRECTLY OBTAINED')

                    return post_data
            except:
                self.log.critical("NOT ABLE TO READ THE {} FILE".format(post_file_path))

            finally:
                post_conf_file.close()


if __name__ == "__main__":
    proba2 = ReadHeadersFromFile()
    print(proba2.read_header_file('POST'))
