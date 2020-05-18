from rest_framework import serializers

from jobs.models import WorkHistory, EducationHistory, Reference

class WorkHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = '__all__'

class EducationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationHistory
        fields = '__all__'

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = '__all__'
