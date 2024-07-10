import datetime
from mptt.models import MPTTModel, TreeForeignKey

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from common.utils import validate_phone_number
from clinics.models import Specialist

class ServiceCategory(MPTTModel):
    title = models.CharField(_("title"), max_length=100)
    order = models.IntegerField(_("order"), default=0)

    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='children')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Service Category")
        verbose_name_plural = _("Service Categories")
        ordering = ['order']

    class MPTTMeta:
        order_insertion_by = ['title']


class Service(models.Model):
    title = models.CharField(_("title"), max_length=100)
    subtitle = models.CharField(_("subtitle"), max_length=100)
    image = models.ForeignKey('common.Media',
                              on_delete=models.CASCADE,
                              verbose_name=_("image"))
    for_what = models.CharField(_("for what"), max_length=100)
    short_desc = models.TextField(_("short description"))
    desc = models.TextField(_("description"))
    price = models.IntegerField(_("price"))
    category = models.ForeignKey(ServiceCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name=_('category'),
                                 related_name='services')
    is_home_page = models.BooleanField(_("is home page"), default=False,
                                       unique=True)
    gif = models.ForeignKey('common.Media',
                            on_delete=models.CASCADE,
                            verbose_name=_("gif"),
                            related_name='service_gif')

    class Meta:
        verbose_name = _("service")
        verbose_name_plural = _("services")

    def __str__(self):
        return self.title


class ServiceImage(models.Model):
    image = models.ForeignKey('common.Media',
                              on_delete=models.CASCADE,
                              verbose_name=_("image"))
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                verbose_name=_("service"),
                                related_name="images")

    class Meta:
        verbose_name = _("service image")
        verbose_name_plural = _("service images")

    def __str__(self):
        return f"Id: {self.id}| Service: {self.service.title}"


class Characteristic(models.Model):
    title = models.CharField(_("title"), max_length=100)
    value = models.CharField(_("value"), max_length=100)
    service = models.ForeignKey(Service,
                                on_delete=models.CASCADE,
                                verbose_name=_("service"),
                                related_name="characteristics")

    class Meta:
        verbose_name = _("characteristic")
        verbose_name_plural = _("characteristics")

    def __str__(self):
        return self.title


class ProcedureCost(models.Model):
    title = models.CharField(_("title"), max_length=100)
    price = models.CharField(_("price"), max_length=100)
    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                verbose_name=_("service"),
                                related_name='procedure_costs')

    class Meta:
        verbose_name = _("procedure cost")
        verbose_name_plural = _("procedure costs")


class WhoPerformsProcedure(models.Model):
    specialist = models.ForeignKey(Specialist,
                                   on_delete=models.CASCADE,
                                   verbose_name=_("specialist"),
                                   related_name='procedures')

    service = models.ForeignKey(Service, on_delete=models.CASCADE,
                                verbose_name=_("service"),
                                related_name='who_performs_procedures')

    class Meta:
        verbose_name = _("Specialist's service")
        verbose_name_plural = _("Specialist's services")

    def __str__(self):
        return f"Id: {self.id} - Specialist: {self.specialist.full_name} - Service: {self.service.title}"


class OrderService(models.Model):
    class OrderStatus(models.TextChoices):
        NEW = 'new', _('new')
        ACCEPTED = 'accepted', _('accepted')
        PROGRESS = 'progress', _('progress')
        CANCELED = 'canceled', _('canceled')
        FINISHED = 'finished', _('finished')

    phone = models.CharField(_("Phone"), max_length=100, validators=[
        validate_phone_number
    ])
    full_name = models.CharField(_("full name"), max_length=100)
    book_date = models.DateField(_("book date"))
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=_("service"))
    status = models.CharField(_("status"), max_length=100,
                              choices=OrderStatus.choices,
                              default=OrderStatus.NEW)

    class Meta:
        verbose_name = _("order service")
        verbose_name_plural = _("order services")

    def __str__(self):
        return self.full_name

    def clean(self):
        if self.book_date < datetime.date.today():
            raise ValidationError(_("Book date must be greater than today"))

