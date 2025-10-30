import os
from pymongo import MongoClient

class Load:
    def __init__(self):
        self.uri = os.getenv("MONGODB_URI")
        if not self.uri:
            raise ValueError("Variável MONGODB_URI não encontrada no .env")
        self.client = MongoClient(self.uri)

    def load_data_atlas(self, data: list[dict], db_name: str, collection_name: str):
        """
        Carrega os dados extraídos para o MongoDB Atlas.
        """
        db = self.client[db_name]
        collection = db[collection_name]
        if not data:
            print(f"Nenhum dado para inserir em {collection_name}")
            return

        # Aqui você pode decidir:
        # - apagar e reinserir
        # - ou inserir somente novos registros
        collection.delete_many({})  # limpa a coleção antes de inserir
        collection.insert_many(data)
        print(f"{len(data)} registros inseridos em {db_name}.{collection_name}")
