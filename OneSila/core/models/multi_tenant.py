from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from core.validators import phone_regex


class MultiTenantCompany(models.Model):
    '''
    Class that holds company information and sales-conditions.
    '''
    from core.countries import COUNTRY_CHOICES
    from core.helpers import get_languages

    LANGUAGE_CHOICES = get_languages()

    name = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100, null=True, blank=True)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    postcode = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=3, choices=COUNTRY_CHOICES, null=True, blank=True)
    language = models.CharField(max_length=7, choices=LANGUAGE_CHOICES, default=settings.LANGUAGE_CODE)

    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    vat_number = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = _("Multi tenant companies")


class MultiTenantAwareMixin(models.Model):
    multi_tenant_company = models.ForeignKey(MultiTenantCompany, on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        abstract = True


class MultiTenantMultiAwareMixin(models.Model):
    multi_tenant_company = models.ManyToManyField(MultiTenantCompany)

    class Meta:
        abstract = True


class MultiTenantUser(AbstractUser, MultiTenantAwareMixin):
    '''
    Q: Why is this user-class abusing the username as an email-field instead of just
    changing the class?
    A: Because starwberry-django will break and rewriting this field is not something
    that's in the cards today.
    '''
    username = models.EmailField(unique=True, help_text=_('Email Address'))

    def __str__(self):
        return f"{self.username} <{self.multi_tenant_company}>"

    def save(self, *args, **kwargs):
        self.email = self.username

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("Multi tenant user")
        verbose_name_plural = _("Multi tenant users")

    # class Meta(AbstractUser.Meta):
    #     constraints = [
    #         CheckConstraint(
    #             check=Q(is_superuser=False, is_staff=False) ^ Q(company=None),
    #             name='user_has_company_if_no_staff_admin',
    #             violation_error_message=_("Users need to have a company assign. Staff and Superusers cannot.")
    #         ),
    #     ]
