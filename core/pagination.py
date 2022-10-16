from rest_framework.utils.urls import replace_query_param
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response
from rest_framework.settings import api_settings

from collections import OrderedDict


class PageNumberPaginationExt(PageNumberPagination):
    """
    Adds extra attributes to response, useful for building
    pagination widgets with range.
    """
    max_page_size = getattr(api_settings, 'MAX_PAGE_SIZE', 100)
    page_size_query_param = 'page_size'

    def get_first_link(self):
        if not self.page.has_previous():
            return None

        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, '1')

    def get_last_link(self):
        if not self.page.has_next():
            return None

        url = self.request.build_absolute_uri()
        return replace_query_param(url, self.page_query_param, 'last')

    def current_page(self):
        return self.request.query_params.get(self.page_query_param, 1)

    def next_page_number(self):
        return self.page.next_page_number() \
            if self.page.has_next() else None

    def prev_page_number(self):
        return self.page.previous_page_number() \
            if self.page.has_previous() else None

    def display_results_from(self):
        if(self.current_page() == 1):
            return 1
        return ((int(self.current_page()) - 1) * self.page_size) + 1

    def display_results_to(self):
        if((int(self.current_page()) == 1 and (self.page.paginator.count < self.page_size))
           or int(self.current_page()) == self.page.paginator.num_pages):
            return self.page.paginator.count
        return (int(self.current_page()) * self.page_size)

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('num_pages', self.page.paginator.num_pages),
            ('count', self.page.paginator.count),
            ('begin', self.display_results_from()),
            ('end', self.display_results_to()),
            ('previous', self.prev_page_number()),
            ('has_prev', self.page.has_previous()),
            ('next', self.next_page_number()),
            ('has_next', self.page.has_next()),
            ('results', data),
            ('last', 'last'),
            ('first', 1),
            ('page_number', self.current_page())
        ]))
