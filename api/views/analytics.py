from api.mixin import HospitalGenericViewSet
from api.service import get_upcoming_visits_count, get_past_visits_count, get_department_names, get_avg_rating, get_income_sum_finance, get_expense_sum_finance, get_tax_sum_finance, get_profit_finance
from api.models import Patient, Doctor, Visit, Department
from rest_framework import status
from rest_framework.response import Response


class CommonAnalyticsView(
    HospitalGenericViewSet,

):
    def get_action_permissions(self):
        if self.action == 'get_common_analytics':
            self.action_permissions = []

    def get_common_analytics(self, request):
        response = {
            'departments': get_department_names(),
            'doctors_count': Doctor.objects.all().count(),
            'patients_count': Patient.objects.all().count()
        }
        return Response(status=status.HTTP_200_OK, data=response)


class VisitAnalyticsView(
    HospitalGenericViewSet,

):
    def get_action_permissions(self):
        if self.action == 'get_visit_analytics':
            self.action_permissions = []

    def get_visit_analytics(self, request):
        response = {
            'all_visits_count': Visit.objects.all().count(),
            'past_visits_count': get_past_visits_count(),
            'upcoming_visits_count': get_upcoming_visits_count(),
        }
        return Response(status=status.HTTP_200_OK, data=response)


class RatingAnalyticsView(
    HospitalGenericViewSet,

):
    def get_action_permissions(self):
        if self.action == 'get_rating_analytics':
            self.action_permissions = []

    def get_rating_analytics(self, request):
        response = {
            'patient_satisfaction_level': get_avg_rating()
        }
        return Response(status=status.HTTP_200_OK, data=response)


class FinanceAnalyticsView(
    HospitalGenericViewSet,

):
    def get_action_permissions(self):
        if self.action == 'get_finance_analytics':
            self.action_permissions = []

    def get_finance_analytics(self, request):
        response = {
            'income_sum': get_income_sum_finance(),
            'expense_sum': get_expense_sum_finance(),
            'tax_sum_from_expense': get_tax_sum_finance(),
            'profit_sum': get_profit_finance()
        }
        return Response(status=status.HTTP_200_OK, data=response)