from enumfields import EnumIntegerField
from enumchoicefield import ChoiceEnum


class JobListingState(EnumIntegerField):
    DRAFT = 1
    PREPUBLISH = 2
    PUBLISHED = 3
    EXPIRED = 4
    CLOSED = 5
    ARCHIVED = 6

    class Labels:
        DRAFT = 'Draft'
        PREPUBLISH = 'Queued for publish'
        PUBLISHED = 'Published'
        EXPIRED = 'Expired'
        CLOSED = 'Closed'
        ARCHIVED = 'Archived'


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
