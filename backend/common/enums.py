from enum import Enum


class LocationState(Enum):
    NT = 'NT',
    WA = 'WA',
    QLD = 'QLD',
    SA = 'SA',
    NSW = 'NSW',
    VIC = 'VIC',
    TAS = 'TAS'


class LocationCountry(Enum):
    AU = 'AU'