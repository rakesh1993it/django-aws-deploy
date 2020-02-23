from django import forms
from image.models import Article

class ArticleForm(forms.ModelForm):

	class Meta:
		model = Article 
		fields = ('title','picture','pub_date')