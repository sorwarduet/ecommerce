from django.urls import path

from search.views import (
    ProductSearchView,


)

app_name = "search"
urlpatterns = [
    path("", ProductSearchView.as_view(), name="list"),

]
