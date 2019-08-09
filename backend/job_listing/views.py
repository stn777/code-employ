from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import JobListing
from .serializers import JobListingSerializer


class JobListingListView(APIView):
    def get(self, request):
        job_listings = JobListing.objects.all()
        serialized = JobListingSerializer(job_listings, many=True)
        return Response(serialized.data)
    

class JobListingView(APIView):
    def get_job_listing(self, id):
        try:
            return JobListing.objects.get(id=id)
        except JobListing.DoesNotExist:
            raise Http404

    def get(self, request, id):
        job_listing = self.get_job_listing(id)
        serialized = JobListingSerializer(job_listing)
        return Response(serialized.data)
            