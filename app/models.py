from django.db import models


class Branch(models.Model):
    id = models.TextField(primary_key=True)
    university = models.TextField()
    branch = models.TextField()

    def __str__(self):
        return f"{self.university} - {self.branch}"

class Subject(models.Model):
    id = models.TextField(primary_key=True)
    year = models.TextField()
    semester = models.TextField()
    name = models.TextField()
    code = models.TextField()
    branches = models.ManyToManyField('Branch', through='SubjectBranch')

    def __str__(self):
        return self.name

class College(models.Model):
    id = models.TextField(primary_key=True)
    password = models.TextField()
    #from form
    email=models.TextField()
    name = models.TextField()
    code=models.TextField(unique=True)
    principal=models.TextField()
    mobile = models.TextField()
    role = models.TextField()
    address=models.TextField()
    state=models.TextField()
    city=models.TextField()
    pincode=models.TextField()
    affiliation=models.TextField()
    website=models.TextField()
    image = models.FileField(null=True, blank=True)
    #auto set
    status=models.TextField()
    payment=models.TextField()
    branches = models.ManyToManyField(Branch, through='CollegeBranch')

    #17
   
    def __str__(self):
        return self.name

class Adminstartor(models.Model):
    id = models.TextField(primary_key=True)
    email=models.TextField()
    password = models.TextField()
    name = models.TextField()
    mobile = models.TextField()
    role = models.TextField()
    image = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.name
 

class CollegeBranch(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('college', 'branch')

    def __str__(self):
        return f"{self.college.name} - {self.branch.branch}"
    
class SubjectBranch(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('subject', 'branch')

    def __str__(self):
        return f"{self.subject.name} - {self.branch.branch}"
  