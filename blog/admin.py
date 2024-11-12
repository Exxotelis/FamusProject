from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'slug')
    search_fields = ['title', 'content']
    list_filter = ['created_at']

    # Define the form layout
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'image_data')
        }),
    )

    # Override the save_model to automatically handle base64 encoding
    def save_model(self, request, obj, form, change):
        obj.save()  # Save the object, this will invoke the custom save() method in the model
        super().save_model(request, obj, form, change)

admin.site.register(Post, PostAdmin)
