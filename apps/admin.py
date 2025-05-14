from django.contrib import admin

from apps.models import BlogPost

# Register your models here.
# admin.site.unregister(Group)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    pass
    # list_display = ('name',)
    # exclude = ('slug',)