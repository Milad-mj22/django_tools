from django.contrib import admin
from .models import Profile
from .models import Tools,Post,Tools,Post_quill , jobs , Projects ,raw_material,create_order\
                    ,mother_material,FoodFilter,SnappFoodList,cities,FoodRawMaterial
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
admin.site.register(Tools)
admin.site.register(FoodFilter)
admin.site.register(SnappFoodList)
admin.site.register(cities)
admin.site.register(FoodRawMaterial)








  
class textEditorAdmin(admin.ModelAdmin):
   list_display = ["title"]
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }


admin.site.register(full_post, textEditorAdmin)




admin.site.register(jobs)