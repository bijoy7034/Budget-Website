from rest_framework import serializers
from ...models import IncomeSource

class IncomeSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeSource
        fields = ['user', 'source_name', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at',  'user']
    
    
    
