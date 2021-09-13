from test import test_project_root


class TestFiles:
    VOCALINK_VALACDOS = 'vocalink_4998_valacdos.txt'
    VOCALINK_SCSUBTAB = 'vocalink_1517_scsubtab.txt'
    VOCALINK_NOT_FOUND = 'vocalink_not_valid.txt'


def read_file(file):
    with open(test_project_root().joinpath("utils", "test_data", "vocalink_responses", file)) as f:
        return f.read()
