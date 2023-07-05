import uuid
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.db.models import Q
from django.db.models.query import QuerySet

# Create your models here.


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("You have not provided an email address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    profile_picture = models.ImageField(blank=True, null=True)
    first_name = models.CharField(max_length=255, default='', blank=True)
    last_name = models.CharField(max_length=255, default='', blank=True)
    username = models.CharField(max_length=255, default='', blank=True)
    email = models.EmailField(max_length=255, default='', unique=True)
    bio = models.TextField(blank=True, null=True)
    gitHub = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    created_on = models.DateTimeField(default=timezone.now)
    updated_on = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class Course(models.Model):
    title = models.CharField(max_length=255)
    what_you_learn = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    targeted_audience = models.TextField(null=True, blank=True)
    instructor = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_in_minutes = models.PositiveIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Cartitems(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, blank=True, null=True)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, blank=True, null=True, related_name='cartitems')
    quantity = models.IntegerField(default=0)


class Enrollment(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Enrolled at {self.course}"


class Review(models.Model):
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} reviewed {self.course}"


class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title
