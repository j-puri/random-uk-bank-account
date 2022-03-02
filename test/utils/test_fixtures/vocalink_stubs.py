import pytest
from random_uk_bank_account.utils.config import \
    (VOCALINK_URL, DEFAULT_VOCALINK_VERSION_PATH, DEFAULT_SORT_CODE_SUBSTITUTION_VERSION_PATH)
from test.utils.test_data import read_file, TestFiles, INFERRED_VALACDOS_VERSION, INFERRED_SCSUBTAB_VERSION


@pytest.fixture()
def vocalink_standard_stubs(requests_mock):
    requests_mock.get(
        f"{VOCALINK_URL}/media/{DEFAULT_VOCALINK_VERSION_PATH}.txt",
        text=read_file(TestFiles.VOCALINK_VALACDOS)
    )
    requests_mock.get(
        f"{VOCALINK_URL}/media/{DEFAULT_SORT_CODE_SUBSTITUTION_VERSION_PATH}.txt",
        text=read_file(TestFiles.VOCALINK_SCSUBTAB)
    )
    requests_mock.get(
        f"{VOCALINK_URL}/tools/modulus-checking",
        text=read_file(TestFiles.TOOLS_MODULUS_CHECKING_HTML)
    )
    requests_mock.get(
        f"{VOCALINK_URL}/media/{INFERRED_VALACDOS_VERSION}/valacdos.txt",
        text=read_file(TestFiles.VOCALINK_VALACDOS_INFERRED_VERSION_1)
    )
    requests_mock.get(
        f"{VOCALINK_URL}/media/{INFERRED_SCSUBTAB_VERSION}/scsubtab.txt",
        text=read_file(TestFiles.VOCALINK_SCSUBTAB_INFERRED_VERSION_2)
    )