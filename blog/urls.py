#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: liangliangyy
@license: MIT Licence
@contact: liangliangyy@gmail.com
@site: https://www.lylinux.net/
@software: PyCharm
@file: urls.py
@time: 2016/11/2 下午7:15
"""

from django.urls import path
from django.views.decorators.cache import cache_page
# 视图
from . import views
from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView

# blog app 的 urls
# name定义在 apps.py
app_name = "blog"


urlpatterns = [
    # 默认路径
    # 返回视图
    path(
        r'',
        views.IndexView.as_view(),
        name='index'),

    # eg. /page/2/
    # 但是1页在右边 2页在左边 不是很舒服
    # 2021年1月4日09:53:09
    path(
        r'page/<int:page>/',
        views.IndexView.as_view(),
        name='index_page'),

    # 按照时间阅读文章
    path(
        r'article/<int:year>/<int:month>/<int:day>/<int:article_id>.html',
        views.ArticleDetailView.as_view(),
        name='detailbyid'),

    # 分类名查找
    path(
        r'category/<slug:category_name>.html',
        views.CategoryDetailView.as_view(),
        name='category_detail'),

    # 分类名 + 页数
    path(
        r'category/<slug:category_name>/<int:page>.html',
        views.CategoryDetailView.as_view(),
        name='category_detail_page'),

    # 作者名
    path(
        r'author/<author_name>.html',
        views.AuthorDetailView.as_view(),
        name='author_detail'),

    # 作者名 + 页数
    path(
        r'author/<author_name>/<int:page>.html',
        views.AuthorDetailView.as_view(),
        name='author_detail_page'),

    # 标签名
    path(
        r'tag/<slug:tag_name>.html',
        views.TagDetailView.as_view(),
        name='tag_detail'),

    # 标签名 + 页数
    path(
        r'tag/<slug:tag_name>/<int:page>.html',
        views.TagDetailView.as_view(),
        name='tag_detail_page'),


    path(
        'archives.html',
        cache_page(
            60 * 60)(
            views.ArchivesView.as_view()),
        name='archives'),

    # 友情链接
    path(
        'links.html',
        views.LinkListView.as_view(),
        name='links'),

    # only for post
    path(
        r'upload',
        views.fileupload,
        name='upload'),

    # 刷新缓存
    path(
        r'refresh',
        views.refresh_memcache,
        name='refresh')]
