from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .forms import DocumentForm
from .models import Document

class DocumentUploadView(View):
    def get(self, request):
        docs = Document.objects.all()
        return render(self.request, 'documents/index.html', {'docs': docs})

    def post(self, request):
        form = DocumentForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            doc = form.save()
            data = {'is_valid': True, 'name': doc.file.name, 'url': doc.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)