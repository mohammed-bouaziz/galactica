from rest_framework.viewsets import ModelViewSet
from .serializers import RoouteSerializer
from .models import Routes
from rest_framework.decorators import action
from .utils import get_data, find_fastes_algo
from rest_framework.response import Response

class RouteViewset(ModelViewSet):
    serializer_class = RoouteSerializer
    queryset = Routes.objects.all()

    @action(detail=False, methods=['post'])
    def find_fastest_way(self, request):
        departure, autonomy = get_data()
        routes = self.get_queryset()
        arrival = request.data.get('arrival')
        departure = departure
        autonomy = autonomy
        duration, path = find_fastes_algo(routes, autonomy, departure, arrival)
        return Response({
            'duration': duration,
            'route': path
        })
        


        
        
        
        



        
