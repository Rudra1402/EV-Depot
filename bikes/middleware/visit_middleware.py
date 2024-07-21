# your_app/middleware/visit_middleware.py

from django.utils.deprecation import MiddlewareMixin

class VisitMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Dictionary to store visit counts
        visit_counts = {
            'bikes': int(request.COOKIES.get('bikes_visits', 0)),
            'cars': int(request.COOKIES.get('cars_visits', 0)),
            'trucks': int(request.COOKIES.get('trucks_visits', 0)),
        }

        # Determine which app is being visited and update the count
        if 'bikes' in request.path:
            visit_counts['bikes'] += 1
        elif 'cars' in request.path:
            visit_counts['cars'] += 1
        elif 'trucks' in request.path:
            visit_counts['trucks'] += 1

        # Set the updated visit counts in cookies
        request.visit_counts = visit_counts

    def process_response(self, request, response):
        if hasattr(request, 'visit_counts'):
            response.set_cookie('bikes_visits', request.visit_counts['bikes'])
            response.set_cookie('cars_visits', request.visit_counts['cars'])
            response.set_cookie('trucks_visits', request.visit_counts['trucks'])
        return response
