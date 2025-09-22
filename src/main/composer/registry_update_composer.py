from src.use_cases.registry_update import RegistryUpdate
from src.models.repository.orders_repository import OrdersRepository
from src.models.connection.connection_handler import db_connection_handler

def registry_update_composer():
    conn = db_connection_handler.get_db_connection()
    model = OrdersRepository(conn)
    use_case = RegistryUpdate(model)

    return use_case
