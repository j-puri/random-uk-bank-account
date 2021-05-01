from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from typing import List
from collections import namedtuple

VocalinkModulusAlgorithmType = namedtuple('VocalinkAlgorithmType', ['name', 'modulus'])


class VocalinkModulusAlgorithms:
    DBLAL = VocalinkModulusAlgorithmType('DBLAL', 10)
    MOD10 = VocalinkModulusAlgorithmType('MOD10', 10)
    MOD11 = VocalinkModulusAlgorithmType('MOD11', 11)

    @staticmethod
    def get(name):
        if name in VocalinkModulusAlgorithms().__dir__():
            return VocalinkModulusAlgorithms().__getattribute__(name)
        else:
            raise AttributeError(f"{name} is not an expected algorithm name.")


@dataclass_json
@dataclass()
class VocalinkRule:
    sort_code_from: str
    sort_code_to: str
    algorithm: VocalinkModulusAlgorithmType
    sort_code_pos_1: int
    sort_code_pos_2: int
    sort_code_pos_3: int
    sort_code_pos_4: int
    sort_code_pos_5: int
    sort_code_pos_6: int
    account_number_pos_1: int
    account_number_pos_2: int
    account_number_pos_3: int
    account_number_pos_4: int
    account_number_pos_5: int
    account_number_pos_6: int
    account_number_pos_7: int
    account_number_pos_8: int
    exception: int = 0

    def __post_init__(self):
        if isinstance(self.algorithm, str):
            self.algorithm = VocalinkModulusAlgorithms.get(self.algorithm)

    def to_ordered_tuple(self):
        return (
            self.sort_code_from,
            self.sort_code_to,
            self.algorithm.name,
            self.sort_code_pos_1,
            self.sort_code_pos_2,
            self.sort_code_pos_3,
            self.sort_code_pos_4,
            self.sort_code_pos_5,
            self.sort_code_pos_6,
            self.account_number_pos_1,
            self.account_number_pos_2,
            self.account_number_pos_3,
            self.account_number_pos_4,
            self.account_number_pos_5,
            self.account_number_pos_6,
            self.account_number_pos_7,
            self.account_number_pos_8,
            self.exception
        )

    def account_number_weight_array(self):
        return [
            self.account_number_pos_1,
            self.account_number_pos_2,
            self.account_number_pos_3,
            self.account_number_pos_4,
            self.account_number_pos_5,
            self.account_number_pos_6,
            self.account_number_pos_7,
            self.account_number_pos_8
        ]

    def sort_code_weight_array(self):
        return [
            self.sort_code_pos_1,
            self.sort_code_pos_2,
            self.sort_code_pos_3,
            self.sort_code_pos_4,
            self.sort_code_pos_5,
            self.sort_code_pos_6
        ]


@dataclass_json()
@dataclass()
class VocalinkRuleCollection:
    rules: List[VocalinkRule] = field(default_factory=lambda: [])

    def to_ordered_tuple_list(self):
        return [rule.to_ordered_tuple() for rule in self.rules]


@dataclass_json()
@dataclass
class VocalinkSortCodeSubstitution:
    original_sort_code: str = None
    substituted_sort_code: str = None

    def to_ordered_tuple(self):
        return (
            self.original_sort_code,
            self.substituted_sort_code
        )


@dataclass_json()
@dataclass
class VocalinkSortCodeSubstitutionCollection:
    substitutions: List[VocalinkSortCodeSubstitution] = field(default_factory=lambda: [])

    def to_ordered_tuple_list(self):
        return [substitutions.to_ordered_tuple() for substitutions in self.substitutions]


class VocalinkArrayMap:
    SORT_CODE_FROM = 0
    SORT_CODE_TO = 1
    ALGORITHM = 2
    SORT_CODE_RULE_1 = 3
    SORT_CODE_RULE_2 = 4
    SORT_CODE_RULE_3 = 5
    SORT_CODE_RULE_4 = 6
    SORT_CODE_RULE_5 = 7
    SORT_CODE_RULE_6 = 8
    ACCOUNT_NUMBER_RULE_1 = 9
    ACCOUNT_NUMBER_RULE_2 = 10
    ACCOUNT_NUMBER_RULE_3 = 11
    ACCOUNT_NUMBER_RULE_4 = 12
    ACCOUNT_NUMBER_RULE_5 = 13
    ACCOUNT_NUMBER_RULE_6 = 14
    ACCOUNT_NUMBER_RULE_7 = 15
    ACCOUNT_NUMBER_RULE_8 = 16
    EXCEPTION = 17
