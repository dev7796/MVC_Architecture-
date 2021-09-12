from base import db


class CategoryVO(db.Model):
    __tablename__ = 'categorymaster'
    category_id = db.Column('categoryId', db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column('categoryName', db.String(100))
    category_description = db.Column('categoryDescription', db.String(100))

    def as_dict(self):
        return {
            'categoryId': self.category_id,
            'categoryName': self.category_name,
            'categoryDescription': self.category_description
        }


db.create_all()
