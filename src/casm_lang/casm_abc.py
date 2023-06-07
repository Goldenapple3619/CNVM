class Token:
    def __init__(self, keyword, value) -> None:
        self.keyword: str = keyword
        self.value = value

    def __repr__(self) -> str:
        return (self.keyword + ': ' + str(self.value))