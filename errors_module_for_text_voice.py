class TextInvalidValue(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "Invalid text value: NULL"