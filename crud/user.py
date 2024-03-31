from sqlalchemy.orm import Session
import models

def get_user_by_uid(db: Session, user_id: str):
    return db.query(models.User).filter(models.User.id == user_id).first()
