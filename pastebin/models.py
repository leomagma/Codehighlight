from django.db import models
from pygment.style import get_all_styles
from pygment.lexers import get_all_lexers
# Create your models here.

LEXERS = [item for item in get_all_lexers if item[1]]
STYLE_CHIOCES =  sorted([[item,item] for item in get_all_styles()])
LANG_CHOICES = sorted([item[1][0],item[0]] for item in LEXERS )

class Snipper(models.Model):
	created=models.DateTimeField(auto_now_add=True)
	title= models.CharField(max_length=100,defualt='',blank=True)
	code = models.TextField()
	linenos = models.boolean(default=False)
	language = models.CharField(choices=LANG_CHOICES, default='friendly' , max_length())
	style =models.CharField(choices=STYLE_CHOICES, default='python' ,max_length='100')

	class Meta:
		odering  = [created]
