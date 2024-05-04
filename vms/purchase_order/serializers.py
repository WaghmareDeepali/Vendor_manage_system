from rest_framework import serializers
from .models import PurchaseOrder



class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

    # Validates the quantity field
    def validate_quantity(self,value):
        if value <= 0:
            raise serializers.ValidationError('Quantity Cannot be less than 1')
        return value

    # Validates the status field
   
    def validate_quality_rating(self, value):
        if self.instance is not None:
            current_status = self.instance.status
            if current_status.lower() != 'completed':
                raise serializers.ValidationError('Cannot give Quality rating ')
        
        if value is not None and value not in range(1, 11):
            raise serializers.ValidationError('Quality Rating must be between 1 and 10')
    
        return value
