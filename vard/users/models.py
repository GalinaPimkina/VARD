from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None, **kwargs):
        if not email:
            raise ValueError("Поле Email не должно быть пустым!")

        user = self.model(
            name=name, email=self.normalize_email(email), password=password, **kwargs
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email=email, password=password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(blank=None, max_length=255)
    email = models.EmailField(unique=True, max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_password_change = models.DateTimeField(auto_now=True)
    password = models.CharField(_("password"), max_length=255)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Access(models.Model):
    user_id = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name='access')
    file_id = models.ForeignKey(to="Files", on_delete=models.CASCADE, related_name='access_file')
    access_type_id = models.ForeignKey(to="AccessType", on_delete=models.CASCADE, related_name='access_type')
    date_access_open = models.DateTimeField(auto_now=True)
    date_access_close = models.DateTimeField(blank=True, null=True)


class AccessType(models.Model):
    ACCESS_TYPES = [
        ('RE', 'READER'),
        ('OW', 'OWNER'),
        ('CO', 'COMMENTATOR'),
        ('ED', 'EDITOR'),
    ]
    access_type = models.CharField(max_length=2, choices=ACCESS_TYPES, default='RE')


class Files(models.Model):
    user_id = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name='file')
    place_id = models.ForeignKey(to="Place", on_delete=models.CASCADE, related_name='file_place')
    type_id = models.ForeignKey(to="FilesType", on_delete=models.CASCADE, related_name='file_type')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)
    date_delete = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    PUBLISH = [
        (0, 'no'),
        (1, 'yes'),
    ]
    publish = models.CharField(max_length=1, choices=PUBLISH, default=0)


class FilesType(models.Model):
    FILES_TYPES = [
        ('CSV', 'CSV'),
        ('JSON', 'JSON'),
        ('EXCEL', 'EXCEL'),
        ('PDF', 'PDF'),
    ]
    files_type = models.CharField(max_length=10, choices=FILES_TYPES, default='JSON')


class Place(models.Model):
    TYPES = [
        ('CO', 'Community'),
        ('MY', 'My Files'),
    ]
    type = models.CharField(max_length=2, choices=TYPES, default='MY')


class Dushboards(models.Model):
    user_id = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name='dushboard')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)


class Charts(models.Model):
    user_id = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name='chart')
    date_creation = models.DateTimeField(auto_now_add=True)
    date_change = models.DateTimeField(auto_now=True)


class Feedback(models.Model):
    user_id = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name='feedback')
    date_creation = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255)
    description = models.TextField()


class Comments(models.Model):
    user_id = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name='comment')
    file_id = models.ForeignKey(to="Files", on_delete=models.CASCADE, related_name='comment_file')
    chart_id = models.ForeignKey(to="Charts", on_delete=models.CASCADE, related_name='comment_chart')
    dushboard_id = models.ForeignKey(to="Dushboards", on_delete=models.CASCADE, related_name='comment_dushboard')
    date_send = models.DateTimeField(auto_now_add=True)
    date_remove = models.DateTimeField(blank=True, null=True)
    date_delivery = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

class ReadComments(models.Model):
    user_id = models.ForeignKey(to="User", on_delete=models.CASCADE, related_name='read')
    comment_id = models.ForeignKey(to="Comments", on_delete=models.CASCADE, related_name='read_comment')
    date_reading = models.DateTimeField(blank=True, null=True)


