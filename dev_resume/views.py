from django.http import HttpResponse, request
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

from weasyprint import HTML

from .models import DeveloperProfile


def resume_list(request: request) -> HttpResponse:
    """
    This view is used to display a list of resumes.
    """

    resumes = DeveloperProfile.objects.all()
    return render(request, "dev_resume_list.html", {"resumes": resumes})


def resume_view(request: request, developer: str) -> HttpResponse:
    """
    This view is used to display a developer's resume.
    """

    resume = get_object_or_404(DeveloperProfile, slug=developer)
    context = {
        "name": resume.name,
        "phone": resume.phone_number,
        "email": resume.email,
        "linkedin": resume.linkedin,
        "github": resume.github,
        "objective": resume.objective,
        "skills": resume.get_skills(),
        "experiences": resume.experience.all(),
        "projects": resume.projects.all(),
        "educations": resume.education.all(),
        "languages": resume.languages.all(),
    }

    return render(request, "dev_resume.html", context)


def generate_pdf(request: request) -> HttpResponse:
    """
    This view is used to generate a PDF of a developer's resume.
    """

    resume = get_object_or_404(DeveloperProfile, name=request.GET.get("name"))

    context = {
        "name": resume.name,
        "phone": resume.phone_number,
        "email": resume.email,
        "objective": resume.objective,
        "skills": resume.get_skills(),
        "experiences": resume.experience.all(),
        "projects": resume.projects.all(),
        "educations": resume.education.all(),
        "languages": resume.languages.all(),
        "developer_list": DeveloperProfile.objects.values_list(
            "name",
            flat=True,
        ),
    }

    html_string = render_to_string("cv_pdf.html", context)
    pdf = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="resume.pdf"'
    return response
