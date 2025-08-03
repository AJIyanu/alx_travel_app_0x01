import os
import django
import random
import uuid
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from app.models import Listing, Booking, Review  # Replace `app` with your actual app name

# Optional: clear previous data (CAUTION in production)
Review.objects.all().delete()
Booking.objects.all().delete()
Listing.objects.all().delete()
User.objects.exclude(is_superuser=True).delete()

# Create sample users
users = []
for i in range(5):
    user = User.objects.create_user(
        username=f'user{i+1}',
        email=f'user{i+1}@example.com',
        password='testpassword123'
    )
    users.append(user)

# Create sample listings
listings = []
locations = ['Lagos', 'Abuja', 'Ibadan', 'Port Harcourt', 'Enugu']
for i in range(5):
    listing = Listing.objects.create(
        property_id=uuid.uuid4(),
        host=random.choice(users),
        name=f'Property {i+1}',
        description='A nice and cozy place to stay.',
        location=random.choice(locations),
        pricepernight=random.randint(5000, 20000),
    )
    listings.append(listing)

# Create sample bookings
statuses = ['pending', 'confirmed', 'canceled']
for i in range(10):
    property_obj = random.choice(listings)
    user = random.choice(users)
    start_date = datetime.today().date() + timedelta(days=random.randint(1, 30))
    end_date = start_date + timedelta(days=random.randint(1, 7))
    nights = (end_date - start_date).days
    total_price = property_obj.pricepernight * nights

    Booking.objects.create(
        booking_id=uuid.uuid4(),
        property=property_obj,
        user=user,
        start_date=start_date,
        end_date=end_date,
        total_price=total_price,
        status=random.choice(statuses)
    )

# Create sample reviews
for i in range(10):
    property_obj = random.choice(listings)
    user = random.choice(users)
    rating = random.randint(1, 5)
    comment = f"This is a review with rating {rating} for {property_obj.name}."

    Review.objects.create(
        review_id=uuid.uuid4(),
        property=property_obj,
        user=user,
        rating=rating,
        comment=comment
    )

print("✅ Database seeded with sample data.")
