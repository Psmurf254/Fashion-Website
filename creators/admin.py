from django.contrib import admin
from . models import *


class CreatorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'contact_phone', 'specialty')
    list_filter = ('full_name', 'gender')
    search_fields = ('full_name', 'gender')




@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('fashion', 'user', 'text', 'created_at')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('fashion', 'user')








admin.site.register(Creator, CreatorAdmin)
admin.site.register(ReviewRating)
admin.site.register(CreatorReviewRating)
admin.site.register(FashionCategory)
admin.site.register(Fashion)
admin.site.register(Favorite)
admin.site.register(Following)
