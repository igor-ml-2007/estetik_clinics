from django.contrib import admin

from clinics.models import *
from services.models import WhoPerformsProcedure

# Register your models here.

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'requirements']
    search_fields = ['title', 'requirements', 'responsibilities', 'conditions']


@admin.register(Action)
class ActionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'expires_in', 'percentage', 'in_discount', 'desc']
    search_fields = ['title', 'short_desc', 'desc']
    list_filter = ['in_discount', 'special_offer', 'expires_in']


@admin.register(ActionTag)
class ActionTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(ActionImage)
class ActionImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']


@admin.register(OnlineAppointment)
class OnlineAppointmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'full_name', 'book_date', 'active']
    search_fields = ['phone_number', 'full_name']
    list_filter = ['active']
    list_editable = ['active']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['id', 'video', 'summary']


@admin.register(PhotoGalleryCategory)
class PhotoGalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(PhotoGallery)
class PhotoGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category']


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(ContactChiefDoctor)
class ContactChiefDoctorAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'full_name', 'active']
    list_editable = ['active']

class ServicesInline(admin.StackedInline):
    model = WhoPerformsProcedure
    extra = 1

@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'position', 'experience_in_field', 'experience_in_years',
                    'experience_in_company']
    list_filter = ['position']
    inlines = [ServicesInline]


@admin.register(Diploma)
class DiplomaAdmin(admin.ModelAdmin):
    list_display = ['id', 'specialist']


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']
    search_fields = ['title']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'published']
    search_fields = ['title', 'desc']
    list_filter = ['published', 'category', 'special_offer']


@admin.register(NewsTag)
class NewTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'address', 'work_time']
    search_fields = ['phone_number', 'address']


@admin.register(ArticleCategory)
class ArticleCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'created_at', 'published']
    search_fields = ['title', 'desc']
    list_filter = ['published', 'category']


@admin.register(StoryCategory)
class StoryCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']



class StoryProductInline(admin.TabularInline):
    model = StoryProduct
    extra = 1


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'published', 'order']
    search_fields = ['title', 'desc']
    list_filter = ['published', 'category']
    inlines = [StoryProductInline]



@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'created_at', 'phone_number', 'is_view']
    list_filter = ['is_view']
    search_fields = ['full_name', 'phone_number', 'text']


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'file']
    search_fields = ['title']

