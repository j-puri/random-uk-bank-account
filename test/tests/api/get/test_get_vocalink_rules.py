from random_uk_bank_account import VocalinkRuleCollection, GenerateUkBankAccount, VocalinkSortCodeSubstitutionCollection, \
    VocalinkSortCodeSubstitution
import pytest

from test.utils.test_fixtures.classes_under_test import generator


def test_get_rules_for_existing_sort_code(generator: GenerateUkBankAccount):
    rules = generator.get_vocalink_rules("040004")
    assert isinstance(rules, VocalinkRuleCollection)
    assert isinstance(rules.to_dict(), dict)
    assert isinstance(rules.to_json(), str)


def test_get_rules_for_non_existing_sort_code(generator: GenerateUkBankAccount):
    rules = generator.get_vocalink_rules("040001")
    assert len(rules.rules) == 0


@pytest.mark.parametrize('sort_code', ['0404', "04000a"])
def test_get_rules_for_invalid_sort_code(generator: GenerateUkBankAccount, sort_code):
    with pytest.raises(AttributeError):
        generator.get_vocalink_rules(sort_code)


def test_get_sort_code_substitutions_for_sort_code_with_no_substitutions(generator: GenerateUkBankAccount):
    substitution = generator.get_vocalink_substitution('040004')
    assert not substitution.substituted_sort_code
    assert not substitution.original_sort_code

def test_get_sort_code_substituion_for_sort_code_with_substition(generator: GenerateUkBankAccount):
    substitution = generator.get_vocalink_substitution('938618')
    assert substitution.substituted_sort_code
    assert substitution.original_sort_code
    assert isinstance(substitution, VocalinkSortCodeSubstitution)


def test_get_all_sort_code_substitutions(generator: GenerateUkBankAccount):
    substitutions = generator.get_all_vocalink_substitutions()
    assert isinstance(substitutions, VocalinkSortCodeSubstitutionCollection)
    assert len(substitutions.substitutions) > 0
    assert isinstance(substitutions.substitutions[0], VocalinkSortCodeSubstitution)

