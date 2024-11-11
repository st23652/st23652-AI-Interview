from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class Interview(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    candidate = models.ForeignKey(User, related_name='interviews', on_delete=models.CASCADE)
    interviewer = models.ForeignKey(User, related_name='conducted_interviews', on_delete=models.CASCADE)
    scheduled_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=(('scheduled', 'Scheduled'), ('completed', 'Completed')))
    question_set = models.CharField(max_length=50, choices=(('problem_solving', 'Problem Solving'), ('decision_making', 'Decision Making'), ...))  # Add all sets
    answers = models.JSONField()  # Store answers in a JSON field (ideal for dynamic questions)
    feedback = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class InterviewQuestion(models.Model):
    interview = models.ForeignKey(Interview, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    order = models.PositiveIntegerField()
    
    def __str__(self):
        return f'Question {self.order}: {self.question_text[:50]}'

class InterviewResponse(models.Model):
    interview = models.ForeignKey(Interview, related_name='responses', on_delete=models.CASCADE)
    question = models.ForeignKey(InterviewQuestion, related_name='responses', on_delete=models.CASCADE)
    response_text = models.TextField()

    def __str__(self):
        return f'Response to Question {self.question.order}'

class CVSubmission(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    job = models.ForeignKey('Job', on_delete=models.CASCADE)
    cv_file = models.FileField(upload_to='cvs/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
def validate_file(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Only PDF files are allowed.')

class CustomUser(AbstractBaseUser):
    ROLE_CHOICES = [
        ('candidate', 'Candidate'),
        ('employer', 'Employer'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employer')
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    # Employer-specific fields
    company_name = models.CharField(max_length=255, blank=True, null=True)
    starting_date = models.DateField(blank=True, null=True)
    industry = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    is_employed = models.BooleanField(default=False)
    company_size = models.CharField(max_length=50, blank=True, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = BaseUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    class Meta:
        abstract = False

class Resume(models.Model):
    candidate = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='resumes/')
    parsed_text = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.candidate.username}'s Resume"
        
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_candidate = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)
    
    # Candidate fields
    occupation = models.CharField(max_length=100, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True)
    currently_employed = models.BooleanField(default=False)
    current_company = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    
    # Employer fields
    company_name = models.CharField(max_length=255, blank=True)
    company_start_date = models.DateField(blank=True, null=True)
    company_size = models.CharField(max_length=100, blank=True)
    company_industry = models.CharField(max_length=100, blank=True)
    years_in_business = models.PositiveIntegerField(blank=True, null=True)
    website = models.URLField(blank=True)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

class Question(models.Model):
    QUESTION_SET_CHOICES = [
        ('problem_solving', 'Problem Solving'),
        ('decision_making', 'Decision Making'),
    ]
    question_set = models.CharField(max_length=20, choices=QUESTION_SET_CHOICES)
    text = models.TextField()

    def __str__(self):
        return self.text

def get_custom_user_form():
    from .forms import CustomUserCreationForm
    return CustomUserCreationForm

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, password, **extra_fields)

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        pass

# models.py
class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Employer(models.Model):
    COMPANY_SIZE_CHOICES = [
        ('1-10', '1-10 employees'),
        ('11-50', '11-50 employees'),
        ('51-200', '51-200 employees'),
        ('201-500', '201-500 employees'),
        ('501-1000', '501-1000 employees'),
        ('1001+', '1001+ employees'),
    ]

    INDUSTRY_CHOICES = [
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('manufacturing', 'Manufacturing'),
        ('aviation', 'Aviation'),
        ('marketing', 'Marketing'),
        ('estate', 'Real Estate'),
        ('petrolium', 'Petrolium'),
        ('agriculture', 'Agriculture'),
        ('entertainment', 'Entertainment'),
        ('hospitality', 'Hospitality'),
        ('food', 'Food'),
        ('automobile', 'Auto Mobile'),
        ('business', 'Business'),
        # Add more industries as needed
    ]
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    start_date = models.DateField()
    company_size = models.CharField(max_length=255, choices=COMPANY_SIZE_CHOICES)
    industry = models.CharField(max_length=255, choices=INDUSTRY_CHOICES)

    def __str__(self):
        return self.company_name

class Candidate(models.Model):
    INDUSTRY_CHOICES = [
        ('tech', 'Technology'),
        ('finance', 'Finance'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('manufacturing', 'Manufacturing'),
        ('aviation', 'Aviation'),
        ('marketing', 'Marketing'),
        ('estate', 'Real Estate'),
        ('petrolium', 'Petrolium'),
        ('agriculture', 'Agriculture'),
        ('entertainment', 'Entertainment'),
        ('hospitality', 'Hospitality'),
        ('food', 'Food'),
        ('automobile', 'Auto Mobile'),
        ('business', 'Business'),
        # Add more industries as needed
    ]
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    occupation = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    currently_employed = models.BooleanField(default=False)
    current_company = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Skill(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contract', 'Contract'),
    ]
    
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    experience = models.IntegerField()  # or models.PositiveIntegerField() if you don't want negative numbers
    job_type = models.CharField(max_length=10, choices=JOB_TYPE_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    job_type = models.CharField(max_length=50, choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('internship', 'Internship'), ('placement', 'Placement')])
    deadline = models.DateField()

    class Meta:
        db_table = 'jobpostings'

    def __str__(self):
        return f"{self.title} at {self.company_name}"
    
class CandidateResponse(models.Model):
    candidate = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    interview = models.ForeignKey(Interview, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    generated_follow_up = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.candidate.username} - {self.question.text[:50]}"

class CV(models.Model):
    cv = models.FileField(upload_to='resumes/', validators=[validate_file])
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True, blank=True)
    cover_letter = models.TextField(blank=True, null=True)
    applied_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('submitted', 'Submitted'),
            ('under_review', 'Under Review'),
            ('interview_scheduled', 'Interview Scheduled'),
            ('offered', 'Offered'),
            ('rejected', 'Rejected'),
        ],
        default='submitted'
    )

    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"

class CVUpload(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cvs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class CandidateProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cvs/')  # Store uploaded CV
    cv_parsed_data = models.JSONField(null=True, blank=True)  # Store parsed data from CV

    def __str__(self):
        return self.user.username

class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()

    def __str__(self):
        return f"{self.candidate.user.username} - {self.job.title}"
    
User = get_user_model()

class SkillAssessment(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    questions = models.TextField()

    def __str__(self):
        return self.name

class SkillAssessmentResult(models.Model):
    assessment = models.ForeignKey(SkillAssessment, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Profile, on_delete=models.CASCADE)
    answers = models.TextField()
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.candidate.user.username} - {self.assessment.name}"
