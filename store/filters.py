import django_filters
import store.models
from django.db.models import Q



# class store(django_filters.FilterSet):
#    class Meta:
#        model = store.models.store
#        fields = ['title', 'description']

class Store(django_filters.FilterSet):
    price_ranga = django_filters.RangeFilter(field_name = 'storage__price', label="Цена от и до")
    #title = django_filters.CharFilter(lookup_expr = 'icontains', label='Название')
    #description = django_filters.CharFilter(lookup_expr = 'icontains', label='Описание')
    available = django_filters.BooleanFilter(method='filter_available', label = "В наличии")
    term =django_filters.CharFilter(method = 'filter_term', label='')
    
    class Meta:
        model =store.models.store
        fields = ['title', 'description', 'price_range', 'term', 'available']
        
    def filter_available(self,queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(storage__amout_ggt = 0)
        return queryset.filter(storage__amount = 0)
    
    def filter_term(self,queryset, name, value):
        criteria =Q()
        for term in value.split():
            criteria &= Q(title__icontains=term) |Q(description__icontains=term)
            
            return queryset.filter(criteria). distinct()
            
        
