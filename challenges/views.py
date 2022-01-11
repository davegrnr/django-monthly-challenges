from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None
}

# Create your views here.


# def january(request):
#     return HttpResponse("Eat no meat for the entire month")


# def february(request):
#     return HttpResponse("Run 30 miles")


# def march(request):
#     return HttpResponse("Learn Django for 20 mins every day")

def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    except:
        raise Http404()

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
