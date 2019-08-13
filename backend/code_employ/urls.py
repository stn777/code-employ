from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('user/', include('apps.user.api.urls')),
    re_path('applicant/', include('apps.applicant.api.urls')),
    re_path('company/', include('apps.company.api.urls')),
    re_path('job-listing/', include('apps.job_listing.api.urls'))
]
