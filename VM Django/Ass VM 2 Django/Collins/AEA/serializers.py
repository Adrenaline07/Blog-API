from rest_framework import serializers
from . import models

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Job
        fields = ('id', 'jobTitle', 'jobdescription', 'jobOwner',)
        read_only_fields = ('id',)

class HirerSerializer(serializers.ModelSerializer):
    class Meta:
        model= models.Hirer
        fields = ('id', 'username', 'password')
        read_only_fields = ('id',)

class FreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Freelancer
        fields = ('id', 'username', 'password', )
        read_only_fields = ('id',)