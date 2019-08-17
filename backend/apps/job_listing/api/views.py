from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..business.services import JobListingService
from ..business.selectors import JobListingSelector
from .serializers import (
    JobListingSerializer, JobListingSearchFilterSerializer,
    JobListingSearchResponseSerializer, JobListingEditSerializer
)


class JobListingPagedListView(APIView):
    def post(self, request):
        search_filter = JobListingSearchFilterSerializer(request.data)
        search_response = JobListingSelector.get_paged_job_listings(search_filter)
        serialized = JobListingSearchResponseSerializer(search_response)
        return Response(serialized.data)


class JobListingView(APIView):
    def get(self, request, id):
        job_listing = JobListingSelector.get_job_listing_by_id(id)
        serialized = JobListingSerializer(job_listing)
        return Response(serialized.data)


class JobListingCreateView(APIView):
    def post(self, request):
        serialized = JobListingEditSerializer(request.data)
        job_listing_id = JobListingService.create_job_listing(serialized)
        return Response(job_listing_id)


class JobListingEditView(APIView):
    def put(self, request, id):
        serialized = JobListingEditSerializer(request.data)
        job_listing_id = JobListingService.update_job_listing(id, serialized)
        return Response(job_listing_id)


class JobListingDeleteView(APIView):
    def delete(self, request, id):
        JobListingService.delete_job_listing(id)
        return Response(status=status.HTTP_200_OK)


class JobListingPublishView(APIView):
    def put(self, request, id):
        pass


class JobListingActivateView(APIView):
    def put(self, request, id):
        pass
