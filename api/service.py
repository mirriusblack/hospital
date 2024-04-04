import datetime

from api.models import Visit, Department, Finance
from django.db.models import Avg, Sum


def get_past_visits_count():
    return Visit.objects.filter(
        schedule__timestamp_end__lte=datetime.datetime.now()
    ).count()


def get_upcoming_visits_count():
    return Visit.objects.filter(
        schedule__timestamp_start__gte=datetime.datetime.now()
    ).count()


def get_department_names():
    return list(set(Department.objects.all().values_list('name', flat=True)))


def get_avg_rating():
    visits = Visit.objects.all()
    return visits.values('rating').aggregate(Avg('rating'))


def get_income_sum_finance():
    income_sum = Finance.objects.aggregate(total=Sum('cost'))
    return income_sum.get('total')


def get_expense_sum_finance():
    expense_sum = Finance.objects.aggregate(total=Sum('expense'))
    return expense_sum.get('total')


def get_tax_sum_finance():
    tax_sum = Finance.objects.aggregate(total=Sum('tax'))
    return tax_sum.get('total')


def get_profit_finance():
    cost_sum = Finance.objects.aggregate(total=Sum('cost'))
    expense_sum = Finance.objects.aggregate(total=Sum('expense'))
    return cost_sum.get('total') - expense_sum.get('total')


def get_net_profit_finance():
    cost_sum = Finance.objects.aggregate(total=Sum('cost'))
    expense_sum = Finance.objects.aggregate(total=Sum('expense'))
    tax_sum = Finance.objects.aggregate(total=Sum('tax'))
    return cost_sum.get('total') - expense_sum.get('total') - tax_sum.get('total')