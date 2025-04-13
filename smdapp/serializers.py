from rest_framework import serializers
from . import models

class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StudentMetaData
        fields = ['student_name', 'subject_marks', 'total_marks']  # Removed 'subject_data'

class SubjectMetaDataSerializer(serializers.ModelSerializer):
    student_data = StudentDataSerializer(many=True)

    class Meta:
        model = models.SubjectMetaData
        fields = ['teacher_name', 'teacher_email', 'class_name', 'division', 'subject_name', 'student_data']

    def create(self, validated_data):
        student_data = validated_data.pop('student_data')
        subject_metadata = models.SubjectMetaData.objects.create(**validated_data)
        for student in student_data:
            # Automatically associate subject_metadata with each student
            models.StudentMetaData.objects.create(subject_data=subject_metadata, **student)
        return subject_metadata
    
class SubjectMetaDataSerializer2(serializers.ModelSerializer):
    class Meta:
        model = models.SubjectMetaData
        fields = ['class_name', 'division', 'subject_name']
