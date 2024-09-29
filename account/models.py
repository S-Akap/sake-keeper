from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields['is_active'] = True
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self._create_user(
            email=email,
            username=username,
            password=password,
            **extra_fields,
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name="username",
        unique=True,
        max_length=20
    )
    email = models.EmailField(
        verbose_name="email",
        unique=True
    )
    icon = models.ImageField(
        verbose_name="icon",
        upload_to="",
        null=True,
        blank=True
    )
    is_superuser = models.BooleanField(
        verbose_name="is_superuer",
        default=False
    )
    is_staff = models.BooleanField(
        verbose_name='staff status',
        default=False,
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True,
    )
    created_at = models.DateTimeField(
        verbose_name="created_at",
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="updateded_at",
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

