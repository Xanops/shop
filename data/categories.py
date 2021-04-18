import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Category(SqlAlchemyBase, SerializerMixin):
    serialize_only = ('id', 'title')
    __tablename__ = 'categories'
    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
