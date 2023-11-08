from django_filters import rest_framework as filters

from apps.cars.models import CarModel


class CarFilter(filters.FilterSet):
    # price_lt = filters.NumberFilter('price', 'lt')
    # price_gt = filters.NumberFilter('price', 'gt')
    # price_lte = filters.NumberFilter('price', 'lte')
    # price_gte = filters.NumberFilter('price', 'gte')
    # price_range = filters.RangeFilter('price')
    # seats_lt = filters.NumberFilter('seats', 'lt')
    # seats_gt = filters.NumberFilter('seats', 'gt')
    # seats_lte = filters.NumberFilter('seats', 'lte')
    # seats_gte = filters.NumberFilter('seats', 'gte')
    # seats_range = filters.RangeFilter('seats')
    # engine_volume_lt = filters.NumberFilter('engine_volume', 'lt')
    # engine_volume_gt = filters.NumberFilter('engine_volume', 'gt')
    # engine_volume_lte = filters.NumberFilter('engine_volume', 'lte')
    # engine_volume_gte = filters.NumberFilter('engine_volume', 'gte')
    # engine_volume_range = filters.RangeFilter('engine_volume')
    # brand_contains = filters.CharFilter('brand', 'icontains')
    # brand_startswith = filters.CharFilter('brand', 'startswith')
    # brand_endswith = filters.CharFilter('brand', 'endswith')
    # body_type_contains = filters.CharFilter('body_type', 'icontains')
    # body_type_startswith = filters.CharFilter('body_type', 'startswith')
    # body_type_endswith = filters.CharFilter('body_type', 'endswith')
    order = filters.OrderingFilter(
        fields=(
            'id',
            'brand',
            'price',
            'body_type',
            'seats',
            'engine_volume',
        )
    )
    class Meta:
        model = CarModel
        fields = {
            'price': ('gt', 'lt', 'lte', 'gte'),
            'seats': ('gt', 'lt', 'lte', 'gte'),
            'engine_volume': ('gt', 'lt', 'lte', 'gte'),
            'brand': ('contains', 'startswith', 'endswith'),
            'body_type': ('contains', 'startswith', 'endswith')
        }
