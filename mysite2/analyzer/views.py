from django.shortcuts import render
from analyzer.analyzer_class.KeyWords import KeyWords
from analyzer.analyzer_class.ReadFile import ReadFile
from analyzer.analyzer_class.CompatibilityAnalysis import CompatibilityAnalysis



# Create your views here.
def index(request):
    return render(request,
                  'html/index.html')


def analize_one(request):
    return render(request,
                  'html/analize_one.html')


def analize_two(request):
    return render(request,
                  'html/analize_two.html')


def result_analize_one(request):
    return render(request,
                  'html/results_one.html')


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
    if 'two_uploaded_file' in request.FILES and request.FILES['two_uploaded_file']:
        two_uploaded_file = request.FILES['two_uploaded_file']
        two_uploaded_file = read_file.ReadFile(two_uploaded_file)
    if 'one_uploaded_file' in request.FILES and request.FILES['one_uploaded_file']:
        one_uploaded_file = request.FILES['one_uploaded_file']
        one_uploaded_file = read_file.ReadFile(one_uploaded_file)

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
                  'html/results_two.html', context={'one_material_name': one_material_name,
                                                    'two_material_name': two_material_name,
                                                    'one_data': one_data,
                                                    'two_data': two_data,
                                                    'result': result})
