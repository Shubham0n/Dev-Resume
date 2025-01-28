from django.urls import path
from dev_resume.views import resume_list, resume_view, generate_pdf

urlpatterns = [
    path("", resume_list, name="resume_list"),
    path("resume/<slug:developer>", resume_view, name="resume_view"),
    path("generate-pdf/", generate_pdf, name="generate_pdf"),
]
