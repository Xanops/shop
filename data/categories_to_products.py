import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Categories_to_products(SqlAlchemyBase, SerializerMixin):
    serialize_only = ('product', 'category')
    __tablename__ = 'categories'
    __table_args__ = {'extend_existing': True}
    product = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    category = sqlalchemy.Column(sqlalchemy.Integer)

    def __repr__(self):
        return self.title
