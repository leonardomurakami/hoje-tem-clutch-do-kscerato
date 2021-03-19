from checkDate import is_game_today
from config import MATCH_SITE_URL
from responses import positive_responses, negative_responses
from random import choice

def hoje_tem_clutch_do_kscerato():
    if is_game_today(MATCH_SITE_URL):
        return choice(positive_responses)
    return choice(negative_responses)
        