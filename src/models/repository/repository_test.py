import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connection_to_db()
conn = db_connection_handler.get_db_connection()

@pytest.mark.skip(reason="interacao com o banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = { "alguma": "coisa", "valor": 5 }
    orders_repository.insert_document(my_doc)

@pytest.mark.skip(reason="interacao com o banco")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_doc = [{ "elem1": "aqui1"}, {"elem2": "aqui2" }, {"elem3": "aqui3"}]
    orders_repository.insert_list_of_documents(my_doc)

@pytest.mark.skip(reason="interacao com o banco")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "valor": 5
    }
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)

    for doc in response:
        print(doc)

@pytest.mark.skip(reason="interacao com o banco")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "valor": 5
    }
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)

    for doc in response:
        print(doc)

@pytest.mark.skip(reason="interacao com o banco")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "valor": 5
    }
    response = orders_repository.select_many_with_properties(doc_filter)
    print()

    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interacao com o banco")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()
    print()

    for doc in response:
        print(doc)
        print()

@pytest.mark.skip(reason="interacao com o banco")
def test_select_many_with_multiple_select():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True,
        "itens.doce": { "$exists": True }
    }

    response = orders_repository.select_many(doc_filter)
    print()
    print(response)

    for doc in response:
        print(doc)

@pytest.mark.skip(reason="interacao com o banco")
def test_select_many_with_or_select():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [
                { "address": { "exists": False } },
                { "itens.doce.tipo": "Chocolate" }
            ]
    }

    response = orders_repository.select_many(doc_filter)
    print()
    print(response)

    for doc in response:
        print(doc)

@pytest.mark.skip(reason="interacao com o banco")
def test_selecte_by_object_id():
    orders_repository = OrdersRepository(conn)

    response = orders_repository.selecte_by_object_id("68ceaad7d9edce8da7d84210")
    print()
    print(response)

@pytest.mark.skip(reason="interacao com o banco")
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_registry("68ceaad7d9edce8da7d84210")

@pytest.mark.skip(reason="interacao com o banco")
def test_edit_many_registry():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_many_registry()

@pytest.mark.skip(reason="interacao com o banco")
def test_edit_registry_increment():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_registry_increment()