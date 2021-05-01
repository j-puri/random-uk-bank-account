import pytest

from test.utils.test_fixtures.classes_under_test import generator

@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("118765", "64371389")
    ])
def test_known_values_for_exception_1(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)


@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("309070", "02355688"),
        ("309070", "12345668"),
        ("309070", "12345677"),
        ("309070", "99345694")
    ])
def test_known_values_for_exception_2_and_9(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)


@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("820000", "73688637"),
        ("827999", "73988638"),
        ("827101", "28748352"),
    ])
def test_known_values_for_exception_3(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)


@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("134020", "63849203")
    ])
def test_known_values_for_exception_4(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)


@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("938611", "07806039"),
        ("938611", "42368003"),
        ("938063", "55065200")
    ])
def test_known_values_for_exception_5(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)


@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("200915", "41011166")
    ])
def test_known_values_for_exception_6(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)


@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("772798", "99345694")
    ])
def test_known_values_for_exception_7(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)


@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("086090", "06774744")
    ])
def test_known_values_for_exception_8(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)


@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("871427", "46238510"),
        ("872427", "46238510"),
        ("871427", "09123496"),
        ("871427", "99123496"),

    ])
def test_known_values_for_exception_10_and_11(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)


@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("074456", "12345112"),
        ("070116", "34012583"),
        ("074456", "11104102")
    ])
def test_known_values_for_exception_12_and_13(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)


@pytest.mark.parametrize(
    "sort_code,account_number", [
        ("180002", "00000190")
    ])
def test_known_values_for_exception_14(generator, sort_code, account_number):
    assert generator.validate(sort_code=sort_code, account_number=account_number)
