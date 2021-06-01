from django.db.models import fields
from rest_framework import serializers
from .models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # field=['name','age']
        fields = '__all__'
        # exclude = ['id']

    def validate(self, data):
        if data['age'] < 18:
            raise serializers.ValidationError({'error': 'age is less than 18'})

        if data['name']:
            for n in data['name']:
                if n.isdigit():
                    raise serializers.ValidationError(
                        {'error': 'name cannot contain numbers'})

        return data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        # field=['name','age']
        fields = '__all__'
        # exclude = ['id']


class BookSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = '__all__'
