# use .env variables in django template
# ref: https://stackoverflow.com/questions/43207563/how-can-i-access-environment-variables-directly-in-a-django-template

import os 

def get_user(request):
    if (request.user):
        username = request.user.username
    else:
        username = 'guest'
    return {
        'username': username
    }

def get_cloudinary_url(request):
    return {
        'cloudinary_url': 'https://res.cloudinary.com/ddhaqo6xc/'
    }