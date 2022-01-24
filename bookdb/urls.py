"""bookdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from bms import views, rest
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
import notifications.urls

router = routers.DefaultRouter()
router.register(r'users', rest.UserViewSet)
router.register(r'schools', rest.SchoolViewSet)
router.register(r'courseinfo', rest.CourseInfoViewSet)
router.register(r'courses', rest.SemesterCourseViewSet)
router.register(r'publishers', rest.PublisherViewSet)
router.register(r'books', rest.BookViewSet)
router.register(r'materials', rest.MaterialViewSet)
router.register(r't', rest.TenderExerciseListView)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include('bms.urls')),
    path('api/v2/', include(router.urls)),
    path('api/users/', rest.UserList.as_view()),
    path('api/publishers/', rest.PublisherList.as_view()),
    path('api/books/', rest.BookList.as_view()),
    path('api/materials/', rest.MaterialList.as_view()),
    path('api/materials/find', rest.MaterialListByMostRecentCourse.as_view()),
    path('api/courses/<int:pk>/', rest.CourseDetail.as_view()),
    path('api/login', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LoginView.as_view(), name='logout'),
    path('admin/', admin.site.urls),
    # path('course/', include('courses.urls'))
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('login/forgot-password.html', views.forgot_password, name='forgot_password'),
    path('logout/forgot-password.html', views.forgot_password, name='forgot_password'),

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
