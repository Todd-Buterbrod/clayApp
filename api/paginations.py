from rest_framework.pagination import CursorPagination


class PaginationByCreateTime(CursorPagination):
    page_size = 3  # default size
    # max_page_size = 1000
    ordering = '-created'

class PaginationById(CursorPagination):
    page_size = 20  # default size
    # max_page_size = 1000
    ordering = '-id'

# class PageNumberAsLimitOffset(PageNumberPagination):
#     page_query_param = "offset"   # this is the "page"
#     page_size_query_param="limit" # this is the "page_size"
#     page_size = 5
#     max_page_size = 100