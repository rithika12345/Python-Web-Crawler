from django.shortcuts import render  
from django.http import HttpResponse  
from webcrawler.functions import handle_uploaded_file  
from webcrawler.forms import StudentForm
from webcrawler.crawler import crawler
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)
        if student.is_valid():
            file=request.FILES['file']
            lines=handle_uploaded_file(request.FILES['file'])
            crawler(lines)
            return HttpResponse("Crawled successfully")
            
            
            
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form':student})  
