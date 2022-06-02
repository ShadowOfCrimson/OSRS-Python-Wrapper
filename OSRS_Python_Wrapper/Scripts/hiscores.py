import requests as rq

# Import supporting scripts
import const
import exceptions as err

# --------------------------------------------------------- Supporting Functions

def validate_hs_params(username, account_type):
    '''Verifies provided info when creating a Hiscore object'''
    if len(username) > 12:
        raise err.BadUsername(username, "Twelve Error")
    for char in username:
        if char not in const.valid_username_chars:
            raise err.BadUsername(username, "Char Error")

    if account_type not in const.valid_account_types and account_type is not None:
        raise err.BadAccountType(account_type)
    if account_type is None:
        final_type = get_acc_type(username)
        return username, final_type

    response = rq.get(const.hiscore_link_dict[account_type] + username)
    if response.status_code == 404:
        raise err.UserNotFound(username, account_type)
    return username, account_type

def get_acc_type(username):
    '''Attempts to get account type with the given username'''
    for acc_type in reversed(const.valid_account_types):
        response = rq.get(const.hiscore_link_dict[acc_type] + username)
        if response.status_code == 404:
            continue
        else:
            return acc_type
    raise err.UserNotFound(username)

def process_hiscore_response(username, account_type):
    '''Processes the messy response from the Hiscores API and makes it an easier to work with dict'''
    response = rq.get(const.hiscore_link_dict[account_type] + username)
    formatted_response = ((response.text).replace("\n", ",")).split(",")
    for index, entry in enumerate(formatted_response):
        pass  # TODO

# --------------------------------------------------------- Main Class

class Hiscores:
    def __init__(self, username, account_type = None):
        returned_info = validate_hs_params(username, account_type)
        self.username = returned_info[0]
        self.account_type = returned_info[1]

    def get_level(self, skill):
        skills_dict = process_hiscore_response(self.username, self.account_type)
        # TODO
