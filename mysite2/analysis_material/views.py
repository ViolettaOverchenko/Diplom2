from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView, CreateView
from analyzer.analyzer_class.KeyWords import KeyWords
from analyzer.analyzer_class.ReadFile import ReadFile
from analyzer.analyzer_class.CompatibilityAnalysis import CompatibilityAnalysis
from .forms import DocumentForm
from .models import Document
from django.urls import reverse_lazy

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

class CreateDocumentView(CreateView): # новый
    model = Document
    form_class = DocumentForm
    template_name = 'analysis_material/create_document.html'
    success_url = reverse_lazy('personal_account')

def createDocument(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personal_account')
    form = DocumentForm()

    return render(request,'analysis_material/create_document.html',{'form': form})

def deleteDocument(request, pk, template_name='analysis_material/personal_account.html'):
    document = Document.objects.get(pk=pk)
    #document = get_object_or_404(Document, pk=pk)
    if request.method=='POST':
        document.delete()
        return redirect('personal_account')
    return render(request, template_name)


def result_analize_two(request):
    # проверка чтобы либо текст либо файл
    # если файл не того формата тоже првоерка
    one_material_name = ""
    two_material_name = ""
    one_text_for_analize = ""
    two_text_for_analize = ""
    one_uploaded_file = None
    two_uploaded_file = None
    read_file = ReadFile()

    if 'one_material_name' in request.GET and request.GET['one_material_name']:
        one_material_name = request.GET['one_material_name']
    if 'two_material_name' in request.GET and request.GET['two_material_name']:
        two_material_name = request.GET['two_material_name']
    if 'one_text_for_analize' in request.GET and request.GET['one_text_for_analize']:
        one_text_for_analize = request.GET['one_text_for_analize']
    if 'two_text_for_analize' in request.GET and request.GET['two_text_for_analize']:
        two_text_for_analize = request.GET['two_text_for_analize']
    if 'one_uploaded_file' in request.FILES and request.FILES['one_uploaded_file']:
        one_uploaded_file = request.FILES['one_uploaded_file']
        one_uploaded_file = read_file.ReadFile(one_uploaded_file)
    if 'two_uploaded_file' in request.FILES and request.FILES['two_uploaded_file']:
        two_uploaded_file = request.FILES['two_uploaded_file']
        two_uploaded_file = read_file.ReadFile(two_uploaded_file)


    key_words = KeyWords()

    if one_uploaded_file is not None:
        one_data_keys, one_data = key_words.get_key_words(text=one_uploaded_file)
    else:
        one_data_keys, one_data = key_words.get_key_words(text=one_text_for_analize)

    if two_uploaded_file is not None:
        two_data_keys, two_data = key_words.get_key_words(text=two_uploaded_file)
    else:
        two_data_keys, two_data = key_words.get_key_words(text=two_text_for_analize)

    analisis = CompatibilityAnalysis()
    result = analisis.analyze(one_data_keys, two_data_keys)
    return render(request,
                  'analysis_material/results_two.html', context={'one_material_name': one_material_name,
                                                    'two_material_name': two_material_name,
                                                    'one_data': one_data,
                                                    'two_data': two_data,
                                                    'result': result})
