from django.urls import path, include
from rest_framework import routers
from .views import SenssorListView, SensorView, MeasurementAddView


router = routers.DefaultRouter()
#router.register('sensors',SenssorListView.as_view(), basename='sensors')

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SenssorListView.as_view(), name='sensors_list'),
    path('sensors/<pk>/', SensorView.as_view(), name='sensor_details'),
    path('measurements/', MeasurementAddView.as_view(), name='measure_add'),
    #path('',include(router.urls)),
]
