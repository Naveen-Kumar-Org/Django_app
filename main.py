import sys
from django.conf import settings
from django.urls import path
from django.http import HttpResponse
from django.core.management import execute_from_command_line

# 1. Configure Settings
settings.configure(
    DEBUG=True,
    SECRET_KEY="a-random-secret-key",
    ROOT_URLCONF=__name__,
)

# # 2. Define a View
# def home(request):
#     return HttpResponse("<h1>Hello from a Single-File Django App!</h1>")

def home(request):
    # This code to test if AI detects the bug in PR
    val = request.GET.get("value", 0)

    # and dividing by a value that might be zero.
    result = 100 / int(val) 

    return HttpResponse(f"<h1>Calculated: {result}</h1>")

# 3. Define URL Patterns
urlpatterns = [
    path("", home),
]

# 4. Execution Logic
if __name__ == "__main__":
    execute_from_command_line(sys.argv)
