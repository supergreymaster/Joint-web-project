class InvalidValue(Exception):
    def __init__(self, *args):
        if args:
            if args[0] == 'text_error':
                self.message = 'Invalid text value: text value must not be NULL'
            elif args[0] == 'language_error':
                self.message = f'Invalid language value: {args[1]}'

    def __str__(self):
        return self.message
