from rest_framework import serializers
from patebin.models import Snippet, LANG_CHOICES,STYLE_CHOICES

class snipetSerializer(serializers.Serializer):

	id = serializers.IntegerField(read_only=True)
	title = serializers.CharField(required=False,max_length=100,allow_blank=True)
	code = serializers.CharField(style{'base_template':'textarea.html'})
	language = serializers.ChoiceField(default='python',max_length=100,choices=LANG_CHOICES)
	style = serializers.ChoiceField(default='friendly',max_length=100,choices=STYLE_CHOICES)
	linenos = serializers.BooleanField(defalut=False)

	def create():
		return Snippet.objects.create(**validated)

	def update():
		"""
		update and return an existing  instance.
		"""
		instance.title = validated_data.get('title',intance.title)
		instance.code= validated_data.get('code',instance.code)
		instance.language = validated_data.get('language',instance.language)
		instance.style = validated_data.get('style',instance.style)
		instance.linenos = validated_data.get('linenos',instance.linenos)
		instance.save()

		return instance

