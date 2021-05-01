from random_uk_bank_account.vocalink.vocalink_model import \
    (VocalinkRuleCollection, VocalinkRule, VocalinkModulusAlgorithms, VocalinkModulusAlgorithmType,
     VocalinkSortCodeSubstitution)
from random_uk_bank_account.validator.vocalink_check_logic import ConditionalVocalinkCheckLogic


class ModulusChecker:

    def __init__(self, vocalink_rules: VocalinkRuleCollection, substitution: VocalinkSortCodeSubstitution):
        self.vocalink_rules = vocalink_rules
        self.sort_code_substitutions = substitution
        self.exception_2_and_9 = sorted([rule.exception for rule in vocalink_rules.rules]) == ["2", "9"]
        self.exception_10_and_11 = sorted([rule.exception for rule in vocalink_rules.rules]) == ["10", "11"]
        self.exception_12_and_13 = sorted([rule.exception for rule in vocalink_rules.rules]) == ["12", "13"]
        self.exception_14 = sorted([rule.exception for rule in vocalink_rules.rules]) == ["14"]
        self.exception_14b = False

    def are_vocalink_rules_applied(self, account_array: [], sort_code_array: []):
        rules_to_satisfy = len(self.vocalink_rules.rules)

        check_one = self._mod_check_for_algorithm(account_array, sort_code_array, self.vocalink_rules.rules[0])

        if rules_to_satisfy == 1:
            if self.exception_14:
                self.exception_14b = True
                return self._mod_check_for_algorithm(account_array, sort_code_array, self.vocalink_rules.rules[0])
            else:
                return check_one

        if rules_to_satisfy == 2:
            check_two = self._mod_check_for_algorithm(account_array, sort_code_array, self.vocalink_rules.rules[1])

            if self.exception_2_and_9:
                if check_one:
                    return True
                elif check_two:
                    return True
                else:
                    return False
            if self.exception_10_and_11 or self.exception_12_and_13:
                return check_one or check_two
            else:
                return check_one and check_two
        else:
            raise Exception("Unexpected number of Vocalink rules provided.")

    def _mod_check_for_algorithm(self, account_number_array: [], sort_code_array: [], rule: VocalinkRule) -> bool:

        if self.exception_2_and_9:
            if rule.exception == '9':
                sort_code_array = [3, 0, 9, 6, 3, 4]

            rule = VocalinkExceptionHandling.handle_exception_2_and_9(
                rule=rule, account_number=account_number_array)

        if rule.exception == '5' and self.sort_code_substitutions.original_sort_code:
            sort_code_array = [int(digit) for digit in list(self.sort_code_substitutions.substituted_sort_code)]

        if rule.exception == '7':
            rule = VocalinkExceptionHandling.handle_exception_7(
                rule=rule, account_number=account_number_array
            )

        if rule.exception == '8':
            sort_code_array = [0, 9, 0, 1, 2, 6]

        if rule.exception == '10':
            rule = VocalinkExceptionHandling.handle_exception_10(
                rule=rule, account_number=account_number_array
            )

        if self.exception_14b:
            account_number_array = VocalinkExceptionHandling.handle_exception_14b(
                account_number=account_number_array
            )

        weighted_sort_code = self._get_weighted_array(sort_code_array, rule.sort_code_weight_array())
        weighted_account_number = self._get_weighted_array(account_number_array, rule.account_number_weight_array())

        sort_code_sum = self._array_sum_for_algorithm(
            algorithm=rule.algorithm, array_to_calculate=weighted_sort_code)
        account_number_sum = self._array_sum_for_algorithm(
            algorithm=rule.algorithm, array_to_calculate=weighted_account_number)

        check_logic = ConditionalVocalinkCheckLogic(
            sort_code_array=sort_code_array,
            sort_code_sum=sort_code_sum,
            account_number_array=account_number_array,
            account_number_sum=account_number_sum,
            rule=rule
        )

        if rule.exception == '1':
            return check_logic.check_for_vocalink_exception_1()

        elif rule.exception == '3':
            return check_logic.check_for_vocalink_exception_3()

        elif rule.exception == '4':
            return check_logic.check_for_vocalink_exception_4()

        elif rule.exception == '5':
            return check_logic.check_for_vocalink_exception_5()

        elif rule.exception == '6':
            return check_logic.check_for_vocalink_exception_6()

        else:
            return check_logic.check_for_vocalink_standard()

    def _modulus(self, sort_code_sum: int, account_number_sum, rule: VocalinkRule):
        return divmod(sort_code_sum + account_number_sum, rule.algorithm.modulus)[1]

    def _array_sum_for_algorithm(self, algorithm: VocalinkModulusAlgorithmType, array_to_calculate: []):
        if algorithm.name == VocalinkModulusAlgorithms.DBLAL.name:
            """
            DBLAL - sum of the individual digits of array. I.e. If array = [10, 15, 20], then array
            sum will be 1+0+1+5+2+0
            """
            return sum([int(digit) for digit in ''.join(str(number) for number in array_to_calculate)])
        else:
            return sum(array_to_calculate)

    def _get_weighted_array(self, array_to_weight: [], weights: []):
        if len(array_to_weight) != len(weights):
            raise ValueError("array_to_weight is not the same length as weights.")
        else:
            return [
                int(number) * int(weight) for number, weight in zip(array_to_weight, weights)
            ]


class VocalinkExceptionHandling:

    @staticmethod
    def handle_exception_2_and_9(rule: VocalinkRule, account_number: [int]) -> VocalinkRule:
        if account_number[0] != 0 and rule.exception == '2':
            if account_number[6] != 9:
                rule.sort_code_pos_1 = 0
                rule.sort_code_pos_2 = 0
                rule.sort_code_pos_3 = 1
                rule.sort_code_pos_4 = 2
                rule.sort_code_pos_5 = 5
                rule.sort_code_pos_6 = 3
                rule.account_number_pos_1 = 6
                rule.account_number_pos_2 = 4
                rule.account_number_pos_3 = 8
                rule.account_number_pos_4 = 7
                rule.account_number_pos_5 = 10
                rule.account_number_pos_6 = 9
                rule.account_number_pos_7 = 3
                rule.account_number_pos_8 = 1
            else:
                rule.sort_code_pos_1 = 0
                rule.sort_code_pos_2 = 0
                rule.sort_code_pos_3 = 0
                rule.sort_code_pos_4 = 0
                rule.sort_code_pos_5 = 0
                rule.sort_code_pos_6 = 0
                rule.account_number_pos_1 = 0
                rule.account_number_pos_2 = 0
                rule.account_number_pos_3 = 8
                rule.account_number_pos_4 = 7
                rule.account_number_pos_5 = 10
                rule.account_number_pos_6 = 9
                rule.account_number_pos_7 = 3
                rule.account_number_pos_8 = 1

        return rule

    @staticmethod
    def handle_exception_7(rule: VocalinkRule, account_number: [int]) -> VocalinkRule:
        if account_number[6] == 9:
            rule.sort_code_pos_1 = 0
            rule.sort_code_pos_2 = 0
            rule.sort_code_pos_3 = 0
            rule.sort_code_pos_4 = 0
            rule.sort_code_pos_5 = 0
            rule.sort_code_pos_6 = 0
            rule.account_number_pos_1 = 0
            rule.account_number_pos_2 = 0

        return rule

    @staticmethod
    def handle_exception_10(rule: VocalinkRule, account_number: [int]) -> VocalinkRule:
        if (account_number[0] == 0 and account_number[1] == 9) \
                or (account_number[0] == account_number[1] == account_number[6] == 9):
            rule.sort_code_pos_1 = 0
            rule.sort_code_pos_2 = 0
            rule.sort_code_pos_3 = 0
            rule.sort_code_pos_4 = 0
            rule.sort_code_pos_5 = 0
            rule.sort_code_pos_6 = 0
            rule.account_number_pos_1 = 0
            rule.account_number_pos_2 = 0
        return rule

    @staticmethod
    def handle_exception_14b(account_number: [int]):
        if account_number[7] in [0, 1, 9]:
            account_number.pop(7)
            account_number.insert(0,0)
        return account_number
