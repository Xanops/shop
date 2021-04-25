import sqlalchemy
from .db_session import SqlAlchemyBase
from .categories import Category
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

categories_to_products = sqlalchemy.Table('categories_to_products', SqlAlchemyBase.metadata,
                                          sqlalchemy.Column('product', sqlalchemy.Integer,
                                                            sqlalchemy.ForeignKey('products.id')),
                                          sqlalchemy.Column('category', sqlalchemy.Integer,
                                                            sqlalchemy.ForeignKey('categories.id')))


class Product(SqlAlchemyBase, SerializerMixin):
    serialize_only = ('id', 'title', 'description', 'price', 'categories')
    __tablename__ = 'products'
    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    categories = orm.relationship(Category, secondary='categories_to_products', backref='categories')
