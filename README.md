
# Random UK Bank Account

![main](https://github.com/j-puri/random-uk-bank-account/actions/workflows/python-test.yml/badge.svg)
![main](https://github.com/j-puri/random-uk-bank-account/actions/workflows/python-publish.yml/badge.svg) 
[![codecov](https://codecov.io/gh/j-puri/random-uk-bank-account/branch/main/graph/badge.svg?token=198PVGHJXA)](https://codecov.io/gh/j-puri/random-uk-bank-account)
[![PyPI version fury.io](https://badge.fury.io/py/random-uk-bank-account.svg)](https://pypi.org/project/random-uk-bank-account/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/random-uk-bank-account.svg)](https://pypi.python.org/pypi/random-uk-bank-account/)


A package to generate random test UK bank account numbers for a given UK sort code
which pass [Vocalink modulus checks](https://www.vocalink.com/tools/modulus-checking/).



## Install

    pip3 install random-uk-bank-account
    
    
## Usage

#### Generate Account Numbers

```python
from random_uk_bank_account import GenerateUkBankAccount
    
account = GenerateUkBankAccount().generate_for_sort_code('040004')
>> RandomBankAccount(sort_code='040004', account_numbers=['82965944'])

account.sort_code
>> '040004'

account.account_numbers
>> ['41066722']


GenerateUkBankAccount().generate_for_sort_code('040004', total=20)
>> RandomBankAccount(sort_code='040004', account_numbers=['92612857', '76448619', '09409980', '95576964', '76299182', '68185209', '44888939', '55332169', '50496590', '42464621', '38534657', '44047783', '91289609', '32162555', '71814032', '33956578', '22465479', '82075062', '16446077', '22058275'])

GenerateUkBankAccount().generate_for_sort_code('201053', total=5).to_json()
>> {"sort_code": "201053", "account_numbers": ["56990833", "67758799", "72576465", "02666758", "28778256"]}
```

#### Validate Account Numbers

```python
from random_uk_bank_account import GenerateUkBankAccount
    
GenerateUkBankAccount().validate(sort_code='040004', account_number='82965944')
>> True
```
    
#### Get Vocalink Rules
    
```python
from random_uk_bank_account import GenerateUkBankAccount
    
GenerateUkBankAccount().get_vocalink_rules(sort_code='040004')
>> VocalinkRuleCollection(rules=[VocalinkRule(sort_code_from='040004', sort_code_to='040004', algorithm=VocalinkAlgorithmType(name='DBLAL', modulus=10), sort_code_pos_1=0, sort_code_pos_2=0, sort_code_pos_3=0, sort_code_pos_4=0, sort_code_pos_5=0, sort_code_pos_6=0, account_number_pos_1=8, account_number_pos_2=7, account_number_pos_3=6, account_number_pos_4=5, account_number_pos_5=4, account_number_pos_6=3, account_number_pos_7=2, account_number_pos_8=1, exception='0')])

GenerateUkBankAccount().get_vocalink_rules(sort_code='040004').to_json()
>> {"rules": [{"sort_code_from": "040004", "sort_code_to": "040004", "algorithm": ["DBLAL", 10], "sort_code_pos_1": 0, "sort_code_pos_2": 0, "sort_code_pos_3": 0, "sort_code_pos_4": 0, "sort_code_pos_5": 0, "sort_code_pos_6": 0, "account_number_pos_1": 8, "account_number_pos_2": 7, "account_number_pos_3": 6, "account_number_pos_4": 5, "account_number_pos_5": 4, "account_number_pos_6": 3, "account_number_pos_7": 2, "account_number_pos_8": 1, "exception": "0"}]}
```


#### Get Vocalink Sort Code Substitutions

```python
from random_uk_bank_account import GenerateUkBankAccount
    
GenerateUkBankAccount().get_all_vocalink_substitutions()
GenerateUkBankAccount().get_all_vocalink_substitutions().to_json()

GenerateUkBankAccount().get_vocalink_substitution(sort_code='938628')
>> VocalinkSortCodeSubstitution(original_sort_code='938628', substituted_sort_code='938181')

GenerateUkBankAccount().get_vocalink_substitution(sort_code='938628').to_json()
>> {"original_sort_code": "938628", "substituted_sort_code": "938181"}
```

## Additional Options

#### Logging

By default logging is set to ERROR. To enable debug use `log_level`: 

```python
GenerateUkBankAccount(log_level=logging.DEBUG).generate_for_sort_code(sort_code='040004', total=5)
```
```
STDOUT >>
    2021-04-28 17:53:37,970 - random-bank-account - DEBUG - 4889/valacdos has been cached previously in /Users/{USER}/.vocalink
    2021-04-28 17:53:37,970 - random-bank-account - DEBUG - 1517/scsubtab has been cached previously in /Users/{USER}/.vocalink
    2021-04-28 17:53:37,971 - random-bank-account - DEBUG - Vocalink rules: {"rules": [{"sort_code_from": "040004", "sort_code_to": "040004", "algorithm": ["DBLAL", 10], "sort_code_pos_1": 0, "sort_code_pos_2": 0, "sort_code_pos_3": 0, "sort_code_pos_4": 0, "sort_code_pos_5": 0, "sort_code_pos_6": 0, "account_number_pos_1": 8, "account_number_pos_2": 7, "account_number_pos_3": 6, "account_number_pos_4": 5, "account_number_pos_5": 4, "account_number_pos_6": 3, "account_number_pos_7": 2, "account_number_pos_8": 1, "exception": "0"}]}
    2021-04-28 17:53:37,971 - random-bank-account - DEBUG - Vocalink sort code substitutions: {"original_sort_code": null, "substituted_sort_code": null}
    2021-04-28 17:53:37,972 - random-bank-account - DEBUG - Generating Bank Account for 040004. Seed array: [1, 6, 2, 6, 7, 7, 2, 1] 
    2021-04-28 17:53:37,972 - random-bank-account - DEBUG - Account Number [5, 6, 3, 6, 7, 7, 2, 1] satisfies checks after 5 numeric changes
    2021-04-28 17:53:37,972 - random-bank-account - DEBUG - 1/2 account numbers generated
    2021-04-28 17:53:37,972 - random-bank-account - DEBUG - Generating Bank Account for 040004. Seed array: [9, 0, 4, 3, 5, 0, 4, 5] 
    2021-04-28 17:53:37,972 - random-bank-account - DEBUG - Account Number [9, 1, 4, 6, 5, 0, 4, 5] satisfies checks after 4 numeric changes
    2021-04-28 17:53:37,972 - random-bank-account - DEBUG - 2/2 account numbers generated
```

#### Vocalink Caching
By default Vocalink data is retrieved from the Vocalink website and permanently cached in a sqlite database located in 
the home directory under the folder `.vocalink`.

The cache can be recreated with `recreate_vocalink_db`:

```python
GenerateUkBankAccount(log_level=logging.DEBUG, recreate_vocalink_db=True)
```
```
STDOUT >>
    2021-04-28 17:58:56,373 - random-bank-account - DEBUG - Deleting previously created /Users/{USER}/.vocalink/4889-valacdos.db
    2021-04-28 17:58:56,571 - random-bank-account - DEBUG - Vocalink data saved to /Users/{USER}/.vocalink/4889-valacdos.db
```
The location for the cache can be overwritten with `cache_location`:
```python
GenerateUkBankAccount(cache_location='some/real/path')
```

#### Vocalink Version
The version of Vocalink is defaulted to values in config. These are retrievable via:

```python
GenerateUkBankAccount().VOCALINK_VERSION
GenerateUkBankAccount().VOCALINK_SUBSTITUTION_VERSION
```
    
The version can be overwitten via `vocalink_rules_version` and `vocalink_substitution_version`. The values of which 
are taken from the Vocalink URLs shown in bold below.
<pre>
https://www.vocalink.com/media/<b>4941/valacdos</b>.txt
https://www.vocalink.com/media/<b>1517/scsubtab</b>.txt
</pre>
For example: 

```python
GenerateUkBankAccount(
    recreate_vocalink_db=True, 
    vocalink_rules_version='4941/valacdos', 
    vocalink_substitution_version='1517/scsubtab'
)
```

#### Tests
Clone the repository and run:

    make test