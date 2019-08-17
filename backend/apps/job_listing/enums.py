from enumchoicefield import ChoiceEnum


class JobListingStatus(ChoiceEnum):
    DRAFT = 'Draft'
    PUBLISHED = 'Published'
    EXPIRED = 'Expired'
    CLOSED = 'Closed'


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
