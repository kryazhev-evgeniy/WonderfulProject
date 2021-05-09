from django.contrib import admin
from .models import Order,Service, Category, ReviewUser
# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user_order','service_order','date','time')
    list_filter = ('date','time')
    ordering = ('user_order','service_order','date','time')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title','user')

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service,ServiceAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(ReviewUser,ReviewAdmin)

admin.site.site_header = "Администрация салона Чудо"
