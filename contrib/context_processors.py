from django.contrib.auth.models import User

def current_user(request):
    return {'current_user': request.user}

