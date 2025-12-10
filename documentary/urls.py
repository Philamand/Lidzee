from django.urls import path
from .views import DocumentaryListView

urlpatterns = [path("", DocumentaryListView.as_view(), name="documentary_list")]
