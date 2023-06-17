#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""124bot constants"""

from typing import Final

from reactionmenu import ReactionButton  # type: ignore

BOT_DB_URL: Final[str] = "sqlite:///bot.db?check_same_thread=False"
MESSAGE_WRAP_LEN: Final[int] = 1900
BUTTONS: Final[tuple[ReactionButton, ...]] = (
    ReactionButton.go_to_first_page(),
    ReactionButton.back(),
    ReactionButton.next(),
    ReactionButton.go_to_last_page(),
)
MAX_PRESENCE_LEN: Final[int] = 64
OK_CHANNEL: Final[str] = "ok"
RULES_CHANNEL: Final[str] = "rules"
REAL_RULES_ID: Final[tuple[str, ...]] = ("(real rule)", "( real rule )")
FAKE_RULES_ID: Final[tuple[str, ...]] = ("(fake rule)", "( fake rule )")
MIN_WORDCLOUD_LIMIT: Final[int] = 500
WORDCLOUD_WRAP: Final[int] = 540
MIN_RULES_LIMIT: Final[int] = 1000
MIN_CONFESSION_LIMIT: Final[int] = 500

MSGS_W: Final[float] = 0.08
VCS_W: Final[float] = 0.1
WC_W: Final[float] = 0.12
REACT_GET_W: Final[float] = 0.2
REACT_POST_W: Final[float] = 0.15

REACT_POST_K: Final[float] = 0.7
