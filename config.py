#!/usr/bin/env python3
import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """
    APP_ID = os.environ.get("MICROSOFT_APP_ID", "")
    APP_PASSWORD = os.environ.get("MICROSOFT_APP_PASSWORD", "")
    GOOGLE_SERVICE_ACCOUNT = os.environ.get("GOOGLE_SERVICE_ACCOUNT", "")
    SPREADSHEET_FAQ = "Taiwan Bot FAQ"
    SPREADSHEET_LOG = "Taiwan Bot Log"
    SHEET_GENERAL = "General"
    SHEET_GOLDCARD = "GoldCard"
