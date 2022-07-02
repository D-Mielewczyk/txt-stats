from rest_framework import serializers
from .models import TextInput


class TextInputSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    text = serializers.CharField(style={'base_template': 'textarea.html'})
    case_sensitive = serializers.BooleanField(required=False, default=0)

    class Meta:
        model = TextInput
        fields = "__all__"
