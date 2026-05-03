from django.contrib import admin

# Register your models here.
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_at")
    
    