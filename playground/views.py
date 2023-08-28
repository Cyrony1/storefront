from django.shortcuts import render
from django.http import HttpResponse
from store.models import Customer

def say_hello(request):
    query_set = Customer.objects.all()

    for customer in query_set:
        print(customer)

        return render(request, 'hello.html')


