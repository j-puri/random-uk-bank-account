import pytest
from pytest_mock import MockerFixture

from random_uk_bank_account import GenerateUkBankAccount
from random_uk_bank_account.generator.uk_account import RandomBankAccountGenerator
from random_uk_bank_account.utils.config import \
    (VOCALINK_URL, DEFAULT_VOCALINK_VERSION_PATH, DEFAULT_SORT_CODE_SUBSTITUTION_VERSION_PATH)
from test.utils.test_data import read_file, TestFiles
from test.utils.test_data.vocalink_rules_objects.rule_collections import VOCALINK_RULE_COLLECTION_SINGLE_RULE


@pytest.fixture()
def generator(requests_mock, tmp_path):
    requests_mock.get(
        f"{VOCALINK_URL}/media/{DEFAULT_VOCALINK_VERSION_PATH}.txt",
        text=read_file(TestFiles.VOCALINK_VALACDOS)
    )
    requests_mock.get(
        f"{VOCALINK_URL}/media/{DEFAULT_SORT_CODE_SUBSTITUTION_VERSION_PATH}.txt",
        text=read_file(TestFiles.VOCALINK_SCSUBTAB)
    )
    return GenerateUkBankAccount(
        recreate_vocalink_db=True,
        cache_location=str(tmp_path)
    )


@pytest.fixture()
def random_bank_account_generator(mocker: MockerFixture, tmp_path):
    mocker.patch(
        'random_uk_bank_account.generator.uk_account.get_vocalink_rules_for_sort_code',
        return_value=VOCALINK_RULE_COLLECTION_SINGLE_RULE
    )
    mocker.patch(
        'random_uk_bank_account.generator.uk_account.get_vocalink_sort_code_substitution_for_sort_code',
        return_value=None
    )

    return RandomBankAccountGenerator(sort_code='123456', db_location=str(tmp_path))

