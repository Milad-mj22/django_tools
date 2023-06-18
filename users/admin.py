from django.contrib import admin
from .models import Profile
from .models import Post,Tools,Post_quill


import enchant
enchant.dict_exists('en')


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



from .models import full_post
from django.db import models
from tinymce.widgets import TinyMCE

  
class textEditorAdmin(admin.ModelAdmin):
   list_display = ["title"]
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }


admin.site.register(full_post, textEditorAdmin)