from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'hospital_recommend_api'	# namespace of this urls.py

urlpatterns = [
	url(r'^$', views.index, name="index"),	
	url(r'^hospital_recommend_api/$', views.HospitalRecommend.as_view(), name="hospital_recommend_api"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
