from django.urls import path
from medicSearch.views.perfilView import list_profile_view

urlpatterns = [
    path("", list_profile_view),
    path("<int:id>", list_profile_view)
]