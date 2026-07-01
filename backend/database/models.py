from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text
from datetime import datetime
from backend.database.db import Base


class Draft(Base):
    __tablename__ = "drafts"

    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(String, unique=True, index=True)
    topic = Column(String)
    genre = Column(String)
    platform = Column(String)
    draft = Column(Text)
    status = Column(String)
    approval_required = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(String, index=True)
    action = Column(String)
    status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Metric(Base):
    __tablename__ = "metrics"

    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String)
    metric_name = Column(String)
    metric_value = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)