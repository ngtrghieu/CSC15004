from django.shortcuts import render

def home(request):
    if request.method=='POST':
          input=request.POST.get('input')
          print(input)
    return render(request, "final_lab/index.html")
