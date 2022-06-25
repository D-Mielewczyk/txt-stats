from rest_framework import serializers
from .models import TextInput


class TextInputSerializer(serializers.ModelSerializer):
    text = serializers.CharField(max_length=int(1e9))
    case_sensitive = serializers.BooleanField(required=False, default=0)

    class Meta:
        model = TextInput
        fields = "__all__"
