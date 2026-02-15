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

# 2. Define a View
def home(request):
    return HttpResponse("<h1>Hello from a Single-File Django App!</h1>")

# 3. Define URL Patterns
urlpatterns = [
    path("", home),
]

# 4. Execution Logic
if __name__ == "__main__":
    execute_from_command_line(sys.argv)
