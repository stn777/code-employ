from django.db import models
from collections import namedtuple


PagedResult = namedtuple('PagedResult', ['items', 'record_count'])


class ModelManager(models.Manager):
    """
    A custom manager class to support filtered and
    paginated query results.
    """
    def get_paginated(self, query, paginated_filter):
        items_per_page = paginated_filter.data['items_per_page']
        current_page = paginated_filter.data['current_page']
        order_by_column = paginated_filter.data['order_by_column']
        order_direction = paginated_filter.data['order_direction']
        limit = items_per_page * current_page
        offset = limit - items_per_page

        items = super(ModelManager, self).get_queryset().filter(query).order_by(
            f'{"" if order_direction else "-"}{order_by_column}'
        )[offset:limit]
        record_count = super(ModelManager, self).get_queryset().all().count()

        return PagedResult(items=items, record_count=record_count)
