from main import app
from database import register_business_db, register_business_category_db, get_business_categories_db,\
    get_exact_business_db, delete_business_db, pay_for_service_db, delete_business_category_db


@app.post('/register-business-category')
async def register_business_category_api(name: str):
    result = register_business_category_db(name)

    return {'status': 1, 'message': result}


@app.post('/register-business')
async def register_business_api(category_id: int, name: str, card_number: int):
    result = register_business_db(category_id, name, card_number)

    return {'status': 1, 'message': result}


@app.get('/get-all-categories')
async def get_business_category_api(exact_category_id: int = 0):
    result = get_business_categories_db(exact_category_id)

    return {'status': 1, 'message': result}


@app.get('/get_business')
async def get_exact_business_api(business_id: int, category_id: int):
    result = get_exact_business_db(business_id, category_id)

    return {'status': 1, 'message': result}


@app.post('/pay-service')
async def pay_for_service(business_id: int, from_card: int, amount: float):
    result = pay_for_service_db(business_id, from_card, amount)

    return {'status': 1, 'message': result}


@app.delete('/delete-business')
async def delete_business_api(business_id: int):
    result = delete_business_db(business_id)

    return {'status': 1, 'message': result}


@app.delete('/delete-business-category')
async def delete_business_category_api(category_id: int):
    result = delete_business_category_db(category_id)

    return {'status': 1, 'message': result}
