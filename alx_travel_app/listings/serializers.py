from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Listing, Booking, Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ListingSerializer(serializers.ModelSerializer):
    host = UserSerializer(read_only=True)

    class Meta:
        model = Listing
        fields = [
            'property_id',
            'host',
            'name',
            'description',
            'location',
            'pricepernight',
            'created_at',
            'updated_at',
        ]


class BookingSerializer(serializers.ModelSerializer):
    property = ListingSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = [
            'booking_id',
            'property',
            'user',
            'start_date',
            'end_date',
            'total_price',
            'status',
            'created_at',
        ]


class ReviewSerializer(serializers.ModelSerializer):
    property = ListingSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            'review_id',
            'property',
            'user',
            'rating',
            'comment',
            'created_at',
        ]
