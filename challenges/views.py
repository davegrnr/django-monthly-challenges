from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february":  "Run 30 miles",
    "march": "Learn Django for 20 mins each day",
    "april": "Eat not meat for entire month",
    "may": "Run 30 miles",
    "june": "Learn Django for 20 mins each day",
    "july": "Eat no meat for the entire month",
    "august": "walk every day",
    "september": "walk the dogs every day",
    "october": "take Finn to play soccer",
    "november": "Eat no meat",
    "december": "Learn Django"
}

# Create your views here.


# def january(request):
#     return HttpResponse("Eat no meat for the entire month")


# def february(request):
#     return HttpResponse("Run 30 miles")


# def march(request):
#     return HttpResponse("Learn Django for 20 mins every day")

def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponse("This month is not supported!")

# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == "january":
#         challenge_text = "Eat no meat for the entire month"
#     elif month == "february":
#         challenge_text = "Run 30 miles"
#     elif month == "march":
#         challenge_text = "Learn Django for 20 mins every day"
#     else:
#         return HttpResponseNotFound("This month is not supported")
#     return HttpResponse(challenge_text)
