from db.database import ENGINE, Base
from db.models import User, Category, Product, Order

Base.metadata.create_all(bind=ENGINE)