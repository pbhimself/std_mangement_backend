from django.db import models

# Create your models here.

class SubjectMetaData(models.Model):
    teacher_name = models.CharField(max_length=100)
    teacher_email = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    subject_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.teacher_name} - {self.class_name} - {self.division} - {self.subject_name}"
    
class StudentMetaData(models.Model):
    student_name = models.CharField(max_length=100)
    subject_data = models.ForeignKey(SubjectMetaData, on_delete=models.CASCADE)
    subject_marks = models.IntegerField()
    total_marks = models.IntegerField()

    def __str__(self):
        return f"{self.student_name} - {self.subject_data} - {self.subject_marks} - {self.total_marks}"

    