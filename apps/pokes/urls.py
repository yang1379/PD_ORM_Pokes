from django.conf.urls import url
from . import views
def test(request):
    print 'sdkdkjsjdkdjksdjkj'

urlpatterns = [
#     url(r'^add_power$', views.add_power),
#     url(r'^add_power_validate$', views.add_power_validate),
#     url(r'^add_hero$', views.add_hero),
#     url(r'^add_hero_validate$', views.add_hero_validate),
#     url(r'^show_hero/(?P<hero_id>\d+)$', views.show_hero),
    url(r'^poke/(?P<poke_id>\d+)$', views.poke_user),
#     url(r'^unlike_hero/(?P<hero_id>\d+)$', views.unlike_hero),
    url(r'^logout$', views.logout),
    url(r'^', views.dashboard)
]