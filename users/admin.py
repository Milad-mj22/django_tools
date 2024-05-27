from django.contrib import admin
from .models import Profile
from .models import Post,Tools,Post_quill , jobs , Projects ,raw_material,create_order\
                    ,mother_material
from django.contrib import admin
from .models import QuillPost
from .models import full_post
from django.db import models
from tinymce.widgets import TinyMCE



admin.site.register(Profile)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(raw_material)
admin.site.register(mother_material)
admin.site.register(create_order)








  
class textEditorAdmin(admin.ModelAdmin):
   list_display = ["title"]
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }


admin.site.register(full_post, textEditorAdmin)




admin.site.register(jobs)