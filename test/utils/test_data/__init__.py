from test import test_project_root

INFERRED_VALACDOS_VERSION = 'inferred_version_1'
INFERRED_SCSUBTAB_VERSION = 'inferred_version_2'


class TestFiles:
    VOCALINK_VALACDOS = 'vocalink_4997_valacdos.txt'
    VOCALINK_SCSUBTAB = 'vocalink_1517_scsubtab.txt'
    VOCALINK_NOT_FOUND = 'vocalink_not_valid.txt'
    TOOLS_MODULUS_CHECKING_HTML = 'tools-modulus-checking-web.html'
    VOCALINK_VALACDOS_INFERRED_VERSION_1 = 'vocalink_inferred_version_1_valacdos.txt'
    VOCALINK_SCSUBTAB_INFERRED_VERSION_2 = 'vocalink_inferred_version_2_scsubtab.txt'


def read_file(file):
    with open(test_project_root().joinpath("utils", "test_data", "vocalink_responses", file)) as f:
        return f.read()
