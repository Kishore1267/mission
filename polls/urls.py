from django.urls import path
from mission import settings
from .import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('',views.index,name='index'),
    path('success/',views.success,name='success'),

    path('contact/',views.contact,name='contact'),

    path('about/',views.about,name='about'),

    path('student/',views.student_data,name='student'),

    path('receipes/',views.receipes,name='receipes'),

    path('delete_receipe/<id>/',views.delete_receipe,name='delete_receipe'),

    path('update_receipe/<id>/',views.update_receipe,name='update_receipe'),

    path('login/',views.login_page,name='login_page'),

    path('logout/',views.logout_page,name='logout_page'),

    path('register/',views.register,name='register'),

    path('students/',views.get_students,name='students'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += staticfiles_urlpatterns()
