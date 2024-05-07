import os


class Config:
    TIMEOUT_UI_ELEMENTS_SEC = 10

    def __init__(self) -> None:
        if os.getenv("ENV") == "DEV":
            self.BASE_URL = "google.com"
