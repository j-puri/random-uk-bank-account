from random_uk_bank_account.client import HttpSession
from random_uk_bank_account.utils.config import VOCALINK_URL
from random_uk_bank_account.utils.exceptions import IncompatibleVocalinkVersion


class VocalinkApi(HttpSession):
    def __init__(self):
        super().__init__()

    def get_vocalink_modulus_media(self, version) -> str:
        data = self.session.get(url=f"{VOCALINK_URL}{version}.txt")
        data.raise_for_status()

        if "Sorry, we can't find that page" in data.text:
            raise IncompatibleVocalinkVersion(data.url)

        return data.text
