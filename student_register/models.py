from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model): 
    GENDER = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('O', 'Other'),
        ('Prefer', 'Prefer not to say'),
    ]

    PATH =[
        ('FullStack', 'FullStack'),
        ('Front-End', 'Front-End'),
        ('Back-End', 'Back-End'),
    ]

    fullname = models.CharField(max_length=100)
    number = models.IntegerField()
    mobile = PhoneNumberField(region="TR")
    email = models.EmailField(max_length=254)
    gender = models.CharField(max_length=50, choices=GENDER)
    path = models.CharField(max_length=50, choices=PATH)


    def __str__(self):
        return f"{self.fullname} - {self.number}"