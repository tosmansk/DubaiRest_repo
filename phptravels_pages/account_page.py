from phptravels_utils.some_useful_utils import Logger


class AccountPage(Logger):
    """This classs validates sends GET request with https://www.phptravels.net/account/ url"""

    def __init__(self):
        super(AccountPage, self).__init__('../phptravels_logs/tour_reservation.log')

