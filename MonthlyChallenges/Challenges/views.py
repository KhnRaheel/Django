
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
Monthly_Challenges={
    "january":"Eat no meat for the entire month",
    "feburary":"walk for atleast 20 min a day",
    "march":"learn django atleast 30 mins aday",
    "april":"learn django atleast 30 mins aday",
    "may":"learn django atleast 30 mins aday",
    "june":"learn django atleast 30 mins aday",
    "july":"learn django atleast 30 mins aday",
    "august":"learn django atleast 30 mins aday",
    "september":"learn django atleast 30 mins aday",
    "october":"learn django atleast 30 mins aday",
    "november":"learn django atleast 30 mins aday",
    "December":None,
    

}
def index(request):
    list_item= ""
    months=list(Monthly_Challenges.keys())
    return render(request, "Challenges/index.html",{
        "months":months
    })
    
    # for month in months:
    #     capitalized_month =month.capitalize()
    #     monthpath = reverse("month-challenge",args=[month])
    #     list_item += f"<li><a href=\"{monthpath}\">{capitalized_month}</a></li>"
    
 
    # response_data=f"<ul>{list_item}</ul>"
    # return HttpResponse(response_data)

def monthly_challengeByNumber(request, month):
    months = list(Monthly_Challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("month is not valid ")
    
    redirect_Month=months[month-1]
    redirect_path= reverse ("month-challenge", args=[redirect_Month])
    return HttpResponseRedirect(redirect_path)  

def monthly_challenge(request, month):
     try:
        challenge_text=Monthly_Challenges[month]
        # response_data=f"<h1>{challenge_text}</h1>"
        # response_data=render_to_string("Challenges/challenge.html")
        # return HttpResponse(response_data)   to get rid of these two line use django import render 
        return render(request, "Challenges/challenge.html",{
            "text":challenge_text,
            # 'month_name':month.capitalize() it is good practice to only code logic in vieews.py not style the text
            "month_name":month
            })
     except:
       return HttpResponseNotFound("This month is not supported")
    