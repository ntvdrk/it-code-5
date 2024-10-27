from rest_framework import serializers
from store import models

class store(serializers.ModelSerializer):
    store_id = serializers.IntegerField(required = False, allow_null = True)
    price = serializers.SerializerMethodField()
    class Meta:
        model = models.store
        fields = "__all__"
        
    def get_price(self, obj):
        if models.Storage.objects.filter(store=obj).exists:
            return obj.storage.price
        return None