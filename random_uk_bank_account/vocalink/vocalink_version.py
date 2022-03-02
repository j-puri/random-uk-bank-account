from bs4 import BeautifulSoup
import re

from random_uk_bank_account.client.vocalink import VocalinkApi
from random_uk_bank_account.utils.exceptions import ErrorInferringVocalinkVersions

SORT_CODE_SUB_LINK_TEXT = "Sorting Code Substitution Data"
MODULUS_WEIGHT_TABLE_LINK_TEXT = "Modulus weight table data"

def _extract_version(html: BeautifulSoup, link_text: str, logger):
    try:
        sort_code_link = html.find_all("a", string=link_text)[0].attrs['href']
        return re.findall(r'/media/(.+?).txt', sort_code_link)[0]
    except Exception as e:
        raise ErrorInferringVocalinkVersions(logger, e)

def get_inferred_latest_versions(logger):
    html = BeautifulSoup(VocalinkApi().get_vocalink_modulus_checking_page(), features="html.parser")
    modulus_version = _extract_version(html, MODULUS_WEIGHT_TABLE_LINK_TEXT, logger)
    sort_code_substitution = _extract_version(html, SORT_CODE_SUB_LINK_TEXT, logger)
    return modulus_version, sort_code_substitution
