from django.conf import settings

def app_name(request):
    app_name = settings.APP_SHOW_NAME
    return {"app_name": app_name}