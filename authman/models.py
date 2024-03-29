from django.contrib.auth.hashers import make_password
from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser
)
from django.contrib.auth.models import Group
from api.models import *

# Create your models here.


class EmailConfig(models.Model):
    from_email = models.EmailField(max_length=100)
    email_password = models.CharField(
        max_length=128, validators=[MinLengthValidator(8)])
    email_host = models.CharField(max_length=50, default="mail.tdbsoft.co.ke")
    email_port = models.CharField(max_length=5, default=465)
    use_tls = models.BooleanField(default=True)
    fail_silently = models.BooleanField(default=True)

    # def save(self, *args, **kwargs):
    #     self.email_password = make_password(self.email_password)
    #     super(EmailConfig, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.from_email

    class Meta:
        verbose_name_plural = 'Email Configuration'


class RoleScreens(models.Model):
    role_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    screens = models.TextField(
        max_length=2500, default="Dashboard,DataAlignment,IndicatorMappingRules,IndicatorComparison,DataQuality,Indicators,AllIndicators,Categories,Security,DataPullSchedule,Roles,Users,PasswordPolicy,Reports")
    counties = models.ManyToManyField(counties)
    facilities = models.ManyToManyField(Facilities)

    class Meta:
        db_table = 'role_screens'
        verbose_name_plural = 'Role Access'

    def __str__(self) -> str:
        return self.role_id.name + " metadata"

from django.contrib.auth.models import Group


class MyUser(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        unique=True,
    )
    phone = models.CharField(max_length=15)
    organisation = models.CharField(
        max_length=255, default='HealthIT', blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    is_active = models.BooleanField(default=False)

    # objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'first_name',
                       'last_name', 'email']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        # Hash the password before saving the user
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_staff
