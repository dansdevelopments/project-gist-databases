from .models import Gist
from datetime import datetime
def search_gists(db_connection, **kwargs):
    datetime_format = "%Y-%m-%dT%H:%M:%SZ"
    params = kwargs
    gists_data = db_connection.execute("SELECT * FROM gists")
    result = [Gist(row) for row in gists_data]
    if "github_id" in params:
        result = [gist for gist in result if gist.github_id == params['github_id']]
    
    if "created_at" in params:
        result = [gist for gist in result if datetime.strptime(gist.created_at, datetime_format) == params['created_at']]
    
    if "created_at__gt" in params:
        result = [gist for gist in result if datetime.strptime(gist.created_at, datetime_format) > params['created_at__gt']]

    if "created_at__gte" in params:
        result = [gist for gist in result if datetime.strptime(gist.created_at, datetime_format) >= params['created_at__gte']]
    
    if "created_at__lt" in params:
        result = [gist for gist in result if datetime.strptime(gist.created_at, datetime_format) < params['created_at__lt']]

    if "created_at__lte" in params:
        result = [gist for gist in result if datetime.strptime(gist.created_at, datetime_format) <= params['created_at__lte']]

    if "updated_at" in params:
        result = [gist for gist in result if datetime.strptime(gist.created_at, datetime_format) == params['updated_at']]
    
    if "updated_at__gt" in params:
        result = [gist for gist in result if datetime.strptime(gist.created_at, datetime_format) > params['updated_at__gt']]

    if "updated_at__gte" in params:
        result = [gist for gist in result if datetime.strptime(gist.created_at, datetime_format) >= params['updated_at__gte']]
    
    if "updated_at__lt" in params:
        result = [gist for gist in result if datetime.strptime(gist.created_at, datetime_format) < params['updated_at__lt']]

    if "updated_at__lte" in params:
        result = [gist for gist in result if datetime.strptime(gist.created_at, datetime_format) <= params['updated_at__lte']]

    return result
