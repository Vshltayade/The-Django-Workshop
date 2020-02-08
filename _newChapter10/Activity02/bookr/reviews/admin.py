from django.contrib import admin
from django.utils.html import format_html
from reviews.models import Publisher, Contributor, Book, BookContributor, Review, ReviewerProfile


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('name__startswith',)
    list_per_page = 20
    list_max_show_all = 50

class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn')
    list_filter = ('publisher', 'publication_date')
    list_per_page = 20
    list_max_show_all = 50
    search_fields = ('title', 'isbn', 'publisher__name')

class ContributorAdmin(admin.ModelAdmin):
    list_display = ('last_names', 'first_names')
    list_filter = ('last_names',)
    list_per_page = 20
    list_max_show_all = 50
    search_fields = ('last_names__startswith', 'first_names')

class BookContributorAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_max_show_all = 50

class ReviewerProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location', 'has_profile_photo')
    list_editable= ('location',)
    list_per_page = 20
    list_max_show_all = 50

    def has_profile_photo(self, obj):
        return obj.profile_photo and format_html('<h1>&#128511;</h1>')  or ''

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ('book__title', 'creator__username',)
    list_filter = ('rating',)
    list_per_page = 20
    list_max_show_all = 50
    show_full_result_count = False

# Register your models here.
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor, BookContributorAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(ReviewerProfile, ReviewerProfileAdmin)
