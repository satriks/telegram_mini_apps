from rest_framework import serializers
from .models import State

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = [ 'pk', 'tg_name', 'created', 'updated', 'data']


    def update(self, instance, validated_data):
        instance.tg_name = validated_data.get('tg_name', instance.tg_name)
        instance.data = validated_data.get('data', instance.data)
        instance.save()
        return instance