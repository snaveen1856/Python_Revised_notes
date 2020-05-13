"""
Singleton:
=========
In object-oriented programming, a singleton class is a class that can have only one object
(an instance of the class) at a time.
"""


class Only_Singleton(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class Singleton:
    __instance = None

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton.__instance = Singleton()
        return Singleton.__instance

    def __init__(self):
        try:
            if Singleton.__instance is not None:
                # raise Exception("This is a Singleton")
                raise Only_Singleton("This is a ****Singleton")
            else:
                Singleton.__instance = self
        except Exception as e:
            print(e)


s = Singleton()
print(s.get_instance())
x = Singleton()
