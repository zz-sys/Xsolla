from rest_framework.pagination import LimitOffsetPagination


class StandartSetPagination(LimitOffsetPagination):
    max_limit = 100
    default_limit = 100
    limit_query_param = 'limit'
    offset_query_param = 'offset'
