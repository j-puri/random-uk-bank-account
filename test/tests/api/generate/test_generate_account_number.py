import pytest

from random_uk_bank_account import RandomBankAccount, GenerateUkBankAccount

from test.utils.test_fixtures.classes_under_test import generator

def test_generate_for_sort_code(generator: GenerateUkBankAccount):

    sort_code = "118765"
    random_account = generator.generate_for_sort_code(sort_code)
    assert isinstance(random_account, RandomBankAccount)

    assert random_account.sort_code == sort_code
    assert len(random_account.account_numbers) == 1
    assert isinstance(random_account.account_numbers[0], str)
    assert len(random_account.account_numbers[0]) == 8


def test_generate_10_for_sort_code(generator: GenerateUkBankAccount):
    sort_code = "827101"
    random_account = generator.generate_for_sort_code(sort_code, total=10)
    assert isinstance(random_account, RandomBankAccount)

    assert random_account.sort_code == sort_code
    assert len(set(random_account.account_numbers)) == 10



def test_generate_for_sort_codes_are_validated(generator: GenerateUkBankAccount):
    sort_code = "200915"

    random_account = generator.generate_for_sort_code(sort_code, total=100)

    for account_number in random_account.account_numbers:
        assert generator.validate(account_number=account_number, sort_code=sort_code)


@pytest.mark.parametrize('sort_code', ['0404', "04000a"])
def test_generate_for_invalid_sort_code(sort_code, generator: GenerateUkBankAccount):
    with pytest.raises(AttributeError):
        generator.generate_for_sort_code(sort_code, total=100)
