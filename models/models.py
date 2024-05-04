from sqlalchemy.sql import func
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Enum, Float, Boolean, ARRAY, PrimaryKeyConstraint, BigInteger

from utils import Model

# BASE = declarative_base(cls=Model)
#
# DQ_SCHEMA = 'data_quality'


# class DataQualityInput(BASE):
    # __tablename__ = 'data_quality_inputs'
    #
    # owner = Column(String, nullable=True, )
    # schema = Column(String, nullable=False, default='feeds')
    # feed = Column(String, nullable=False)  # the only required field
    # type = Column(Enum(FeedType), default=FeedType.DUMP, nullable=False)
    # engine = Column(Enum(Engine), default=Engine.KAMANJA, nullable=False)
    # # best_run_time = Column(Enum(FeedType), default=FeedType.DUMP, nullable=False)
    #
    # threshold = Column(Float, default=0.1, nullable=False)
    # window = Column(Integer, default=7, nullable=False)
    # retries = Column(Integer, default=1, nullable=False)  # TODO; just in failures [conditional]
    # partitioned_by = Column(String, default='tbl_dt', nullable=False)
    # regex = Column(String, default='([0-9]{8}).*$', )
    # ignore_files_with_regex = Column(String, default='%.tar.gz$', )
    # seasonality = Column(Enum(Frequency), default=Frequency.WEEKLY, nullable=False)
    #
    # last_available_stats_day = Column(Integer, nullable=True)
    # frequency = Column(Enum(Frequency), default=Frequency.DAILY, nullable=False)
    # msck = Column(Boolean, default=True, nullable=False)
    # dedup = Column(Boolean, default=True, nullable=False)
    # pcf = Column(Boolean, default=True, nullable=False)
    # trend = Column(Boolean, default=True, nullable=False)
    # match = Column(Boolean, default=True, nullable=False)
    #
    # # TODO: the below is to specify which feed to include in the rerun
    # # rerun = Column(Boolean, default=True, nullable=False)
    #
    # # TODO: add in the validator if possible
    # #  1- best time to run -- when it was ingested from the filestats -- note give out-buffer of 15 min
    #
    # # Feed outputs
    #
    # # if true meaning it was not found in file stats but still registered in the system
    # decommissioned = Column(Boolean, default=False, nullable=False)
    # decommission_after_days = Column(Integer, default=92, nullable=False)
    # created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    # updated_at = Column(DateTime, default=datetime.utcnow, onupdate=func.now(), nullable=False)
    # removed_at = Column(DateTime, default=None, nullable=True)
    #
    # __table_args__ = (
    #     PrimaryKeyConstraint('schema', 'feed'),
    #     {'extend_existing': True, 'schema': DQ_SCHEMA, },
    #
    # )
    # pass
