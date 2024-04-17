from django.conf.urls.static import static
from django.urls import path

from Migration import settings
from . import views
app_name = 'my_site'

urlpatterns=[
    path('home/',views.home, name='home'),
    path('work/', views.work, name='work'),
    path('study/',views.study,name='study'),
    path('life/', views.life, name='life'),
    path('consulting/',views.consulting, name='consulting'),
    path('signin/', views.signin, name='signin'),
    path('login/', views.view_login, name='login'),
    path('vissa/', views.vissa, name='vissa'),
    path('usa/', views.usa, name='usa'),
    path('germany/', views.germany, name='germany'),
    path('about/', views.about, name='about'),
    path('feedback/', views.feedback, name='feedback'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('look_profile/', views.look_profile, name='look_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('suggestion/', views.suggestion, name='suggestion'),
    path('Verification_code/', views.Verification_code_view, name='Verification_code'),
    # path('iamge/', views.upload_photo, name='upload_photo'),

]