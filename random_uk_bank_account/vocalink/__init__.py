from random_uk_bank_account.vocalink.vocalink_data import get_vocalink_data, get_vocalink_substitutions
from random_uk_bank_account.vocalink.vocalink_db_init import CreateVocalinkDb

import logging
import os


def set_db_location(cache_location, version):
    if not os.path.isdir(cache_location):
        os.mkdir(cache_location)

    db_file_location = f"{cache_location}{os.sep}{version.replace('/', '-')}.db"

    return cache_location, db_file_location

def initialise(cache_location, version, sort_code_subs_version, recreate, logger=logging.getLogger()):

    base_path, db_file_location = set_db_location(cache_location, version)

    if os.path.isfile(db_file_location) and not recreate:
        logger.debug(f"{version} has been cached previously in {base_path}")
        logger.debug(f"{sort_code_subs_version} has been cached previously in {base_path}")

    else:
        if recreate:
            logger.debug(f"Deleting previously created {db_file_location}")
            try:
                os.remove(db_file_location)
            except:
                logger.warning(f"Unable to remove {db_file_location} for recreate mode. Ignoring and moving on.")

        if not os.path.isdir(base_path):
            os.mkdir(base_path)

        vocalink_data = get_vocalink_data(version)
        vocalink_sort_code_substitutions = get_vocalink_substitutions(sort_code_subs_version)

        CreateVocalinkDb(db_file_location, vocalink_data, vocalink_sort_code_substitutions).build()
        logger.debug(f"Vocalink data saved to {db_file_location}")

    return cache_location, db_file_location
