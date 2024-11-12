import base64
from django.db import models
from django.urls import reverse
from django.core.files.base import ContentFile

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image_data = models.TextField(null=True, blank=True)  # Base64 image data
    updated_at = models.DateTimeField(auto_now=True)

    def save_image_as_base64(self, image_file):
        """Convert an image file to base64 and save it in the `image_data` field"""
        if image_file:
            # Read and encode the image as base64
            encoded_img = base64.b64encode(image_file.read()).decode('utf-8')
            # Get the MIME type (e.g., "image/jpeg")
            mime_type = image_file.content_type
            # Format as a data URL and assign to image_data
            self.image_data = f"data:{mime_type};base64,{encoded_img}"

    def save(self, *args, **kwargs):
        """Override save to convert image to base64 if it's uploaded via the admin panel"""
        image_file = kwargs.pop('image_file', None)
        if image_file:
            # If an image file is provided, convert to base64
            self.save_image_as_base64(image_file)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.slug])

