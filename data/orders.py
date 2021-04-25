import sqlalchemy
from sqlalchemy import orm
from .users import User
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin

orders_to_products = sqlalchemy.Table('orders_to_products', SqlAlchemyBase.metadata,
                                      sqlalchemy.Column('order', sqlalchemy.Integer,
                                                        sqlalchemy.ForeignKey('orders.id')),
                                      sqlalchemy.Column('product', sqlalchemy.Integer,
                                                        sqlalchemy.ForeignKey('products.id')))


class Order(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'orders'
    serialize_only = ('id', 'user', 'products')
    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('users.id'), nullable=False)
    products = orm.relationship('Product', secondary='orders_to_products')
    user = orm.relationship(User)
