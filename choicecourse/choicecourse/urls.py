from django.conf.urls import include, url
from django.contrib import admin

app_name = 'choice_course'

# Examples:
# url(r'^$', 'choisecourse.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('course.urls')),
]