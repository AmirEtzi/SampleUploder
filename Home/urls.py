from django.urls import path, include
from . import views
from .views import (
    SampleViewerView,
    SampleUploderView,
    SampleDetailView,
    SampleEditorView,
    DeleteSampleView,
    ImageDeleteView,
)

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("sampleviewer/", SampleViewerView.as_view(), name="sampleviewer"),
    path("sample/<int:pk>", SampleDetailView.as_view(), name="sampledetails"),
    path("sampleuploder/", SampleUploderView.as_view(), name="sampleuploder"),
    path("sampleeditor/<int:pk>/", SampleEditorView.as_view(), name="sampleeditor"),
    path(
        "deletesample/<int:pk>/delete", DeleteSampleView.as_view(), name="deletesample"
    ),
    path("delete-image/<int:pk>/", ImageDeleteView.as_view(), name="delete_image"),
]
