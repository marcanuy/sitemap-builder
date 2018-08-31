import factory
from random import random

from . import models

class ItemFactory(factory.Factory):
    class Meta:
        model = models.Item

    loc = factory.Faker('uri')
    last_modification = factory.Faker('iso8601')
    change_freq = factory.Iterator(models.CHANGE_FREQ) #factory.LazyFunction(lambda: list(models.CHANGE_FREQ))
    priority = round(random(),1)
