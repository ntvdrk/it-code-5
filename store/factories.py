import factory
from factory.django import ImageField

from store import models


class StoryFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('description')
    price = factory.Faker(provider='price' )
    class Meta:
        model =models.store
        
    