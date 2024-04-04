from django.urls import path
from .views import DoctorView, PatientView, ProcedureView, SpecializationView, VisitView, ScheduleView, CommonAnalyticsView, VisitAnalyticsView, RatingAnalyticsView, DepartmentView, FinanceView, FinanceAnalyticsView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path(
        'doctor/',
        DoctorView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),

    path(
        'doctor/<int:id>/',
        DoctorView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'doctor/<int:id>/patient/',
        DoctorView.as_view({
            'get': 'list_patient'
        })
    ),
    path(
        'patient/',
        PatientView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'patient/<int:id>/',
        PatientView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'procedure/',
        ProcedureView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'procedure/<int:id>/',
        ProcedureView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'visit/',
        VisitView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'visit/<int:id>/',
        VisitView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'visit/<int:id>/rating',
        VisitView.as_view({
            'put': 'set_rating'
        })
    ),
    path(
        'department/',
        DepartmentView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'department/<int:id>/',
        DepartmentView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'specialization/',
        SpecializationView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'specialization/<int:id>/',
        SpecializationView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'schedule/',
        ScheduleView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'schedule/<int:id>/',
        ScheduleView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'finance/',
        FinanceView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'finance/<int:id>/',
        FinanceView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'analytics/common/',
        CommonAnalyticsView.as_view({
             'get': 'get_common_analytics'
         })
    ),
    path(
        'analytics/visit/',
        VisitAnalyticsView.as_view({
             'get': 'get_visit_analytics'
         })
    ),
    path(
        'analytics/rating/',
        RatingAnalyticsView.as_view({
             'get': 'get_rating_analytics'
         })
    ),
    path(
        'analytics/finance/',
        FinanceAnalyticsView.as_view({
             'get': 'get_finance_analytics'
         })
    ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
