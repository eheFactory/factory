from rest_framework import serializers

class vlAveragingBlurSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
#    originalImage = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=False)
   resultImage = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=False)

class vlMedianBlurSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
#    originalImage = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=False)
   resultImage = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=False)

class vlGaussianBlurSerializer(serializers.Serializer):
   """Your data serializer, define your fields here."""
#    originalImage = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=False)
   resultImage = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=False)