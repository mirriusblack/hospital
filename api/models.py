from django.db import models


class Specialization(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
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
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    note = models.TextField(null=True)

    def __str__(self):
        return self.name


class Visit(models.Model):
    PLANNED = 'PLANNED'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

    VISIT_STATUS = (
        (PLANNED, PLANNED),
        (COMPLETED, COMPLETED),
        (CANCELLED, CANCELLED)
    )

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='visits')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='visits')
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, null=True, blank=True)
    visit_date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=VISIT_STATUS)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.doctor.full_name} - {self.patient.full_name} - {self.visit_date_time}'