from sqlalchemy import Column, DateTime, String, Integer, Boolean, ForeignKey, func, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
#metaData = MetaData()

Base = declarative_base()

class Visiter(Base):
    __tablename__ = 'trackself_visiter'
    id = Column(Integer, primary_key=True)
    #pageview = relationship("Pageview",backref="Visiter")
    first_time_visit = Column(DateTime)
    last_time_visit = Column(DateTime,default=func.now())
    friend_status = Column(String(1),default='0')
    visit_times = Column(Integer,default=1)
    tokens = Column(String(256),default="---**---")
    location = Column(String(128))
    device = Column(String(64))
    os = Column(String(64))
    browser = Column(String(64))
    casual_user = Column(Boolean,default=True)
    ip = Column(String,default="0x00")
    isp = Column(String(128))
    uuid = Column(String(64))


class Pageview(Base):
    __tablename__ = "trackself_pageview"
    id = Column(Integer,primary_key=True)
    random = Column(String(64),default='0')
    #visiter_id = Column(Integer,ForeignKey("visiter.id",ondelete="CASCADE"))
    brow_page = Column(String(64),default="-")
    referer = Column(String(256),default="-")
    language = Column(String(64),default="-")
    residencetime = Column(String(32),default="0")
    platform = Column(String(64),default="-")
    screen = Column(String(16),default="-") 

