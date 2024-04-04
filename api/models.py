from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Department(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    additional_info = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Patient(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    additional_info = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)


class Procedure(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    note = models.TextField(null=True)

    def __str__(self):
        return self.name


class Finance(models.Model):
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'{self.procedure.name} - {self.cost} - {self.expense} - {self.tax}'


class Schedule(models.Model):
    timestamp_start = models.DateTimeField()
    timestamp_end = models.DateTimeField()
    doctor = models.ForeignKey(Doctor, null=True, on_delete=models.SET_NULL, related_name='schedules')

    def __str__(self):
        return f'{self.doctor.full_name} - {self.timestamp_start}'


class Visit(models.Model):
    PLANNED = 'PLANNED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    VISIT_STATUS = (
        (PLANNED, PLANNED),
        (COMPLETED, COMPLETED),
        (CANCELLED, CANCELLED)
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=VISIT_STATUS)
    notes = models.TextField(null=True, blank=True)
    schedule = models.ForeignKey(Schedule, null=True, on_delete=models.SET_NULL, related_name='visits')
    rating = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.patient.full_name} - {self.procedure}'


class Notification(models.Model):
    NEW = 'New'
    READ = 'Red'
    ARCHIVED = 'Archived'

    STATUS_CHOICES = [
        (NEW, NEW),
        (READ, READ),
        (ARCHIVED, ARCHIVED)
    ]

    VISIT_CREATED = 'VISIT_CREATED'
    VISIT_CANCELLED = 'VISIT_CANCELLED'
    OTHER = 'OTHER'

    TYPE_CHOICES = [
        (VISIT_CREATED, VISIT_CREATED),
        (VISIT_CANCELLED, VISIT_CANCELLED),
        (OTHER, OTHER)
    ]

    sender = models.ForeignKey(User, related_name='sent_notifications', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_notifications', on_delete=models.CASCADE)
    message = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=NEW)
    notification_type = models.CharField(max_length=16, choices=TYPE_CHOICES, default=OTHER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sender} -> {self.recipient} : {self.message[:20]}'

    class Meta:
        ordering = ['-created_at']