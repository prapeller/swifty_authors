from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    def validate_email(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        if not username:
            raise ValueError(_("You must provide a username"))

        if not first_name:
            raise ValueError(_("You must provide a first_name"))

        if not last_name:
            raise ValueError(_("You must provide a last_name"))

        if not email:
            raise ValueError(_("Base User Manager: An email is required"))
        user_email = self.normalize_email(email)
        self.validate_email(user_email)

        if not password:
            raise ValueError(_("Base User Manager: A password is required"))

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=user_email,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superusers must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superusers must have is_superuser=True"))

        superuser = self.create_user(username, first_name, last_name, email, password, **extra_fields)

        return superuser