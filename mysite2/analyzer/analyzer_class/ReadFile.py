import os
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
import unicodedata
from subprocess import Popen, PIPE
import docx
from mysite2 import settings

class ReadFile(object):
    def __init__(self):
        pass

    def ReadFile(self, file):
        document_path = settings.MEDIA_URL + file.name
        if os.path.exists(document_path):
            return HttpResponseRedirect("/index")
        document = self.saveFile(file)
        text = self.readText(document, document_path)
        self.delete_doc(document)
        return  text

    def readText(self, document, document_path):
        text = ""
        if document.endswith('.docx'):
            text = self.read_docx(document_path)
        elif document.endswith('.doc'):
            text = self.read_doc(document_path)
        return text


    def delete_doc(self,document):
        os.remove(os.path.join(settings.MEDIA_ROOT, document))

    def saveFile(self, file):
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        return filename

    def read_docx(self, document_path):
        text = ""
        doc = docx.Document(document_path)
        for paragraph in doc.paragraphs:
            paragraphText = paragraph.text
            text = text + ' ' + paragraphText
        text = unicodedata.normalize('NFKD', text)
        return text

    def read_doc(self, document_path):
        cmd = ['antiword', document_path]
        doc = Popen(cmd, stdout=PIPE)
        stdout, stderr = doc.communicate()
        text = stdout.decode('utf-8', 'ignore')
        return text
