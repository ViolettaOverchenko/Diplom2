from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeViews.as_view(), name="home"),    # главная страница
    path('calculation_compatibility/', views.AnalysisMaterialViews.as_view(), name="calculation_compatibility"),
    path('result_analize_two/', views.result_analize_two, name="result_analize_two"),
    path('personal_account/', views.PersonalAccountViews.as_view(), name="personal_account"),
    path('<int:pk>/', views.DocumentDetailViews.as_view(), name="document_detail"),
    path('create_document/', views.CreateDocumentView.as_view(), name='create_document'),
    path('delete/<int:pk>/', views.deleteDocument, name='deleteDocument'),
]
