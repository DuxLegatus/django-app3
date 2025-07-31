from django.contrib import admin
from .models import User

# Register your models here.

admin.site.site_header = "User Admin panel"
admin.site.site_title = "User"
admin.site.index_title = "admin panel"




@admin.action(description="change status to false")
def change_status(modeladmin,request,queryset):
    queryset.update(status=False)

@admin.action(description="change status to true")
def change_status1(modeladmin,request,queryset):
    queryset.update(status=True)



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name','lastname','age','status']
    list_filter = ('status',)
    search_fields = ('name',)
    list_editable = ('status',)
    ordering = ('created_at',)
    actions = [change_status,change_status1]

