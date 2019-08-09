from rest_framework.response import Response
from rest_framework.views import APIView
from .models import JobListing
from .serializers import JobListingSerializer
from .services import JobListingService


class JobListingListView(APIView):
    def get(self, request):
        job_listings = JobListingService.get_job_listings()
        serialized = JobListingSerializer(job_listings, many=True)
        return Response(serialized.data)
    

class JobListingView(APIView):
    def get(self, request, id):
        job_listing = JobListingService.get_job_listing_by_id(id)
        serialized = JobListingSerializer(job_listing)
        return Response(serialized.data)
            