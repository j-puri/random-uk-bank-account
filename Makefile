.PHONY: test

test:
	pip3 install -r requirements.txt
	pip3 install pytest pytest-cov pytest-mock requests_mock
	pytest --cov=random_uk_bank_account --cov-report=xml test/tests
