from django.urls import path
from InoBooks import settings
from . import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns=[
    path('', views.home, name="home"),
    path('singup', views.singup, name="singup"),
    path('login', views.login, name="login"),
    path('handlesignup', views.handlesignup, name="handlesignup"),
    path('handlelogin', views.handlelogin, name="handlelogin"),
    path('logout', views.logout, name="logout"),
    path('upload', views.upload, name="upload"),
    path('donate', views.donate, name="donate"),
    path('handleupload',views.handleupload,name="handleupload"),
    path('search',views.search,name="search"),
    path('pay',views.pay,name="pay"),
    path('bookreport',views.bookreport,name="bookreport"),
    path('aboutus',views.aboutus,name="aboutus"),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
