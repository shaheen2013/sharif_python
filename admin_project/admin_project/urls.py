
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('admin_app.urls')),
    path('survey/',include('survey_tool.urls'))
]
