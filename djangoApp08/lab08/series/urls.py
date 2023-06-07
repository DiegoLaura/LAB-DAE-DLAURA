from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(),name='index'),
    path('serie',views.SeriesView.as_view(),name='series'),
    path('serie/<int:serie_id>',views.SerieDetailView.as_view())

]