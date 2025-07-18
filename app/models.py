from django.db import models


class Branch(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=False)
    university = models.CharField(max_length=255)
    branch = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.university} - {self.branch}"

class Subject(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=False)
    year = models.CharField(max_length=255)
    semester = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    branches = models.ManyToManyField(Branch)

    def __str__(self):
        return self.name

class College(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=False)
    password =models.CharField(max_length=255)
    #from form
    email=models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    principal=models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    pincode=models.CharField(max_length=255)
    affiliation=models.CharField(max_length=255)
    website=models.CharField(max_length=255)
    image = models.FileField(null=True, blank=True)
    #auto set
    status=models.CharField(max_length=255)
    payment=models.CharField(max_length=255)
    branches = models.ManyToManyField(Branch)

    #17
   
    def __str__(self):
        return self.name

class Adminstartor(models.Model):
    id = models.CharField(max_length=255, primary_key=True, db_index=False)
    email=models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.name
 
