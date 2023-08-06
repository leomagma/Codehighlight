from rest_framework import serializers
from pastbin.model import Snippet


class snippetSerializer(serializers.ModelSerializer):
	class Meta:
		model = snippet
		fields = ['id','title','code','linenos','language','style']
