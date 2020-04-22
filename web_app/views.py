from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post
from .forms import ResumeUpload
from .models import UploadPdf

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'web_app/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'web_app/home.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    
class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'web_app/about.html', {'title': 'About'})

def store_pdf(request):
    uploadpdf = UploadPdf.objects.all()
    return render(request, 'web_app/store_pdf.html', {'uploadpdf': uploadpdf})

def upload_pdf(request):
    if request.method == "POST":
        form = ResumeUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
        return redirect('store_pdf')
    else:
        form = ResumeUpload()
    return render(request, 'web_app/upload_pdf.html', {'form': form})

# from django.views.generic.edit import FormView
# from .forms import FileFieldForm

# class FileFieldView(FormView):
#     form_class = FileFieldForm
#     template_name = 'upload.html'  # Replace with your template.
#     success_url = '...'  # Replace with your URL or reverse().

#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file_field')
#         if form.is_valid():
#             for f in files:
#                 ...  # Do something with each file.
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)