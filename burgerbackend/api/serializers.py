from rest_framework import serializers
from .models import CustomerDetail, Ingredient, Order, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
        'input_type': 'password'
    })
    class Meta:
        model = User
        fields = ['id', 'email', 'password', ]
        
    
    def create(self, validated_data):
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_user(email, password)
        return user

    
    
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'
        
class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = '__all__'
  
  
    
class OrderSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer()
    customer = CustomerDetailSerializer()

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        customer_data = validated_data.pop('customer')

        # Create ingredients instance
        ingredients_instance = Ingredient.objects.create(**ingredients_data)

        # Create customer detail instance
        customer_instance = CustomerDetail.objects.create(**customer_data)

        # Create order instance
        order = Order.objects.create(
            ingredients=ingredients_instance,
            customer=customer_instance,
            **validated_data
        )
        return order

