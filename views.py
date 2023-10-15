from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
def results(request):
    return HttpResponse("No. of Results: (by Code Warriors !!)")
def mean(request):
    return HttpResponse("These are the mean Salaries: ")
def median(request):
    return HttpResponse("These are the median Salaries: ")
def salary25(request):
    return HttpResponse("These are 25percentile Salaries: ")
def salary75(request):
    return HttpResponse("these are 75percentile salary: ")

