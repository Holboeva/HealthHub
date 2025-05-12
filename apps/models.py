from django.contrib.auth.models import AbstractUser
from django.db.models import (
    Model, CharField, ForeignKey, CASCADE, ImageField,
    DateTimeField, SlugField, TextField, BooleanField,
    EmailField, IntegerField
)

class User(AbstractUser):
    pass

class Category(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=255)

    def __str__(self):
        return self.name

class Course(Model):
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    duration = CharField(max_length=255)
    participant = CharField(max_length=255)
    category = ForeignKey(Category, CASCADE, related_name='courses')

    def __str__(self):
        return self.name

class Order(Model):
    user = ForeignKey(User, CASCADE)
    course = ForeignKey(Course, CASCADE)
    date_ordered = DateTimeField(auto_now_add=True)
    is_paid = BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"

class BlogPost(Model):
    title = CharField(max_length=200)
    slug = SlugField(unique=True)
    author = ForeignKey(User, CASCADE, null=True)
    content = TextField()
    image = ImageField(upload_to='blog/', null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ContactMessage(Model):
    name = CharField(max_length=100)
    email = EmailField()
    phone = CharField(max_length=15)  # <-- fixed
    message = TextField()
    sent_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class About(Model):
    title = CharField(max_length=200)
    content = TextField()
    image = ImageField(upload_to='about/', blank=True, null=True)
    last_updated = DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Recipe(Model):
    title = CharField(max_length=200)
    slug = SlugField(unique=True)
    ingredients = TextField()
    instructions = TextField()
    prep_time = IntegerField(help_text="Preparation time in minutes")
    calories = IntegerField(null=True, blank=True)
    image = ImageField(upload_to='recipes/')
    created_at = DateTimeField(auto_now_add=True)
    is_vegan = BooleanField(default=False)

    def __str__(self):
        return self.title
