from random_uk_bank_account.generator.uk_account import *

from pytest_mock import MockerFixture
import pytest

from random_uk_bank_account.utils.exceptions import UnsupportVocalinkException, VocalinkUnsupportedSortCodeError
from test.utils.test_data.vocalink_rules_objects.rule_collections import VOCALINK_RULE_COLLECTION_SINGLE_RULE, \
    VOCALINK_RULE_COLLECTION_SINGLE_RULE_UNHANDLED_EXCEPTION_CODE, VOCALINK_RULE_COLLECTION_NO_RULE


def test_generator_class_for_unsupported_vocalink_exception(tmp_path, mocker: MockerFixture):
    mocker.patch(
        'random_uk_bank_account.generator.uk_account.get_vocalink_rules_for_sort_code',
        return_value=VOCALINK_RULE_COLLECTION_SINGLE_RULE_UNHANDLED_EXCEPTION_CODE
    )
    mocker.patch(
        'random_uk_bank_account.generator.uk_account.get_vocalink_sort_code_substitution_for_sort_code',
        return_value=None
    )

    with pytest.raises(UnsupportVocalinkException):
        RandomBankAccountGenerator(sort_code='123456', db_location=str(tmp_path))


def test_generator_class_for_nonexistent_vocalink_rule(tmp_path, mocker: MockerFixture):
    mocker.patch(
        'random_uk_bank_account.generator.uk_account.get_vocalink_rules_for_sort_code',
        return_value=VOCALINK_RULE_COLLECTION_NO_RULE
    )
    mocker.patch(
        'random_uk_bank_account.generator.uk_account.get_vocalink_sort_code_substitution_for_sort_code',
        return_value=None
    )

    with pytest.raises(VocalinkUnsupportedSortCodeError):
        RandomBankAccountGenerator(sort_code='123456', db_location=str(tmp_path))


def test_generator_class_for_invalid_sort_code(tmp_path, mocker: MockerFixture):
    mocker.patch(
        'random_uk_bank_account.generator.uk_account.get_vocalink_rules_for_sort_code',
        return_value=VOCALINK_RULE_COLLECTION_SINGLE_RULE_UNHANDLED_EXCEPTION_CODE
    )
    mocker.patch(
        'random_uk_bank_account.generator.uk_account.get_vocalink_sort_code_substitution_for_sort_code',
        return_value=None
    )

    with pytest.raises(AttributeError):
        RandomBankAccountGenerator(sort_code='12345', db_location=str(tmp_path))

    with pytest.raises(AttributeError):
        RandomBankAccountGenerator(sort_code='12345a', db_location=str(tmp_path))


