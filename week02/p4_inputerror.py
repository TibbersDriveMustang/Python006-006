class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self, ErrorInfo)
        self.errorInfo = ErrorInfo

    def __str__(self):
        return self.errorInfo


userinput = 'a'

try:
    if not userinput.isdigit():
        raise UserInputError('User Input Error')
except UserInputError as ue:
    print(ue)
finally:
    del userinput
