from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.AnalysisMaterialViews.as_view()),    # главная страница
    path('personal_account/', views.PersonalAccountViews.as_view(), name="personal_account"),
    path('<int:pk>/', views.DocumentDetailViews.as_view(), name="document_detail"),
]
