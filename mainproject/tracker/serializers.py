from .models import tracker, landing, tags, mquotes # Import models from the tracker app
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class TrackerSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='name',          # ✅ match landing.name (primary key)
        queryset=landing.objects.all()
    )
    # tag = serializers.CharField(source="tag.tag")
    class Meta:
        model = tracker
        fields = '__all__'


class LandingSerializer(ModelSerializer):
    class Meta:
        model = landing
        fields = '__all__'


class TagsSerializer(ModelSerializer):
    class Meta:
        model = tags
        fields = '__all__'
      
class MQuotesSerializer(ModelSerializer):
    class Meta:
        model = mquotes
        fields = '__all__'