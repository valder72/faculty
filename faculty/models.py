from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=100)
    coordinator_contact = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="programs"
    )

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=150)
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE, related_name="disciplines"
    )

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="teachers"
    )

    def __str__(self):
        return self.name


class FacultyInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    dean_name = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.title


class ExchangeProgram(models.Model):
    university = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    languages = models.CharField(max_length=100)
    places = models.IntegerField()
    deadline = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.university
