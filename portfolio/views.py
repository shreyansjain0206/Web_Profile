from django.shortcuts import render
from .models import Profile, Project, Skill, Experience, ResearchPaper, Certificate, Achievement, ExtraCurricular


def index(request):
    context = {
        'profile': Profile.objects.first(),
        'projects': Project.objects.all(),
        'skills': Skill.objects.all().order_by('category'),
        'experiences': Experience.objects.all().order_by('-start_date'),
        'research_papers': ResearchPaper.objects.all().order_by('-publication_date'),
        'certificates': Certificate.objects.all().order_by('-issue_date'),
        'achievements': Achievement.objects.all().order_by('-date'),
        'extra_curricular': ExtraCurricular.objects.all().order_by('-start_date'),
    }
    return render(request, 'portfolio/index.html', context)