from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import re

# Create your views here.


# Task 1
def my_view(request):
    text = request.GET.get('text', '')
    pattern = re.compile(r'[Rr]b+r')
    matches = pattern.findall(text)
    return render(request)

#Task 2

def credit_card(card_number: str):
    if not re.match(r'^\d{4}-\d{4}-\d{4}-\d{4}$', card_number):
        return False
    card_number = card_number.replace('-', '')

    return sum(int(digit) if i % 2 == 0 else (int(digit) * 2 - 9 if int(digit) * 2 > 9 else int(digit) * 2)
               for i, digit in enumerate(card_number[::-1])) % 10 == 0

# Task 3

def validate_email(email: str):
    pattern = r'^[a-zA-Z0-9]+([_-][a-zA-Z0-9]+)*@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email)

#Task4

def validate_login(login: str):
    pattern = r'^[a-zA-Z0-9]{2,10}$'
    return re.match(pattern, login)
