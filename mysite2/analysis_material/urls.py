from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeViews.as_view(), name="home"),    # главная страница
    path('calculation_compatibility/', views.AnalysisMaterialViews.as_view(), name="calculation_compatibility"),
    path('result_analize_two/', views.result_analize_two, name="result_analize_two"),
    path('result_analize_one/', views.result_analize_one, name="result_analize_one"),
    path('personal_account/', views.PersonalAccountViews.as_view(), name="personal_account"),
    path('<int:pk>/', views.DocumentDetailViews.as_view(), name="document_detail"),
    path('delete/<int:pk>/', views.DocumentDeleteView.as_view(), name='document_delete'),
    #path('delete/<int:pk>/', views.deleteDocument, name='deleteDocument'),
    path('new/', views.DocumentCreateView.as_view(), name='document_new'), # new
]
