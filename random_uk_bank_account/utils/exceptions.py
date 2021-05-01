class VocalinkUnsupportedSortCodeError(Exception):
    def __init__(self, sort_code):
        super().__init__(f"Vocalink version does not support sort code: {sort_code}")


class UnsupportVocalinkException(Exception):
    def __init__(self, exception, sort_code):
        super().__init__(
            f"{sort_code} is a Vocalink exception algorithm {exception}. This is currently unsupported. "
            f"Raise a request with the application to add this exception into the account number "
            f"generator.")


class IncompatibleVocalinkVersion(Exception):
    def __init__(self, version):
        super().__init__(
            f"Unable to load Vocalink data. Please check data is available from {version}.")
