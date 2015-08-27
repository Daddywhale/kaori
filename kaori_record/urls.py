from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'competition_result$', views.competition_result, name='competition_result'),
    url(r'pockemon_result$', views.pockemon_result, name='pockemon_result'),
    url(r'pockemon$', views.pockemon, name='pockemon'),
    url(r'ranking_result$', views.ranking_result, name='ranking_result'),
    url(r'individual_record_result$', views.individual_record_result, name='individual_record_result'),
    url(r'manage$', views.manage, name='manage'),
    url(r'competition$', views.competition, name='competition'),
    url(r'ranking$', views.ranking, name='ranking'),
    url(r'individual_record$', views.individual_record, name='individual_record'),
    url(r'^index$', views.index, name='index'),
    url(r'^$', views.index, name='index'),
]


