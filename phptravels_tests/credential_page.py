import requests
from lxml import html

class CredentialPage(object):
    """This class retrieves credential data for login purpose. This need to be use with requests solution"""

    def retrive_credential_data(self, credential_url):
        """This function makes request to get credential data"""

        credentials = {}
        url = credential_url
        request_get = requests.get(url)

        # Find credential data from request.content
        tree = html.fromstring(request_get.content)
        credential_data = tree.xpath('//section[2]/div/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[2]/div/text()')
        # Add data to the dict
        credentials['username'] = credential_data[1].strip()
        credentials['password'] = credential_data[3].strip()

        return credentials
