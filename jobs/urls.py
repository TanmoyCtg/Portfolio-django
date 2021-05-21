from django.urls import path

from .views import jobs,detail
urlpatterns = [
	path('', jobs, name='home'),
	path('jobs/<int:job_id>', detail, name="detail"),
]