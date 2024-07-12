from functools import wraps
from deny_me.exceptions import PassowrdError, ProtectedError
# from sys import exit as __ex__

class Password:
    def __init__(self, password: str):
        self.__password = password
    
    def protected(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            password = kwargs.pop("password", None)
            if password != None:
                if password == self.__password:
                    return func(self, *args, **kwargs)
                else:
                    raise PassowrdError("Wrong Password provided for an exclusive function.")
            else:
                raise ProtectedError("This function is not available.")