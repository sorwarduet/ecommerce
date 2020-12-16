from django.urls import path

from ecommerce.search.views import (
    ProductSearchView,


)

app_name = "search"
urlpatterns = [
    path("", ProductSearchView.as_view(), name="query"),

]
