import uuid
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import AppUserManager

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_id/<filename>
    return '{0}/{1}'.format(instance.email, filename)

class User(AbstractUser):
    # fields removed from base user model
    first_name = None
    last_name = None
    username = None

    SEX_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    slug = models.SlugField(unique=True, default=uuid.uuid1, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField('full name', max_length=255)
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES, null=True, blank=True)
    photo = models.ImageField(upload_to=user_directory_path, blank=True)
    is_professional = models.BooleanField('professional status', default=False)
    is_employer = models.BooleanField('employer status', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AppUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    @property
    def notification_group(self):
        return f"notify_{self.slug}"

    def __str__(self):
        return self.email

