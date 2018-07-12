import requests
from phptravels_tests.credential_page import CredentialPage
from phptravels_tests.read_config_data import ReadConfigData
from phptravels_utils.html_parser import HtmlParser
from phptravels_utils.read_headers import ReadHeadersFromFile
from phptravels_utils.some_useful_utils import Logger, SomeUsefulUtils


class LoginPage(Logger):
    """This class makes login action using request lib."""

    def __init__(self):

        super(LoginPage, self).__init__('../phptravels_logs/tour_reservation.log')
        self.read_config = ReadConfigData()
        self.title_element = '//title'
        self.email_element = "//input[@placeholder='Email']"
        self.passwd_element = "//input[@placeholder='Password']"
        self.login_client = requests.session()
        self.utils = SomeUsefulUtils()

    def get_login_credentaials(self):
        """This function calls credential_page to get credentials"""

        # Obtain credential_url from ini config file
        credential_url = self.read_config.read_config_ini()['credential_url']
        get_credentials = CredentialPage()

        return get_credentials.retrive_credential_data(credential_url)

    def get_login_page(self):
        """This function makes login GET request sent and make parsing of some element on the page"""

        browser = self.read_config.read_config_ini()['browser']
        elements = {}

        if browser == 'Firefox':

            # Set Firefox header for Get message

            headers_reader = ReadHeadersFromFile()
            get_header_data = headers_reader.read_header_file('GET')
        elif browser == "Chrome":
            raise NotImplemented

        get_login_response = self.login_client.get(self.utils.prepare_url('/login'), headers=get_header_data)
        self.log.debug("Get response code: {}".format(get_login_response.status_code))
        parser = HtmlParser()

        # This is page data for later assertation usage

        elements['title'] = parser.find_element(content=get_login_response.content,
                                                element=self.title_element, el_type='xpath', obtain='text')
        elements['Email'] = parser.find_element(content=get_login_response.content,
                                                element=self.email_element, el_type='xpath', obtain='name')
        elements['Password'] = parser.find_element(content=get_login_response.content,
                                                element=self.passwd_element, el_type='xpath', obtain='name')

        # Returned elements {'title': ['Login'], 'Email': ['username'], 'Password': ['password']}
        return elements

    def make_loggin(self):
        """This function send post request to make logging"""

        url = self.utils.prepare_url("account/login")

        # Set Firefox headers for POST message

        headers_reader = ReadHeadersFromFile()
        post_header_data = headers_reader.read_header_file('POST')
        post_data = self.get_login_credentaials()
        post_login_response = self.login_client.post(url, headers=post_header_data,
                                                     data=post_data)
        self.log.debug("Get response code: {}".format(post_login_response.status_code))

        return post_login_response.text.strip()

    def temp_check(self, resp):
        print(resp)
        print(resp.content)
        print(resp.status_code)
        print(resp.cookies)
        print(resp.headers)
        print(resp.text)
        print(resp.history)

if __name__ == "__main__":
    proba1 = LoginPage()
    proba1.get_login_credentaials()
    proba1.get_login_page()
    proba1.make_loggin()