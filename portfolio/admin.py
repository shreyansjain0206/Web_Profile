from django.contrib import admin
from .models import Profile, Project, Skill, Experience, ResearchPaper, Certificate, Achievement, ExtraCurricular


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'tech_stack']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'start_date', 'is_current']


@admin.register(ResearchPaper)
class ResearchPaperAdmin(admin.ModelAdmin):
    list_display = ['title', 'journal_or_conference', 'publication_date']

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuing_organization', 'issue_date']

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuing_organization', 'date']

@admin.register(ExtraCurricular)
class ExtraCurricularAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'organization', 'start_date']