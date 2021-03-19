from bs4 import BeautifulSoup
from datetime import datetime, date
from pydantic import BaseModel
from typing import List

import requests

def _get_page_content(url: str) -> "content":
    return requests.get(url).content


def _get_soup_from_url(url: str) -> BeautifulSoup:
    return BeautifulSoup(_get_page_content(url), "html.parser")


def get_upcoming_match_dates(soup: BeautifulSoup) -> List[str]:
    match_dates = [
        soup_result.get_text()
        for soup_result in (
            soup
            .find("div", {"class": "matches"})
            .find_all("div", {"class": "match-schedule"})
        )
    ]
    return match_dates


def transform_to_datetime(str_input: List[str]) -> List[date]:
    return [datetime.strptime(date_str.strip() + " 2021", '%b %d %I:%M%p %Y').date() for date_str in str_input]


def is_game_today(url: str) -> bool:
    today = date.today()
    soup = _get_soup_from_url(url)
    next_games_dates = transform_to_datetime(get_upcoming_match_dates(soup))
    for game_date in next_games_dates:
        if today == game_date:
            return True
    return False