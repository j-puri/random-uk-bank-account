from random_uk_bank_account.vocalink.vocalink_model import VocalinkRuleCollection, VocalinkSortCodeSubstitutionCollection
from random_uk_bank_account.client.sqlite3 import SqlLite


class CreateVocalinkDb:

    def __init__(self, DB_LOCATION: str, vocalink_rules: VocalinkRuleCollection,
                 vocalink_sort_code_substitutions: VocalinkSortCodeSubstitutionCollection):

        self.db = SqlLite(local_db=DB_LOCATION)
        self.vocalink_rules = vocalink_rules
        self.vocalink_sort_code_substitutions = vocalink_sort_code_substitutions

    def build(self):
        self._create_table()
        self._insert_data()

    def _insert_data(self):
        self.db.conn.executemany("INSERT INTO vocalink_rules VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                 self.vocalink_rules.to_ordered_tuple_list())
        self.db.conn.executemany("INSERT INTO vocalink_sort_code_substitutions VALUES (?,?)",
                                 self.vocalink_sort_code_substitutions.to_ordered_tuple_list())

        self.db.commit()


    def _create_table(self):
        self.db.conn.executescript("""
                DROP TABLE IF EXISTS vocalink_rules;

                CREATE TABLE vocalink_rules (
                    sort_code_from VARCHAR(6) NOT NULL,
                    sort_code_to VARCHAR(6) NOT NULL,
                    algorithm VARCHAR(10) NOT NULL,
                    sort_code_pos_1 INT NOT NULL,
                    sort_code_pos_2 INT NOT NULL,
                    sort_code_pos_3 INT NOT NULL,
                    sort_code_pos_4 INT NOT NULL,
                    sort_code_pos_5 INT NOT NULL,
                    sort_code_pos_6 INT NOT NULL,
                    account_number_pos_1 INT NOT NULL,
                    account_number_pos_2 INT NOT NULL,
                    account_number_pos_3 INT NOT NULL,
                    account_number_pos_4 INT NOT NULL,
                    account_number_pos_5 INT NOT NULL,
                    account_number_pos_6 INT NOT NULL,
                    account_number_pos_7 INT NOT NULL,
                    account_number_pos_8 INT NOT NULL,
                    exception VARCHAR(10)
                )
            """)
        self.db.conn.executescript("""
                DROP TABLE IF EXISTS vocalink_sort_code_substitutions;

                CREATE TABLE vocalink_sort_code_substitutions (
                    original_sort_code VARCHAR(10) NOT NULL,
                    substituted_sort_code VARCHAR(10) NOT NULL
                )
            """)
        self.db.commit()



