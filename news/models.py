from django.db import models
from PIL import Image

class News(models.Model):
    title = models.CharField(verbose_name="Title", max_length=80, unique=True)
    photo = models.ImageField(verbose_name="Photo", upload_to="photos/", default="photos/default-photo.jpg", blank=True, null=True)
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)
    main_text = models.TextField(verbose_name="Main text")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Перевіряємо, чи є фото
        if self.photo and hasattr(self.photo, 'path') and self.photo.path:
            img = Image.open(self.photo.path)
            if img.height > 670 or img.width > 1200:
                new_img = (1200, 670)  # width, height
                img.thumbnail(new_img)
                img.save(self.photo.path)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title