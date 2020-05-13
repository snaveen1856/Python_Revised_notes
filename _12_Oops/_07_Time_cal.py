class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h}:{self.m}:{self.s}"

    @staticmethod
    def is_Vaild_Time(h, m, s):
        if h < 0 or h > 23:
            return False
        if m < 0 or m > 59:
            return False
        if s < 0 or s > 59:
            return False
        return True

    @classmethod
    def create_Time(cls, h, m, s):
        if Time.is_Vaild_Time(h, m, s):
            return cls(h, m, s)
        else:
            return None

    @property
    def total_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    @total_seconds.setter
    def total_seconds(self, value):
        self.h = value // 3600
        value = value % 3600
        self.m = value // 60
        self.s = value % 60


t = Time.create_Time(19, 56, 18)
print(t)
print(t.total_seconds)
t.total_seconds = 74578
print(t)
