from django.shortcuts import render, HttpResponse, redirect
import json
from django.core import serializers
import requests
from .models import Movie
import math
import urllib.parse

# response = requests.get("http://api.open-notify.org/iss-now.json")
# print(response.status_code)
# OMDb API Key = "KEY HERE"
# How to Use = http://www.omdbapi.com/?i=tt3896198&apikey="KEY HERE"
#                          source        movie id         api key

def index(request):
    return render(request, "index.html")

def search(request):
    # print(request.POST)
    user_input = urllib.parse.quote_plus(request.POST['search'])
    # print(user_input)
    response = requests.get(f"https://api.whatismymovie.com/1.0/?api_key="KEY HERE"&text={user_input}").content
    # print(response)
    return HttpResponse(response, content_type='application/json')


















# def database(request):
#     letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#     page_number = 1
#     for i in range(len(letters)):
#         for x in range(len(letters)):
#             response = requests.get(f"http://www.omdbapi.com/?apikey="KEY HERE"&type=movie&s={letters[i]}{letters[x]}&page={page_number}")
#             movie = json.loads(response.text)
#             for y in range(1, math.floor(int(movie['totalResults']) / 10)):
#                 response = requests.get(f"http://www.omdbapi.com/?apikey="KEY HERE"&type=movie&s={letters[i]}{letters[x]}&page={page_number}")
#                 movie = json.loads(response.text)
#                 for z in range(len(movie['Search'])):
#                     if (movie['Search'][z]['imdbID'] in Movie.objects.all()):
#                         continue
#                     else:
#                         Movie.objects.create(
#                             title = movie['Search'][z]['Title'],
#                             year = movie['Search'][z]['Year'],
#                             imdbID = movie['Search'][z]['imdbID'],
#                         )
#                 page_number += 1