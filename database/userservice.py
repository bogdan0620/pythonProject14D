from database.models import User, Password
from database import get_db
import datetime


def register_user_db(phone_number, name, password, pincode, reg_date):
    db = next(get_db())
    # phone_number = kwargs.get('phone_number')

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return 'Пользователь с таким номером уже существует'

    new_user = User(phone_number=phone_number, name=name, reg_date=datetime.datetime.now())
    db.add(new_user)
    db.commit()

    new_user_password = Password(user_id=new_user.user_id, password=password, pincode=pincode)
    db.add(new_user_password)
    db.commit()

    return 'Пользователь успешно зарегистрирован'


def check_password_db(phone_number, password):
    db = next(get_db())
    checker = db.query(Password).filter(User.phone_number == phone_number).first()

    if checker and checker.password == password:
        return checker.user_id

    elif not checker:
        return 'Номер не зарегистрирован'

    elif checker.password != password:
        return 'Пароль не правильный'


def get_user_cabinet_db(user_id):
    db = next(get_db())

    checker = db.query(User).filter_by(user_id=user_id).first()

    if checker:
        return checker

    return 'Пользователь не существует'
