from django.db import models
class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='profile/', blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    resume = models.FileField(upload_to='resume/', blank=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=80)  # percentage
    category = models.CharField(max_length=100)  # e.g. Frontend, Backend

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.role} at {self.company}"




# ──────────────────────────────
# RESEARCH PAPERS
# ──────────────────────────────
class ResearchPaper(models.Model):
    title = models.CharField(max_length=300)
    authors = models.CharField(max_length=300)
    journal_or_conference = models.CharField(max_length=300)
    publication_date = models.DateField()
    abstract = models.TextField(blank=True)
    paper_link = models.URLField(blank=True)
    doi = models.CharField(max_length=100, blank=True)  # Digital Object Identifier

    def __str__(self):
        return self.title


# ──────────────────────────────
# CERTIFICATES
# ──────────────────────────────
class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuing_organization = models.CharField(max_length=200)
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    credential_url = models.URLField(blank=True)
    image = models.ImageField(upload_to='certificates/', blank=True)

    def __str__(self):
        return self.title


# ──────────────────────────────
# ACHIEVEMENTS
# ──────────────────────────────
class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    issuing_organization = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title


# ──────────────────────────────
# EXTRA CURRICULAR
# ──────────────────────────────
class ExtraCurricular(models.Model):
    CATEGORY_CHOICES = [
        ('club', 'Club / Society'),
        ('sport', 'Sports'),
        ('volunteer', 'Volunteering'),
        ('event', 'Event / Hackathon'),
        ('other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    organization = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title