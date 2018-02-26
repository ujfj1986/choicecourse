# /bin/bash python
# -*- coding: utf-8 -*-
# author: Jinjing Shan

from django.shortcuts import render
from django.views.generic import ListView

import logging

logger = logging.getLogger('course.view')

# Create your views here.
class Element:
    elem_url = ""
    elem_str = ""

    def __init__(self):
        self.elem_url = ""
        self.elem_str = ""

    def clear(self):
        self.elem_url = ""
        self.elem_str = ""

    def __str__(self):
        return self.elem_str

class Row:
    row_url = ""
    pk = ""
    row_num = 1
    elems = []

    def __init__(self):
        self.row_url = ""
        self.pk = ""
        self.elems = []
        self.row_num = 1


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'context'
    paginate_by = 10
    new_url = ''
    cols = []

    def _get_rows(self):
        raise NotImplementedError

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')

        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        context['new_url'] = self.new_url
        context['cols'] = self.cols
        context['rows'] = self._get_rows()

        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}

        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number == 1:
            right = page_range[page_number: page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0: page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0: page_number - 1]
            right = page_range[page_number: page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            
        data = {
            'left': left,
            'right': right,
            'right_has_more': right_has_more,
            'left_has_more': left_has_more,
            'first': first,
            'last': last,
        }
        return data
