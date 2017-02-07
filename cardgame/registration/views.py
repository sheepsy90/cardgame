import random
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template.context import RequestContext
from cards.models.general_cards import CharacterCard, StarterCard, Card
from registration.models import LivingCharacter


def check_is_user_loggedin(request):
    return "AnonymousUser" != request.user.__str__()


def landingpage(request):
    if check_is_user_loggedin(request):
        return HttpResponseRedirect("/mainpage")
    else:
        requestcontext = RequestContext(request)
        some_random_cards = CharacterCard.objects.all()

        four_cards = random.sample(some_random_cards, 4)
        requestcontext["some_random_cards"] = four_cards
        return render_to_response('index.html', requestcontext)



@login_required(login_url="/")
def character_choosing(request):
    requestcontext = RequestContext(request)
    all_characters = CharacterCard.objects.all()
    requestcontext['choosable_character'] = all_characters
    return render_to_response('character_choosing.html', requestcontext)

@login_required(login_url="/")
def choose(request, character_id):
    requestcontext = RequestContext(request)

    starter_cards = StarterCard.objects.filter(character__id=character_id)
    print starter_cards

    #mycharacter = LivingCharacter(user=request.user, chosen_character=character)
    #mycharacter.save()

    return HttpResponseRedirect("/mainpage", requestcontext)


@login_required(login_url="/")
def main_page(request):
    request_context = RequestContext(request)

    # Check if the user actually already has a LivingCharacter
    if not LivingCharacter.objects.filter(user=request.user).exists():
        return HttpResponseRedirect("/character_choosing", request_context)

    # Otherwise we lead him to the main page where he can perform actions
    mycharacter = LivingCharacter.objects.get(user=request.user)
    request_context['living_character'] = mycharacter

    return render_to_response('main_page.html', request_context)
