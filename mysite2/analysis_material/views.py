from django.shortcuts import render
from django.views.generic import View, ListView, DetailView

from .models import Document

class HomeViews(View):
    """ Главная страница """
    def get(self, request):
        return render(request, "analysis_material/home.html")

class AnalysisMaterialViews(View):
    """ Страница для расчёта совместимости """
    def get(self, request):
        return render(request, "analysis_material/calculation_compatibility.html")

class PersonalAccountViews(ListView):
    """ Личный кабинет: список документов, список анализов """
    model = Document
    template_name = "analysis_material/personal_account.html"

    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)

    """def get(self, request):
        documents = Document.objects.all()
        return render(request, "analysis_material/personal_account.html", {"document_list": documents})"""

class DocumentDetailViews(DetailView):
    """ Подробная информация о документе """
    model = Document
    slug_field = "slug"
    """def get(self, request, slug):
        document = Document.objects.get(slug = slug)
        return render(request, "analysis_material/document_detail.html", {"document": document})"""
