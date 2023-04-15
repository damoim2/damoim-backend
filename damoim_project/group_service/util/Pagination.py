from typing import Any
from django.db.models import QuerySet


class Pagination:
    total_count: int
    total_page: int
    paging_count: int
    request_page: int

    def __init__(self):
        self.total_page = 1
        self.paging_count = 10
        self.request_page = 1

    def get_data(self, object: Any, request_page: int, paging_count: int) -> dict:
        self.request_page = request_page
        if isinstance(object, QuerySet):
            self.total_count = object.count()
        else:
            self.total_count = len(object)
        self.paging_count = paging_count
        self.total_page = self.get_page_count()
        return self.get_sliced_data(object=object, page=request_page)

    def get_page_count(self) -> int:
        total_page = self.total_count / self.paging_count
        if total_page != 0:
            self.total_page += 1
        return total_page

    def get_sliced_data(self, object: list, page: int) -> dict:
        start_point = self.paging_count * (page - 1)
        end_point = (self.paging_count * page) - 1
        return {
            "paged_data": object[start_point:end_point],
            "total_count": self.total_count,
            "total_page": self.total_page,
            "current_page": self.request_page,
        }
