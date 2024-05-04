from enum import Enum

ALL = "all"


class Engine(Enum):
    FDI = "fdi"
    KAMANJA = "kamanja"
    DIRECT = "direct"
    UNKNOWN = -1


class FeedType(Enum):
    LIVE = "live"
    DUMP = "daily"
    EXTRACTION = "extraction"
    UNKNOWN = "unknown"


class DBLayer(Enum):
    REJECTION = "fsys_filename"
    HIVE = "file_name"
    OPS = "name"
    # STATS = "fsys_msgtype"


class RangeCenter(Enum):
    END = -1
    START = 0
    CENTER = 1


class Status(Enum):
    SUCCESS = 1
    RUNNING = 0
    FAIL = -1
    PASSED = -100


class DQComparisonStatus(Enum):
    MATCH = 0
    BELOW = -1
    ABOVE = 1
    SKIPPED = -100


class Aggregations(Enum):
    SUM = "sum"
    AVG = "avg"
    MEAN = "mean"
    MODE = "mode"
    COUNT = "count"
    MAX = "max"
    MIN = "min"
    MEDIAN = "median"
    STD = "std"
    VARIANCE = "var"
    FIRST = "first"
    LAST = "last"
    UNIQUE_COUNT = "unique_count"
    DISTINCT_COUNT = "distinct_count"
    COMPLEX = "C"  # HAS SPECIAL REQUIREMENTS


class Frequency(Enum):
    # SECONDS = "S"
    # MINUTES = "T"
    # HOURLY = "H"
    DAILY = "D"
    WEEKLY = "W"
    BIMONTHLY = "2W"
    MONTHLY = "M"
    QUARTERLY = "3M"
    BIANNUAL = "6M"
    ANNUAL = "Y"


class Directions(Enum):
    LEFT = -1
    RIGHT = 1
    MID = 0
    BOTH = 2


if __name__ == "__main__":
    # print([level.name for level in DictLookupLevel])
    pass
