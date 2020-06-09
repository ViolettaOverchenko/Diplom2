from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView
from analyzer.analyzer_class.read_file import ReadFile
from analyzer.analyzer_class.compatibility_analysis import CompatibilityAnalysis
from analyzer.analyzer_class.thesaurus import Thesaurus
from .models import Document, User
from django.urls import reverse_lazy
from .forms import DocumentForm

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

class DocumentDetailViews(DetailView):
    """ Подробная информация о документе """
    model = Document
    template_name = 'analysis_material/document_detail.html'

class DocumentDeleteView(DeleteView):
    """ Удаление документа """
    model = Document
    template_name = 'analysis_material/personal_account.html'
    success_url = reverse_lazy('personal_account')

class DocumentCreateView(CreateView):
    """ Добавление документа """
    model = Document
    form_class = DocumentForm
    template_name = 'analysis_material/document_form.html'


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(DocumentCreateView, self).form_valid(form)

def result_analize_one(request):
    # проверка чтобы либо текст либо файл
    # если файл не того формата тоже првоерка
    name_document = ""
    one_text_area = ""
    path_file = None
    read_file = ReadFile()

    if 'name_document' in request.POST and request.POST['name_document']:
        name_document = request.POST['name_document']
    if 'one_text_area' in request.POST and request.POST['one_text_area']:
        one_text_area = request.POST['one_text_area']
    if 'path_file' in request.FILES and request.FILES['path_file']:
        path_file = request.FILES['path_file']
        path_file = read_file(path_file)

    thesaurus = Thesaurus()
    keys, tfidf = thesaurus(path_file)
    return render(request,
                  'analysis_material/results_one.html', context={'name_document': name_document,
                                                    'keys': keys,
                                                    'tfidf': tfidf})
def result_analize_two(request):
    # проверка чтобы либо текст либо файл
    # если файл не того формата тоже првоерка
    one_material_name = ""
    two_material_name = ""
    one_text_area = ""
    two_text_area = ""
    one_uploaded_file = None
    two_uploaded_file = None
    read_file = ReadFile()

    if 'one_material_name' in request.POST and request.POST['one_material_name']:
        one_material_name = request.POST['one_material_name']
    if 'one_text_area' in request.POST and request.POST['one_text_area']:
        one_text_area = request.POST['one_text_area']
    if 'one_uploaded_file' in request.FILES and request.FILES['one_uploaded_file']:
        one_uploaded_file = request.FILES['one_uploaded_file']
        one_uploaded_file = read_file(one_uploaded_file)

    if 'two_material_name' in request.POST and request.POST['two_material_name']:
        two_material_name = request.POST['two_material_name']
    if 'two_text_area' in request.POST and request.POST['two_text_area']:
        two_text_area = request.POST['two_text_area']
    if 'two_uploaded_file' in request.FILES and request.FILES['two_uploaded_file']:
        two_uploaded_file = request.FILES['two_uploaded_file']
        two_uploaded_file = read_file(two_uploaded_file)

    compatibility_analysis = CompatibilityAnalysis()
    one_data, two_data, result = compatibility_analysis(one_text_area, two_text_area,
                                                                   one_uploaded_file, two_uploaded_file)
    return render(request,
                  'analysis_material/results_two.html', context={'one_material_name': one_material_name,
                                                    'two_material_name': two_material_name,
                                                    'one_data': one_data,
                                                    'two_data': two_data,
                                                    'result': result})
