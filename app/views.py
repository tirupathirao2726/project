from django.shortcuts import render
from app.models import Article
# Create your views here.
def home(request):
	data=Article.objects.all()
	context={

	'data':data,
	}
	return render(request,'index.html',context)