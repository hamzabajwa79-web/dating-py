from django.urls import path
from . import views


urlpatterns =[
    path('own/',views.ProfileDetailView.as_view(), name='my=own'),
    path('update/',views.ProfileDetailView.as_view(), name='profile-update'),
    path('discover/',views.potential_matches, name='discover-profiels'),
    path('swipe/<int:profile_id>/<str:action>/', views.swipe, name='swipe'),
    

]