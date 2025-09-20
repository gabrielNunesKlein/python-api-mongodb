from bson.objectid import ObjectId

class OrdersRepository:

    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data
    
    def select_one(self, doc_filter: dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find_one(doc_filter)
        return data
    
    def select_many_with_properties(self, doc_filter: dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)

        data = collection.find_one(
            doc_filter, # Tipo de Filtro
            { "_id": 0, "cupom": 0 } # Opções de retorno
        )
        
        return data
    
    def select_if_property_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find({ "address": { "$exists": True }})
        return response
    
    def selecte_by_object_id(self, object_id: str) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({ "_id": ObjectId(object_id) })
        return response
    
    def edit_registry(self, object_id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "_id": ObjectId(object_id)}, # Filtros
            { "$set": { "cupom": True } }  # Edição
        )

    def edit_many_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            { "itens.pizza": { "$exists": True } }, # Filtros
            { "$set": { "itens.pizza.quantidade": 30 } }  # Edição
        )

    def edit_registry_increment(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            { "itens.pizza": { "$exists": True } }, # Filtros
            { "$inc": { "itens.pizza.quantidade": 30 } }  # Edição
        )

    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one(
            { "_id": ObjectId("68ceaad7d9edce8da7d84210") }
        )

    def delete_many_registries(self) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many(
            { "itens.pizza": { "$exists": True } },
        )
