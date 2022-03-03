# model.py
from dateutil.utils import today
from django.contrib.admin import models
from django.forms import fields


class Exchange_rate(models.Model):
    date = models.fields.Datetime()
    data = models.fields.Text()

    @classmethod
    def object(cls):
        pass


# url.py

# path('', views.convert)

# views.py

class Convert_curr(object):
    def __init__(self, url=None):
        self.data = Exchange_rate.object().filter(today)
        self.currany = self.data['rate']

    def convert(self, frm_curr, to_curr, amt):
        # bussiness
        return amt
