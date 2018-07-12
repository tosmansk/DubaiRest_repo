import configparser


class ReadConfigData(object):
    """This class supports data retrieval from config files"""

    config = configparser.ConfigParser()

    def read_config_ini(self):
        """This function reads from config.ini file, WebDriver configuration data"""

        config_ini = {}

        config = self.config
        self.config.read('../phptravels_conf/config.ini')

        config_ini['url'] = config['Rest']['url']
        config_ini['credential_url'] = config['Rest']['credential_url']
        config_ini['browser'] = config['Rest']['browser']

        return config_ini

    def read_personal_data_ini(self):
        """This function reads personal_data.ini configuration file"""

        porsonal_data_ini = {}
        guest1_dict, guest2_dict, guest3_dict = {}, {}, {}

        config = self.config
        self.config.read('../phptravels_config/personal_data.ini')

        # quest1 data
        guest1_dict['first_name'] = config['Guest1']['first_name']
        guest1_dict['last_name'] = config['Guest1']['last_name']
        guest1_dict['email'] = config['Guest1']['email']
        guest1_dict['mphone'] = config['Guest1']['mphone']
        guest1_dict['address'] = config['Guest1']['address']
        guest1_dict['country'] = config['Guest1']['country']
        guest1_dict['passport'] = config['Guest1']['passport']
        guest1_dict['age'] = config['Guest1']['age']

        # quest2 data
        guest2_dict['first_name'] = config['Guest2']['first_name']
        guest2_dict['last_name'] = config['Guest2']['last_name']
        guest2_dict['email'] = config['Guest2']['email']
        guest2_dict['mphone'] = config['Guest2']['mphone']
        guest2_dict['address'] = config['Guest2']['address']
        guest2_dict['country'] = config['Guest2']['country']
        guest2_dict['passport'] = config['Guest2']['passport']
        guest2_dict['age'] = config['Guest2']['age']
        # quest2 data
        guest3_dict['first_name'] = config['Guest3']['first_name']
        guest3_dict['last_name'] = config['Guest3']['last_name']
        guest3_dict['email'] = config['Guest3']['email']
        guest3_dict['mphone'] = config['Guest3']['mphone']
        guest3_dict['address'] = config['Guest3']['address']
        guest3_dict['country'] = config['Guest3']['country']
        guest3_dict['passport'] = config['Guest3']['passport']
        guest3_dict['age'] = config['Guest3']['age']

        porsonal_data_ini['guest1'] = guest1_dict
        porsonal_data_ini['guest2'] = guest2_dict
        porsonal_data_ini['guest3'] = guest3_dict

        return porsonal_data_ini

    def read_flight_data_ini(self):
        """This function reads flight_data.ini configuration file"""

        flight_data_ini = {}

        config = self.config
        self.config.read('../phptravels_config/flight_data.ini')

        flight_data_ini['from_airport'] = config['FlightData']['from_airport']
        flight_data_ini['to_airport'] = config['FlightData']['to_airport']
        flight_data_ini['flight_start_date'] = config['FlightData']['flight_start_date']
        flight_data_ini['flight_return_date'] = config['FlightData']['flight_return_date']
        flight_data_ini['adult_passengers'] = config['FlightData']['adult_passengers']
        flight_data_ini['child_passengers'] = config['FlightData']['child_passengers']
        flight_data_ini['infant_passengers'] = config['FlightData']['infant_passengers']

        return flight_data_ini