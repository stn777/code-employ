from enumchoicefield import ChoiceEnum


class JobPositionType(ChoiceEnum):
    CASUAL = 'Casual'
    CONTRACT = 'Contract'
    PARTTIME = 'Part-time'
    FULLTIME = 'Full-time'


class SalaryFrequency(ChoiceEnum):
    PERHOUR = 'Per-hour'
    PERDAY = 'Per-day'
    PERWEEK = 'Per-week'
    PERFORTNIGHT = 'Per-fortnight'
    PERMONTH = 'Per-month'
    PERYEAR = 'Per-year'
