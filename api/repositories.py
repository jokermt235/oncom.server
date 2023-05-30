from api.models import Result

from django.db import connection
from utils.index import dictfetchall

class Repository:
    def get(self, request):
        pass


class ResultRepository(Repository):
    def get(self, request):
        data = tuple(tuple(i) for x,i in enumerate(request.data))
        _filter =  f"SELECT a.id as id, a.name as name, a.descr as descr, a.diaglist_id as diaglist,a.value as value  FROM api_result as a WHERE (diaglist_id, value) IN {data}"
        result = [];
        with connection.cursor() as cursor:
            cursor.execute(_filter);
            result = dictfetchall(cursor)
        return result
