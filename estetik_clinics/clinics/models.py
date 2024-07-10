import datetime
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

from common.models import Media
from common.utils import validate_phone_number


class Vacancy(models.Model):
    title = models.CharField(max_length=120, verbose_name=_('title'))
    image = models.ForeignKey(Media,
                              on_delete=models.SET_NULL,
                              null=True, blank=True)
    responsibilities = RichTextField(verbose_name=_('responsibilities'))
    requirements = RichTextField(verbose_name=_('requirements'))
    conditions = RichTextField(verbose_name=_('conditions'))

    class Meta:
        verbose_name = _('vacancy')
        verbose_name_plural = _('vacancies')

    def __str__(self):
        return self.title


class Action(models.Model):
    title = models.CharField(_("title"), max_length=120)
    special_offer = models.BooleanField(_("special offer"), default=False)
    short_desc = models.TextField(_("short description"))
    desc = RichTextField(verbose_name=_("description"))
    expires_in = models.DateTimeField(_("expires in"), blank=False)
    percentage = models.PositiveSmallIntegerField(_("percentage"))
    tags = models.ManyToManyField("ActionTag", verbose_name=_("action tag"),
                                  blank=True)
    in_discount = models.BooleanField(_("in discount"), default=False)

    class Meta:
        verbose_name = _("action")
        verbose_name_plural = _("actions")

    def __str__(self):
        return self.title

    def clean(self):
        if self.expires_in < datetime.date.today():
            raise ValidationError(_("Expires date must be greater than today !"))


class ActionTag(models.Model):
    title = models.CharField(_("title"), max_length=120)

    class Meta:
        verbose_name = _("action tag")
        verbose_name_plural = _("action tags")

    def __str__(self):
        return self.title


class ActionImage(models.Model):
    action = models.ForeignKey(Action, on_delete=models.CASCADE,
                               verbose_name=_("action"),
                               related_name="action_images")
    image = models.ForeignKey(Media, on_delete=models.CASCADE,
                              verbose_name=_("image"))

    class Meta:
        verbose_name = _("action image")
        verbose_name_plural = _("action images")

    def __str__(self):
        return f"Action: {self.action}| ID: {self.id}"


class OnlineAppointment(models.Model):
    phone_number = models.CharField(_("phone number"), max_length=20)
    full_name = models.CharField(_("full name"), max_length=120)
    book_date = models.DateField(_("book date"))
    active = models.BooleanField(_("active"), default=True)

    class Meta:
        verbose_name = _("online appointment")
        verbose_name_plural = _("online appointments")

    def __str__(self):
        return self.full_name

    def clean(self):
        if self.book_date < datetime.date.today():
            raise ValidationError(_("Book date must be greater than today !"))


class AboutUs(models.Model):
    video = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name=_("video"))
    summary = RichTextField(_("summary"))

    class Meta:
        verbose_name = _("about us")
        verbose_name_plural = _("about us")

    def __str__(self):
        return self.summary


class PhotoGalleryCategory(models.Model):
    title = models.CharField(_("title"), max_length=120)

    def __str__(self):
        return self.title


class PhotoGallery(models.Model):
    photo = models.ForeignKey(Media, on_delete=models.CASCADE,
                              verbose_name=_("photo"))
    category = models.ForeignKey(PhotoGalleryCategory, on_delete=models.CASCADE,
                                 verbose_name=_("category"))

    class Meta:
        verbose_name = _("photo gallery")
        verbose_name_plural = _("photo galleries")

    def __str__(self):
        return f"ID: {self.id}| Category: {self.category}"


class License(models.Model):
    photo = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_("photo"))
    title = models.CharField(_("title"), max_length=120)

    class Meta:
        verbose_name = _("license")
        verbose_name_plural = _("licences")

    def __str__(self):
        return self.title


class ContactChiefDoctor(models.Model):
    phone_number = models.CharField(_("phone number"), max_length=20,
                                    validators=[validate_phone_number])
    full_name = models.CharField(_("full name"), max_length=120)
    message = models.TextField(_("message"))
    active = models.BooleanField(_("active"), default=True)

    class Meta:
        verbose_name = _("contact chief doctor")
        verbose_name_plural = _("contact chief doctors")

    def __str__(self):
        return self.full_name


class Specialist(models.Model):
    full_name = models.CharField(_("full name"), max_length=120)
    position = models.CharField(_("position"), max_length=120)
    about = RichTextField(_("about"))
    certificates = RichTextField(_("certificate"))
    photo = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    experience_in_company = models.CharField(_("experience in company"), max_length=10)
    experience_in_field = models.CharField(_("experience in field"), max_length=10)
    experience_in_years = models.CharField(_("experience in years"), max_length=10)

    class Meta:
        verbose_name = _("specialist")
        verbose_name_plural = _("specialists")

    def __str__(self):
        return self.full_name


class Diploma(models.Model):
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE,
                                   related_name="diplomas")
    file = models.ForeignKey(Media, on_delete=models.CASCADE, verbose_name=_("file"))

    class Meta:
        verbose_name = _("diploma")
        verbose_name_plural = _("diplomas")

    def __str__(self):
        return f"ID: {self.id}| Specialist: {self.specialist}"


class NewsCategory(models.Model):
    title = models.CharField(_("title"), max_length=120)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _("news category")
        verbose_name_plural = _("news categories")

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(_("title"), max_length=120)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    desc = RichTextField(_("text"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("created at"))
    special_offer = models.BooleanField(_("special offer"), default=False)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    tags = models.ManyToManyField("NewsTag", verbose_name=_("news tag"), blank=True)
    published = models.BooleanField(_("published"), default=False)

    class Meta:
        verbose_name = _("news")
        verbose_name_plural = _("news")

    def __str__(self):
        return self.title

class NewsTag(models.Model):
    title = models.CharField(_("title"), max_length=120)

    class Meta:
        verbose_name = _("news tag")
        verbose_name_plural = _("news tags")

    def __str__(self):
        return self.title

class Contacts(models.Model):
    address = models.CharField(_("address"), max_length=120)
    phone_number = models.CharField(_("phone number"), max_length=20,
                                    validators=[validate_phone_number])
    work_time = models.CharField(_("work time"), max_length=120)
    telegram = models.URLField(_("telegram"), validators=[RegexValidator(r'^https?:\/\/t\.me\/[A-Za-z0-9_]{5,}$')])
    instagram = models.URLField(_("instagram"),
                                validators=[RegexValidator(r'^https?:\/\/www\.instagram\.com\/[A-Za-z0-9_]{5,}$')])
    facebook = models.URLField(_("facebook"),
                               validators=[RegexValidator(r'^https?:\/\/www\.facebook\.com\/[A-Za-z0-9_]{5,}$')])
    vkontact = models.URLField(_("vkontact"), validators=[RegexValidator(r'^https?:\/\/vk\.com\/[A-Za-z0-9_]{5,}$')])
    location = models.URLField(_("location"))

    class Meta:
        verbose_name = _("Contacts")
        verbose_name_plural = _("Contacts")

    def __str__(self):
        return self.address

class ArticleCategory(models.Model):
    title = models.CharField(_("title"), max_length=120)

    class Meta:
        verbose_name = _("article category")
        verbose_name_plural = _("article categories")

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(_("title"), max_length=120)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    desc = RichTextField(_("description"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, related_name="articles")
    published = models.BooleanField(_("published"), default=False)

    class Meta:
        verbose_name = _("article")
        verbose_name_plural = _("articles")

    def __str__(self):
        return self.title


class StoryCategory(models.Model):
    title = models.CharField(_("title"), max_length=120)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _("story category")
        verbose_name_plural = _("story categories")

    def __str__(self):
        return self.title


class Story(models.Model):
    title = models.CharField(_("title"), max_length=120)
    order = models.IntegerField(_("order"))
    category = models.ForeignKey(StoryCategory, on_delete=models.CASCADE,
                                 related_name="stories")
    published = models.BooleanField(_("published"), default=False)
    video = models.ForeignKey(Media, on_delete=models.CASCADE,
                              verbose_name=_('video'))
    class Meta:
        verbose_name = _("story")
        verbose_name_plural = _("stories")

    def __str__(self):
        return self.title



class Feedback(models.Model):
    full_name = models.CharField(_("full name"), max_length=120)
    text = models.TextField(_("text"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    phone_number = models.CharField(_("phone number"), max_length=20, validators=[validate_phone_number])
    is_view = models.BooleanField(_("is view"), default=False)
    image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _("feedback")
        verbose_name_plural = _("feedbacks")

    def __str__(self):
        return self.full_name


class StoryProduct(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name="products")
    product = models.ForeignKey("products.Product", verbose_name=_("product"), on_delete=models.CASCADE,
                                related_name="stories")

    class Meta:
        verbose_name = _('story product')
        verbose_name_plural = _('story products')
        unique_together = ['story', 'product']


class HomeSlider(models.Model):
    title = models.CharField(_("title"), max_length=120)
    file = models.ForeignKey(Media, on_delete=models.CASCADE, help_text=_("image or gif"))
    desc = models.TextField(_("description"))

    class Meta:
        verbose_name = _("home slider")
        verbose_name_plural = _("home sliders")

    def __str__(self):
        return self.title