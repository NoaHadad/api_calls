from django.urls import path
from . import views

urlpatterns=[
    path('',views.apiOverview,name="api-overview"),
    path('quote-list',views.quotesList,name="quotes-list"),
    path('quote-create',views.quoteCreate,name="quote-create"),
    path('quote-delete/<str:pk>',views.quoteDelete,name="quote-delete"),
    path('quote-update',views.quoteUpdate,name="quote-update"),
    path('quote-detail/<str:pk>',views.quoteDetail,name="quote-detail"),
]

