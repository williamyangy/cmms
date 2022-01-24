from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.LimitOffsetPagination):
    # override pagination parameters to fit with datatables params
    limit_query_param = 'length'
    offset_query_param = 'start'
