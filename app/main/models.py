from datetime import datetime

from app.database import Column, PkModel, db, reference_col, relationship


class Record(PkModel):
    """Password record that contains:
    - name;
    - login;
    - password;
    - comment.
    """

    __tablename__ = "records"
    name = Column(db.String(100), nullable=False)
    login = Column(db.String(100), nullable=False)
    password = Column(db.String(128), nullable=False)
    comment = Column(db.String(200), nullable=True)
    saved_at = Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = reference_col("users", nullable=False)
    user = relationship("User", backref="records")

    def __repr__(self):
        """Represent instance as a unique string."""
        return f"<Record(id='{self.id}' name='{self.name}' login='{self.login}')>"

    def __str__(self):
        return self.name
