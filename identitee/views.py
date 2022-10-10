from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from identitee.forms import CreateNewIdentity, CreateNewCard
from identitee.models import Identitee
from django import forms
from datetime import datetime
from .models import Card


def add_identity(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("post")
        # return HttpResponse('/thanks/')
        # create a form instance and populate it with data from the request:
        form = CreateNewIdentity(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # form.cleaned_data["telephone"] = str(form.cleaned_data["telephone"])
            email = form.cleaned_data["email"]
            form.save()
            # result = Identitee.objects.get(email=email)
            request.session['sent_email'] = email
            # print("valid")
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect('add_card')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CreateNewIdentity()
    # form = CreateNewIdentity()
    return render(request, 'identitee/identitee.html', {
        'form': form
    })


def add_card(request):
    selected_sent_id = request.session.get('sent_email')
    print(f"selected_sent_id {selected_sent_id}")
    form = CreateNewCard()
    if selected_sent_id:
        form.fields['expiration'].widget = forms.HiddenInput()
        if request.method == 'POST':
            form = CreateNewCard(request.POST)
            # print(form.data.get('month'))
            # form.data['expiration'] = str(request.POST.get('month')) + ' - ' + str(request.POST.get('year'))
            # print(form.data)
            # form.data['num'] = request.POST.get('num')
            if form.is_valid():
                # print(request.POST.get('month'))
                form.cleaned_data['expiration'] = str(request.POST.get('month')) + \
                                                  ' - ' + str(request.POST.get('year'))
                # print(form.cleaned_data['expiration'])
                identitee_id = Identitee.objects.get(email=selected_sent_id)
                # # print(id_identitee)
                # form.cleaned_data['identitee_id'] = id_identitee
                card = Card(
                    titulaire=form.cleaned_data['titulaire'],
                    numero=form.cleaned_data['numero'],
                    montant=form.cleaned_data['montant'],
                    expiration=form.cleaned_data['expiration'],
                    cryptogramme=form.cleaned_data['cryptogramme'],
                    identitee_id=identitee_id,
                )
                card.save()
                # print(form.cleaned_data)
                # form.save()
                print('card inserted')
                return redirect('success')
    return render(request, 'card/card.html', {
        'form': form,
        'month': range(1, 13),
        'year': range(datetime.now().year, datetime.now().year + 11),
    })


def success(request):
    return render(request, 'sucess/success.html')