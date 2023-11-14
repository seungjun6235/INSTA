from django.contrib import admin
from .models import Post
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class PostAdmin(ImportExportModelAdmin):
    pass
    # resource_classes = ['content', 'like_users']


admin.site.register(Post,PostAdmin)