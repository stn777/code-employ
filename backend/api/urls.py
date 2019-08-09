from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('user/', include('user.urls')),
    re_path('applicant/', include('applicant.urls')),
    re_path('company/', include('company.urls')),
    re_path('job-listing/', include('job_listing.urls'))
]
