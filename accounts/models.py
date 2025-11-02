from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    avatar = models.ImageField(verbose_name="Avatar", upload_to="avatars/", default="avatars/default.png")
    bio = models.TextField(verbose_name="Bio", blank=True, null=True)
    favorite_movies = models.ManyToManyField("movies.Movie", verbose_name="Favorite movies", blank=True)

    def save(self, *args, **kwargs):
        super().save()  # Зберігаємо завантажене зображення
        img = Image.open(self.avatar.path)  # Відкриваємо зображення
        # Перевіряємо розміри
        if img.height > 100 or img.width > 100:
            # Якщо не підходять, змінюємо розміри
            new_img = (100, 100)
            img.thumbnail(new_img) # Створюємо мініатюру
            img.save(self.avatar.path)  # Та зберігаємо його в тому ж місці, де воно було збережено