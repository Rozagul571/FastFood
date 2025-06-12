from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import CharField, EmailField, TextChoices

class CustomUserManager(UserManager):
    def _create_user(self, phone_number, email, password, **extra_fields):
        if not phone_number:
            raise ValueError("The given phone_number must be set")
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, email, password, **extra_fields)

    def create_superuser(self, phone_number, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone_number, email, password, **extra_fields)

class User(AbstractUser):
    class RoleType(TextChoices):
        ADMIN = "admin", "Admin"
        WAITER = "waiter", "Waiter"
        USER = "user", "User"
    role = CharField(max_length=10, choices=RoleType.choices, default=RoleType.USER)
    email = EmailField(unique=True)
    # password = CharField(max_length=255)
    phone_number = CharField(max_length=11, unique=True)
    language = CharField(max_length=10, default='uz')

    objects = CustomUserManager()
    USERNAME_FIELD = 'phone_number'
    username = None
    REQUIRED_FIELDS = ['email']