from rest_framework import serializers

from .models import TextInput
from .utils import *


class TextInputSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    text = serializers.CharField(style={'base_template': 'textarea.html'})
    case_sensitive = serializers.BooleanField(required=False, default=0)

    class Meta:
        model = TextInput
        fields = "__all__"


class AnalyzeTextSerializer(TextInputSerializer):
    occurrences = serializers.SerializerMethodField()
    palindromes = serializers.SerializerMethodField()

    class Meta:
        model = TextInput
        fields = ["title", "text", "occurrences", "palindromes", "owner"]

    @staticmethod
    def get_occurrences(text_input):
        return count_words(text_input.text, text_input.case_sensitive)

    @staticmethod
    def get_palindromes(text_input):
        words = count_words(text_input.text, text_input.case_sensitive)
        return extract_palindromes(words)
