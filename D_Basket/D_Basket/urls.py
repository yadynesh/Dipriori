from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^emp/', include('AdminPanel.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),

]

