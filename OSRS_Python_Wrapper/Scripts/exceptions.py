class UserNotFound(Exception):
    def __init__(self, username, account_type = None):
        if account_type == "n" or account_type == "n":
            super().__init__(f"No account by the name \"{username}\" could be found")
        elif account_type == "i":
            super().__init__(f"No account by the name \"{username}\" of type \"Ironman\" could be found")
        elif account_type == "hi":
            super().__init__(f"No account by the name \"{username}\" of type \"Hardcore Ironman\" could be found")
        elif account_type == "ui":
            super().__init__(f"No account by the name \"{username}\" of type \"Ultimate Ironman\" could be found")

class BadUsername(Exception):
    def __init__(self, username, error_type):
        if error_type == "Twelve Error":
            super().__init__(f"The username \"{username}\" is larger then 12 charactors")
        elif error_type == "Char Error":
            super().__init__(f"The username \"{username}\" contains illegal charactors")


class BadAccountType(Exception):
    def __init__(self, given_type):
        super().__init__(f"The given account type \"{given_type}\" is not a valid account type.")
