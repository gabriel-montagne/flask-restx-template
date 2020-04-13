from .. import db


class UserRole(db.Model):
    """ User Roles model """
    __tablename__ = 'user_role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(250))
    authorization = db.Column(db.JSON)
