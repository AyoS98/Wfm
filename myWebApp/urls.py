from django.urls import path
from .views import  *

urlpatterns = [
    # path('', home2, name= 'home'),  # function based view
    path('', home, name= 'WfmAnonContact'),  
    # path('artisanform', home3, name= 'artisanform'),
    # path('cr7', home5, name= 'cr7'),
    # path('messi', home4, name= 'messi'),
    # path('login', login, name= 'login'),
    # path('register', register, name= 'register'),
    # path('logout', logout, name= 'logout'),
    path('success', success, name= 'success'),
    



]