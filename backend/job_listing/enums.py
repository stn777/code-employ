from enum import Enum


class JobPositionType(Enum):
    CASUAL = 'Casual'
    CONTRACT = 'Contract'
    PARTTIME = 'Part-time'
    FULLTIME = 'Full-time'


class SalaryFrequency(Enum):
    PERHOUR = 'Per-hour'
    PERDAY = 'Per-day'
    PERWEEK = 'Per-week'
    PERFORTNIGHT = 'Per-fortnight'
    PERMONTH = 'Per-month'
    PERYEAR = 'Per-year'
