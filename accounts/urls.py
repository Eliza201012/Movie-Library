from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("registration/", views.registration, name="registration"),
    path("profile/", views.profile, name="profile"),
    path("update/", views.update_profile_and_user, name="update"),
    path("logout/", views.custom_logout, name="custom_logout"),
    path("change_password/", views.change_password, name="change_password"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


    # if settings.DEBUG:
    # -------------------
    # на продакшені (DEBUG=False) ця стрічка не працює,
    # тому медіа й статичні файли тоді обслуговуються через вебсервер (наприклад, Render).
    # --------------------------------------------------------------------------------------

    # urlpatterns += ...
    # -------------------
    #  до існуючого списку urlpatterns (де прописані всі твої path() і include())
    #  додаються нові маршрути (URL) для обслуговування файлів.
    # ---------------------------------------------------------------------------

    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # -------------------------------------------------------------------------
    # створює “тестовий” маршрут, який дозволяє Django показувати медіафайли
    # (наприклад, аватарки, картинки, завантаження) напряму під час розробки.