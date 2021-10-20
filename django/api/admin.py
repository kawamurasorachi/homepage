from django.contrib import admin
from .models import Book, Article, Work
from django.utils.safestring import mark_safe


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_og_image', 'created_at', 'is_public')

    def admin_og_image(self, row):
        if row.thumbnail:
            return mark_safe('<img src="{}" style="width:100px;height:auto;">'.format(row.thumbnail.url))
        else:
            return 'no image'         

    admin_og_image.allow_tags = True



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_og_image', 'created_at', 'is_public')

    def admin_og_image(self, row):
        if row.thumbnail:
            return mark_safe('<img src="{}" style="width:100px;height:auto;">'.format(row.thumbnail.url))
        else:
            return 'no image'

    admin_og_image.allow_tags = True

class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'admin_og_image', 'created_at')

    def admin_og_image(self, row):
        if row.thumbnail:
            return mark_safe('<img src="{}" style="width:100px;height:auto;">'.format(row.thumbnail.url))
        else:
            return 'no image'

    admin_og_image.allow_tags = True

admin.site.register(Book ,BookAdmin)
admin.site.register(Article ,ArticleAdmin)
admin.site.register(Work ,WorkAdmin)