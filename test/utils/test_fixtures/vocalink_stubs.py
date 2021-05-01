import pytest
from random_uk_bank_account.utils.config import \
    (VOCALINK_URL, DEFAULT_VOCALINK_VERSION_PATH, DEFAULT_SORT_CODE_SUBSTITUTION_VERSION_PATH)
from test.utils.test_data import read_file, TestFiles


@pytest.fixture()
def vocalink_standard_stubs(requests_mock):
    requests_mock.get(
        f"{VOCALINK_URL}{DEFAULT_VOCALINK_VERSION_PATH}.txt",
        text=read_file(TestFiles.VOCALINK_VALACDOS)
    )
    requests_mock.get(
        f"{VOCALINK_URL}{DEFAULT_SORT_CODE_SUBSTITUTION_VERSION_PATH}.txt",
        text=read_file(TestFiles.VOCALINK_SCSUBTAB)
    )