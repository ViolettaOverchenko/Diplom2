from django.shortcuts import render
from django.views.generic.base import View

from .models import Document

class AnalysisMaterialViews(View):
    """ Главная страница """
    def get(self, request):
        return render(request, "analysis_material/home.html")

class PersonalAccountViews(View):
    """ Личный кабинет: список документов, список анализов """
    def get(self, request):
        documents = Document.objects.all()
        return render(request, "analysis_material/personal_account.html", {"document_list": documents})

class DocumentDetailViews(View):
    """ Подробная информация о документе """
    def get(self, request, pk):
        document = Document.objects.get(id = pk)
        return render(request, "analysis_material/document_detail.html", {"document": document})
