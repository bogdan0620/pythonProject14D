import datetime
from database.models import Card, Transaction
from database import get_db


# сделать перевод с карты на карту
def transfer_money_db(card_from, card_to, date, amount):
    db = next(get_db())
    card_from_checker = get_exact_card_balance_db(card_from)
    card_to_checker = get_exact_card_balance_db(card_to)

    if (card_from_checker and card_to_checker) and (card_from_checker.balance >= amount):
        transaction = Transaction(card_to=card_to, card_id=card_from_checker.card_id, transaction_date=datetime.datetime.now(), amount=amount)
        card_from_checker.balance -= amount
        card_to_checker.balance += amount

        db.add(transaction)
        db.commit()

        return 'Перевод успешно произведен'

    elif not card_to_checker or not card_from_checker:
        return 'Ошибка в данных'

    else:
        return 'Недостаточно средств'


def pay_for_service_db(business_id: int, from_card: int, amount: float):
    db = next(get_db())
    checker = get_exact_card_balance_db(from_card)

    if checker and checker.balance >= amount:
        transaction = Transaction(card_to=business_id, card_id=checker.card_id, amount=amount)
        checker.balance -= amount

        db.add(transaction)
        db.commit()
        return 'Услуга успешно оплачена'

    elif not checker:
        return 'Ошибка в данных'

    else:
        return 'Недостаточно средств'


def get_exact_card_balance_db(card_number):
    db = next(get_db())
    exact_card = db.query(Card).filter_by(card_number=card_number).first()

    return exact_card
