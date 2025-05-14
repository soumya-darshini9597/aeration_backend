import csv
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Areation

@csrf_exempt
def download_aeration_csv(request):
    if request.method == 'GET':
        # Prepare HTTP response with CSV headers
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="areation_data.csv"'

        writer = csv.writer(response)
        # header row
        writer.writerow(['Date', 'Time', 'State'])

        # write one row per Areation, ordered by date & time
        for item in Areation.objects.all().order_by('date', 'time'):
            writer.writerow([
                item.date.isoformat(),
                item.time.strftime('%H:%M:%S'),
                item.state
            ])

        return response

    return HttpResponse("Invalid request method", status=405)
