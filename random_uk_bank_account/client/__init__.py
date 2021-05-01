import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


class HttpSession:
    def __init__(self):
        self.session = requests.Session()

        retries = Retry(
            total=5,
            backoff_factor=0.1,
            status_forcelist=[500, 502, 503, 504]
        )

        self.session.mount('https://', HTTPAdapter(max_retries=retries))
