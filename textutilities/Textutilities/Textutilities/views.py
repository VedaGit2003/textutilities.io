from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    cap=request.POST.get('cap','off')
    newline=request.POST.get('new_line','off')
    space=request.POST.get('space','off')
    charcount=request.POST.get('charcount','off')
    # print(removepunc)
    print(djtext)
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        djtext=analyzed
     #    return render(request,'analyze.html',params)
    if(cap=='on'):
        analyzed=''
        for char in djtext:
                analyzed+=char.upper()
        params={'purpose':'Capitalize','analyzed_text':analyzed}
        djtext=analyzed
     #    return render(request,'analyze.html',params)
    if(newline=='on'):
         analyzed=''
         for char in djtext:
              
              if char !='\n' and char !='\r':
                   analyzed+=char
              else:
                   print("no")
              
         params={'purpose':'Capitalize','analyzed_text':analyzed}
         djtext=analyzed
         #return render(request,'analyze.html',params)
    if(space=='on'):
         analyzed=''
         for index,char in enumerate(djtext):
              if djtext[index]==' ' and djtext[index]==' ':
                   pass
              else:
                   analyzed+=char
         params={'purpose':'Remove space','analyzed_text':analyzed}
         #return render(request,'analyze.html',params)
    if(charcount=='on'):
         analyzed=''
         for index,char in enumerate(djtext):
              if djtext[index]==' ' and djtext[index]==' ':
                   pass
              else:
                   analyzed+=char
         
         params={'purpose':'charcount','analyzed_text':analyzed,'char_count':len(analyzed)}
         #return render(request,'analyze.html',params)
    
    if (removepunc!='on' and cap!='on' and newline!='on' and space!='on' and
        charcount!='on'):
         return HttpResponse('Plese select operation')
    return render(request,'analyze.html',params)


    #Analyze the text
#     else:
#         return HttpResponse("error")

# 
# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")

