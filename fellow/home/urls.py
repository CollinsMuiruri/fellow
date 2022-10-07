from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("getServices/", views.get_services, name="getServices"),
    path("offerServices/", views.offer_services, name="offerServices"),
    path("services/", views.services, name="services"),
]
