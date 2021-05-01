from random_uk_bank_account.client.sqlite3 import SqlLite, SqlLiteUtilities


class VocalinkDataAccess:

    def __init__(self, DB_LOCATION: str):
        self.db = SqlLite(local_db=DB_LOCATION)

    @SqlLiteUtilities.return_rows_as_list_dict
    def get_rules_for_sort_code(self, sort_code: str):
        self.db.cur.execute(
            f"SELECT * FROM VOCALINK_RULES WHERE CAST(? AS INTEGER) "
            f"BETWEEN CAST(sort_code_from AS INTEGER) AND CAST(sort_code_to AS INTEGER)",
            [sort_code]

        )
        return self.db.cur


    @SqlLiteUtilities.return_rows_as_dict
    def get_sort_code_substitution(self, sort_code: str):
        self.db.cur.execute(
            f"SELECT original_sort_code, substituted_sort_code FROM vocalink_sort_code_substitutions WHERE original_sort_code = ?",
            [sort_code]
        )
        return self.db.cur

    @SqlLiteUtilities.return_rows_as_dict
    def get_all_sort_code_substitutions(self):
        self.db.cur.execute(
            f"SELECT original_sort_code, substituted_sort_code FROM vocalink_sort_code_substitutions",
        )
        return self.db.cur
