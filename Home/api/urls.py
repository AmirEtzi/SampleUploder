from django.urls import path
from Home.api.views import sample_list


urlpatterns = [
    path("samplelist/", sample_list, name="sample_list"),
]
