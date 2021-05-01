from random_uk_bank_account.vocalink.vocalink_model import VocalinkRuleCollection, VocalinkModulusAlgorithmType, \
    VocalinkRule, VocalinkModulusAlgorithms

VOCALINK_RULE_COLLECTION_SINGLE_RULE = VocalinkRuleCollection(
    rules=[
        VocalinkRule(
            sort_code_from="040004",
            sort_code_to="040004",
            algorithm=VocalinkModulusAlgorithms.DBLAL,
            sort_code_pos_1=0,
            sort_code_pos_2=0,
            sort_code_pos_3=0,
            sort_code_pos_4=0,
            sort_code_pos_5=0,
            sort_code_pos_6=0,
            account_number_pos_1=8,
            account_number_pos_2=7,
            account_number_pos_3=6,
            account_number_pos_4=5,
            account_number_pos_5=4,
            account_number_pos_6=3,
            account_number_pos_7=2,
            account_number_pos_8=1,
            exception=-1
        )
    ]
)

VOCALINK_RULE_COLLECTION_SINGLE_RULE_UNHANDLED_EXCEPTION_CODE = VocalinkRuleCollection(
    rules=[
        VocalinkRule(
            sort_code_from="040004",
            sort_code_to="040004",
            algorithm=VocalinkModulusAlgorithms.DBLAL,
            sort_code_pos_1=0,
            sort_code_pos_2=0,
            sort_code_pos_3=0,
            sort_code_pos_4=0,
            sort_code_pos_5=0,
            sort_code_pos_6=0,
            account_number_pos_1=8,
            account_number_pos_2=7,
            account_number_pos_3=6,
            account_number_pos_4=5,
            account_number_pos_5=4,
            account_number_pos_6=3,
            account_number_pos_7=2,
            account_number_pos_8=1,
            exception=200
        )
    ]
)


VOCALINK_RULE_COLLECTION_NO_RULE = VocalinkRuleCollection(
    rules=[]
)