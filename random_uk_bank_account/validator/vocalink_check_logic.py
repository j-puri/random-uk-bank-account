from random_uk_bank_account.vocalink.vocalink_model import VocalinkRule, VocalinkModulusAlgorithms


class ConditionalVocalinkCheckLogic:

    def __init__(
            self,
            sort_code_array,
            sort_code_sum,
            account_number_array,
            account_number_sum,
            rule: VocalinkRule):
        self.sort_code_array = sort_code_array
        self.sort_code_sum = sort_code_sum
        self.account_number_array = account_number_array
        self.account_number_sum = account_number_sum
        self.rule = rule

    def _modulus(self) -> int:
        return divmod(self.sort_code_sum + self.account_number_sum, self.rule.algorithm.modulus)[1]

    def check_for_vocalink_standard(self) -> bool:
        return self._modulus() == 0

    def check_for_vocalink_exception_1(self) -> bool:
        return divmod(self.sort_code_sum + self.account_number_sum + 27, self.rule.algorithm.modulus)[1] == 0

    def check_for_vocalink_exception_3(self) -> bool:
        if self.account_number_array[2] in [6, 9]:
            return True
        else:
            return self._modulus() == 0

    def check_for_vocalink_exception_4(self) -> bool:
        check_digit = int(''.join(str(digit) for digit in self.account_number_array[6:]))
        return self._modulus() == check_digit

    def check_for_vocalink_exception_5(self) -> bool:
        remainder = self._modulus()

        if self.rule.algorithm != VocalinkModulusAlgorithms.DBLAL:
            checkdigit = self.account_number_array[6]
            if remainder == 0 and checkdigit == 0:
                return True
            elif remainder == 1:
                return False
            elif 11 - remainder == checkdigit:
                return True
            else:
                return False
        else:
            checkdigit = self.account_number_array[7]
            if remainder == 0 and checkdigit == 0:
                return True
            else:
                return 10 - remainder == checkdigit

    def check_for_vocalink_exception_6(self) -> bool:
        if self._modulus() == 0:
            return True
        elif self.account_number_array[0] in [4, 5, 6, 7, 8] and self.account_number_array[6] == \
                self.account_number_array[7]:
            return True
        else:
            return False
