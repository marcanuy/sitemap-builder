import factory
from random import random, randint

from . import models
from . import sitemap

class ItemFactory(factory.Factory):
    class Meta:
        model = models.Item

    loc = factory.Faker('uri')
    last_modification = factory.Faker('iso8601')
    change_frequency = factory.Iterator(models.CHANGE_FREQ) #factory.LazyFunction(lambda: list(models.CHANGE_FREQ))
    priority = round(random(),1)

class SitemapFactory(factory.Factory):
    class Meta:
        model = sitemap.Sitemap

    hostname = factory.Faker('url', schemes=['http', 'https'])

    @factory.post_generation
    def items(sitemap, create, extracted, **kwargs):
        """
        If called like: SitemapFactory(items=4) it generates a Sitemap
        with 4 Items.
        If called without `items` it generates a random amount of items
        """
        if not create:
            # Build, not create related
            return

        if extracted:
            for n in range(extracted):
                sitemap.add_item(ItemFactory())
        else:
            number_of_items = randint(1, 10)
            for n in range(number_of_items):
                sitemap.add_item(ItemFactory())
