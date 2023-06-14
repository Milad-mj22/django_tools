from django.contrib import admin
from .models import Profile
from .models import Post,Tools,Post_quill


admin.site.register(Profile)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tools)




from django.contrib import admin
from .models import QuillPost

@admin.register(QuillPost)
class QuillPostAdmin(admin.ModelAdmin):
    pass




admin.site.register(Post_quill)


# from django import forms
# from django.contrib.flatpages.admin import FlatPageAdmin
# from django.contrib.flatpages.models import FlatPage
# from django.urls import reverse
# from tinymce.widgets import TinyMCE

# class TinyMCEFlatPageAdmin(FlatPageAdmin):
#     def formfield_for_dbfield(self, db_field, **kwargs):
#         if db_field.name == 'content':
#             return db_field.formfield(widget=TinyMCE(
#                 attrs={'cols': 80, 'rows': 30},
#                 mce_attrs={'external_link_list_url': reverse('tinymce-linklist')},
#             ))
#         return super().formfield_for_dbfield(db_field, **kwargs)


# admin.site.unregister(FlatPage)
# admin.site.register(FlatPage, TinyMCEFlatPageAdmin)