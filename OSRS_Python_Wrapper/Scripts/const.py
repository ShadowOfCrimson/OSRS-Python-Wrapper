# Contains the proper links for retrieving account stats relative to the account type
hiscore_link_dict = {
    "n": r"https://secure.runescape.com/m=hiscore_oldschool/index_lite.ws?player=",
    "i": r"https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.ws?player=",
    "hi": r"https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/index_lite.ws?player=",
    "ui": r"https://secure.runescape.com/m=hiscore_oldschool_ultimate/index_lite.ws?player="
}

# Contains the only valid charactors for usernames
# Lowercase a-z, 0-9, "_", and " "
valid_username_chars = [
        "a", "b", "c", "d", "e", "f", "g", "h",
        "i", "j", "k", "l", "m", "n", "o", "p",
        "q", "r", "s", "t", "u", "v", "w", "x",
        "y", "z", "0", "1", "2", "3", "4", "5",
        "6", "7", "8", "9", "_", " "
]

# Contains the only valid account types
# N=Normal, I=Ironman, HI=Hardcore Ironman, UI=Ultimate Ironman
valid_account_types = ["n", "i", "hi", "ui"]
