from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.HomeViews.as_view(), name="home"),    # главная страница
    path('calculation_compatibility/', views.AnalysisMaterialViews.as_view(), name="calculation_compatibility"),
    path('personal_account/', views.PersonalAccountViews.as_view(), name="personal_account"),
    path('<slug:slug>/', views.DocumentDetailViews.as_view(), name="document_detail"),
]
