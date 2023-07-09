from database.models import Card, User, Transaction
from database import get_db


def add_user_card_db(**kwargs):
    db = next(get_db())
    card_number = kwargs.get('card_number')

    checker = db.query(Card).filter_by(card_number=card_number).first()

    if checker:
        return 'Карта уже добавлена'

    new_card = Card(**kwargs)
    db.add(new_card)
    db.commit()

    return 'Карта успешно добавлена'


# удалить карту
def delete_user_card_db(card_id, user_id):
    db = next(get_db())
    checker = db.query(Card).filter_by(user_id=user_id, card_id=card_id).first()

    if checker:
        db.delete(checker)
        db.commit()
        return 'Карта удалена'

    return 'Вы еще не добавили эту карту'


# получить все карты по номеру телефона
def get_user_cards_by_phone_number_db(phone_number):
    db = next(get_db())
    checker = db.query(Card).filter(User.phone_number == phone_number).all()

    if checker:
        return checker
    return 'Карты отсутствуют'


# получить информацию о карте
def get_exact_user_card_db(user_id, card_id):
    db = next(get_db())
    if card_id == 0:
        card_data = db.query(Card).filter_by(user_id=user_id).all()

    else:
        card_data = db.query(Card).filter_by(user_id=user_id, card_id=card_id).first()

    return card_data


# получить все транзакции по карте или картам
def get_all_cards_or_exact_transactions_db(user_id, card_id):
    db = next(get_db())

    if card_id == 0:
        card_monitor = db.query(Transaction).filter_by(user_id=user_id).all()

    else:
        card_monitor = db.query(Transaction).filter_by(user_id=user_id, card_id=card_id).all()

    return card_monitor
