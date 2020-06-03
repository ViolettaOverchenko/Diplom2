from django.contrib import admin

from .models import Document, AnalysisDocument, Relation_Document_Analysis, Theme, AnalysisTheme, Relation_Theme_Analysis, CleanText, Keyword

admin.site.register(Document)
