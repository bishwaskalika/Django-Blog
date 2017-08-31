from django.contrib import admin

# Register your models here.
from . models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp', 'updated')
    empty_value_display = 'unknown'
    list_filter = ('title','timestamp')
    search_fields = ('title',)



    class Meta:
        model = Post


admin.site.empty_value_display = '(None)'
admin.site.register(Post, PostModelAdmin)