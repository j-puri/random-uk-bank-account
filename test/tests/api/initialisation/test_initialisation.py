import logging

from random_uk_bank_account import GenerateUkBankAccount
from random_uk_bank_account.utils.config import DEFAULT_VOCALINK_VERSION_PATH, VOCALINK_URL
import os
import pytest
import pathlib

from random_uk_bank_account.utils.exceptions import IncompatibleVocalinkVersion
from test.utils.test_data import read_file, TestFiles, INFERRED_VALACDOS_VERSION, INFERRED_SCSUBTAB_VERSION
from test.utils.test_fixtures.vocalink_stubs import vocalink_standard_stubs


def test_vocalink_init_with_specific_cache_location(vocalink_standard_stubs, tmp_path):
    GenerateUkBankAccount(
        recreate_vocalink_db=True,
        cache_location=tmp_path.name
    )

    folder_contents = os.listdir(tmp_path.name)
    assert f"{DEFAULT_VOCALINK_VERSION_PATH}.db".replace('/', '-') in folder_contents
    assert len(folder_contents) == 1


def test_vocalink_init_with_specified_valid_version(requests_mock, vocalink_standard_stubs, tmp_path):
    version = "4941/valacdos"

    requests_mock.get(
        f"{VOCALINK_URL}/media/{version}.txt",
        text=read_file(TestFiles.VOCALINK_VALACDOS)
    )

    GenerateUkBankAccount(
        recreate_vocalink_db=True,
        cache_location=tmp_path.name,
        vocalink_rules_version=version
    )

    folder_contents = os.listdir(tmp_path.name)
    assert f"{version}.db".replace('/', '-') in folder_contents
    assert len(folder_contents) == 1


def test_vocalink_init_with_specified_invalid_version(requests_mock, vocalink_standard_stubs, tmp_path):
    """
    Generator attempts to parse html form https://www.vocalink.com/tools/modulus-checking/ to find current versions
    if current config results in 404's from Vocalink
    """

    version = "1111/valacdos"

    requests_mock.get(
        f"{VOCALINK_URL}/media/{version}.txt",
        text=read_file(TestFiles.VOCALINK_NOT_FOUND)
    )

    generator = GenerateUkBankAccount(
        log_level=logging.DEBUG,
        recreate_vocalink_db=True,
        cache_location=tmp_path.name,
        vocalink_rules_version=version
    )

    assert generator.VOCALINK_VERSION == f"{INFERRED_VALACDOS_VERSION}/valacdos"
    assert generator.VOCALINK_SUBSTITUTION_VERSION == f"{INFERRED_SCSUBTAB_VERSION}/scsubtab"


def test_vocalink_init_with_invalid_substitution_version(requests_mock, vocalink_standard_stubs, tmp_path):
    """
    Generator attempts to parse html form https://www.vocalink.com/tools/modulus-checking/ to find current versions
    if current config results in 404's from Vocalink
    """

    version = "1111/scsubtab"

    requests_mock.get(
        f"{VOCALINK_URL}/media/{version}.txt",
        text=read_file(TestFiles.VOCALINK_NOT_FOUND)
    )

    generator = GenerateUkBankAccount(
        log_level=logging.DEBUG,
        recreate_vocalink_db=True,
        cache_location=str(tmp_path),
        vocalink_substitution_version=version
    )

    assert generator.VOCALINK_SUBSTITUTION_VERSION == f"{INFERRED_SCSUBTAB_VERSION}/scsubtab"
    assert generator.VOCALINK_SUBSTITUTION_VERSION == f"{INFERRED_SCSUBTAB_VERSION}/scsubtab"


def test_vocalink_init_with_recreate_true(vocalink_standard_stubs, tmp_path):
    generator_1 = GenerateUkBankAccount(
        log_level=logging.DEBUG,
        recreate_vocalink_db=False,
        cache_location=str(tmp_path),
    )

    file_before = tmp_path.joinpath(f"{generator_1.VOCALINK_VERSION}.db".replace('/', '-'))
    created_time_before = pathlib.Path(file_before).stat().st_ctime

    generator_2 = GenerateUkBankAccount(
        log_level=logging.DEBUG,
        recreate_vocalink_db=True,
        cache_location=str(tmp_path),
    )

    file_after = tmp_path.joinpath(f"{generator_2.VOCALINK_VERSION}.db".replace('/', '-'))
    created_time_after = pathlib.Path(file_after).stat().st_ctime

    assert created_time_before != created_time_after


def test_vocalink_init_with_recreate_false(vocalink_standard_stubs, tmp_path):
    generator_1 = GenerateUkBankAccount(
        log_level=logging.DEBUG,
        recreate_vocalink_db=False,
        cache_location=str(tmp_path),
    )

    file_before = tmp_path.joinpath(f"{generator_1.VOCALINK_VERSION}.db".replace('/', '-'))
    created_time_before = pathlib.Path(file_before).stat().st_ctime

    generator_2 = GenerateUkBankAccount(
        log_level=logging.DEBUG,
        recreate_vocalink_db=False,
        cache_location=str(tmp_path),
    )

    file_after = tmp_path.joinpath(f"{generator_2.VOCALINK_VERSION}.db".replace('/', '-'))
    created_time_after = pathlib.Path(file_after).stat().st_ctime

    assert created_time_before == created_time_after
