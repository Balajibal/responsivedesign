from django.shortcuts import render

# Create your views here.
def responsivewebsite(request):
    context = {}
    return render(request, 'myfirstapp/responsivewebsite.html', context)