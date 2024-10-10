from django.contrib import admin
from .models import Profile
from .models import Tools,Post,Tools,Post_quill , jobs , Projects ,raw_material,create_order\
                    ,mother_material,FoodFilter,SnappFoodList,cities,FoodRawMaterial,mother_food,mode_raw_materials,\
                    Inventory,InventoryLog,Warehouse,RestaurantBranch,NightOrderRemainder
from django.contrib import admin
from .models import QuillPost
from .models import full_post
from django.db import models
from tinymce.widgets import TinyMCE
from khayyam import JalaliDatetime


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
admin.site.register(mother_food)
admin.site.register(mode_raw_materials)
# admin.site.register(Inventory)








  
class textEditorAdmin(admin.ModelAdmin):
   list_display = ["title"]
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }


admin.site.register(full_post, textEditorAdmin)




admin.site.register(jobs)



class InventoryAdmin(admin.ModelAdmin):
    list_display = ('raw_material_name', 'warehouse', 'quantity', 'jalali_date')
    search_fields = ('raw_material__name', 'warehouse__name')
    list_filter = ('warehouse',)

    def raw_material_name(self, obj):
        return obj.inventory_raw_material.name
    raw_material_name.short_description = 'Raw Material'

    # Method to display the Jalali date in the admin list view
    def jalali_date(self, obj):
        return JalaliDatetime(obj.last_updated).strftime('%Y/%m/%d %H:%M:%S')
    
    # Set the column name for the jalali_date method
    jalali_date.short_description = 'تاریخ (هجری شمسی)'



    

admin.site.register(Inventory, InventoryAdmin)



class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'capacity')  # نمایش ستون‌های مورد نظر
    search_fields = ('name', 'location')  # امکان جستجو بر اساس نام و مکان انبار

admin.site.register(Warehouse, WarehouseAdmin)




class InventoryLogAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('inventory', 'change_type', 'amount', 'jalali_date', 'user', 'warehouse')

    # Add filtering options
    list_filter = ('change_type', 'inventory__warehouse', 'date')
    
    # Enable search functionality for specific fields
    search_fields = ('inventory__raw_material__name', 'user__username', 'inventory__warehouse__name')
    
    # Fields to display in the form
    fields = ('inventory', 'change_type', 'amount', 'date', 'user')
    
    # Method to display the Jalali date in the admin list view
    def jalali_date(self, obj):
        return JalaliDatetime(obj.date).strftime('%Y/%m/%d %H:%M:%S')
    
    # Set the column name for the jalali_date method
    jalali_date.short_description = 'تاریخ (هجری شمسی)'
    
    # Display the warehouse in list view (from the related Inventory model)
    def warehouse(self, obj):
        return obj.inventory.warehouse.name

# Register the model with the custom admin
admin.site.register(InventoryLog, InventoryLogAdmin)




admin.site.register(RestaurantBranch)
admin.site.register(NightOrderRemainder)
