import uuid
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tasks import scrape_coin_data, create_task
from celery.result import AsyncResult

@api_view(['POST'])
def start_scraping(request):
    coin_acronyms = request.data.get('coins', [])
    job_id = scrape_coin_data.delay(coin_acronyms)
    return Response({"job_id": str(job_id)})

@api_view(['GET'])
def scraping_status(request, job_id):
    result = AsyncResult(job_id)

    return Response({"job_id": job_id, "state": result.state, "output": result.result})
