from rest_framework import serializers
from store import models

class store(serializers.ModelSerializer):
    class Meta:
        model = models.store
        fields = "__all__"