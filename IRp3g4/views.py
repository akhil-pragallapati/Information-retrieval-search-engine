from urllib.request import Request
import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
import PyPDF2

def HomePage(request):
    template = loader.get_template('Home.html')
    return HttpResponse(template.render({}, request))

def searchkeywords(request):
    print('Inside def')
    #print(request)
    if 'searchkeywords' in request.POST:
        print('Inside if')
        keyword = request.POST.get("query")
        pdf_file = request.FILES['pdf-file']
        
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages) # Get the number of pages in the PDF file
        print("\n The number of pages in the file are: ", num_pages)

        text = "" # Creating an empty string to store the text
        posting_list = []
        page_text_li = []


        text2 = []
        for i in range(num_pages):  # Loop over each page in the PDF file

            page = reader.pages[i] # Get the page object
            
            page_text = page.extract_text() # Extract the text from the page
            page_text_li = page_text.split()
            #print(page_text_li)
            if keyword in page_text_li:
                posting_list = posting_list + [i+1] 
            
            text += page_text  # Append the text from the page to the string
            text2 = text2 + [page_text + "\n \n Next Page \n "]
        
        print(posting_list)
        #print(text)
        return render(request, 'pdf_contents.html', {'text2':text2, 'keyword':keyword, 'pages': num_pages, 'postinglist':posting_list} )
    return HttpResponseRedirect('/')
        

