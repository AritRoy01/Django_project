from rest_framework import serializers
from home.models import Project

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Project
        fields="__all__"