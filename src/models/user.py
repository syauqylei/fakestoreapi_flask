import datetime
from . import db, bcrypt


class User(db.Model):
    """
    User Model
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, data):
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = self.__generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password = self.__generate_hash(data.get('password'))
            setattr(self, key, item)

        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_user():
        return User.query.all()

    @staticmethod
    def get_one_user(id):
        return User.query.get(id)

    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password,
                                             rounds=10).decode('utf-8')

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __repr(self):
        return '<id {}>'.format(self.id)
