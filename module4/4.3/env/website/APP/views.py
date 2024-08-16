from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    return HttpResponse('Hello World!')

def generate_numbers(request):
    num1=random.randint(0,3)
    num2=random.randint(0,3)
    num3=random.randint(0,3)
    if num1==num2==num3:
        return HttpResponse(f'[{num1}, {num2}, {num3}] Победа, все три числа равны!')
    else:
        return HttpResponse(f'[{num1}, {num2}, {num3}] Повезет в следующий раз!')
       
    # if num1==num2==num3:
    #     response=f'[{num1}, {num2}, {num3}] Победа, все три числа равны [{num1}]!'
    # else:
    #     response=f'[{num1}, {num2}, {num3}] Повезет в следующий раз!'
    # return HttpResponse(response)

# Create your views here.
