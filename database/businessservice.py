import datetime
from database.models import Service, ServiceCategory
from database import get_db


def register_business_category_db(name: str):
    db = next(get_db())
    new_category = ServiceCategory(category_name=name)

    db.add(new_category)
    db.commit()
    return 'Категория бизнеса успeшно зарегистрирована'


def register_business_db(category_id: int, name: str, card_number: int):
    db = next(get_db())
    new_business = Service(service_category=category_id, service_name=name, service_check=card_number, reg_date=datetime.datetime.now())

    db.add(new_business)
    db.commit()
    return 'Бизнес успeшно зарегистрирован'


def get_business_categories_db(exact_category_id: int = 0):
    db = next(get_db())
    if exact_category_id == 0:
        categories = db.query(ServiceCategory).all()

    else:
        categories = db.query(ServiceCategory).filter_by(category_id=exact_category_id).all()

    return categories


def get_exact_business_db(business_id: int, category_id: int):
    db = next(get_db())
    business = db.query(Service).filter_by(service_id=business_id, service_category=category_id).first()

    if business:
        return business

    else:
        return 'Бизнес не найден'


def delete_business_db(business_id: int):
    db = next(get_db())
    business = db.query(Service).filter_by(service_id=business_id).first()

    if business:
        db.delete(business)
        db.commit()
        return 'Бизнес удален'

    else:
        return 'Бизнес не найден'


def delete_business_category_db(category_id: int):
    db = next(get_db())
    category = db.query(ServiceCategory).filter_by(category_id=category_id).first()

    if category:
        db.delete(category)
        db.commit()
        return 'Категория успешно удалена'

    else:
        return 'Категория не найдена'
