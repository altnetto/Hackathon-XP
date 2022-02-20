from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(256), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)

    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = generate_password_hash(email)
        self.password = generate_password_hash(password)

    def __str__(self):
        return self.email

    def compare_value(self, **kwargs):
        all_fields = all(
            [
                check_password_hash(getattr(self, k), v)
            ] for k, v in kwargs.items()
        )
        return all_fields
