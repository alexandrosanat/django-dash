from django.urls import path
from . import views
from home.dash_apps.finished_apps import simple_example

# Do NOT remove the unused import as with the plotly_dash extension it will render automatically

app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
]
