from sqlalchemy import Column, String, Integer, ARRAY
from extensions import db
import bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    roles = Column(ARRAY(String), nullable=False, default=["viewer"])  # Roles: "superuser", "admin", "viewer"

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))

    def has_role(self, role):
        return role in self.roles

    def add_role(self, role):
        print(f"Got call here with {role}", flush=True)
        if role not in self.roles:
            roles = self.roles
            roles.append(role)
            self.roles =roles
        print("Roles of user after updating are", self.roles, flush=True)

    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)
