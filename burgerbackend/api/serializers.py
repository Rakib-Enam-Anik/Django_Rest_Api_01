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
        

def create(self, validate_data):
    ingredient = validate_data['ingredients']
    customer = validate_data['customer']
    price = validate_data['price']
    orderTime = validate_data['orderTime']
    user = validate_data['user']
    order = Order.objects.update_or_create(
        ingredients = IngredientSerializer.create(IngredientSerializer(), ingredient),
        customer = CustomerDetailSerializer.create(CustomerDetailSerializer, customer),
        orderTime = orderTime,
        price = price,
        user = user
    )
    return order 
