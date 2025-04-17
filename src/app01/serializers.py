from rest_framework import serializers
from  .models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ('id', 'title', 'description', 'tecnology', 'craeted_at')
        read_only_fields = ('id', 'craeted_at')