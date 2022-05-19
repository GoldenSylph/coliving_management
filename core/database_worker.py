from typing import Protocol
import pymongo


class DatabaseWorker(Protocol):
    def create_db(self) -> None:
        ...

    def save_to_db(self, object) -> None:
        ...

    def load_from_db(self, object_id) -> None:
        ...

    def update_doc(self, object_id, fields) -> None:
        ...

    def delete(self, object_id) -> None:
        ...


class SqliteWorker:
    def create_db(self) -> None:
        raise NotImplementedError

    def save_to_db(self, object) -> None:
        raise NotImplementedError

    def load_from_db(self, object_id) -> None:
        raise NotImplementedError

    def update_doc(self, object_id, fields) -> None:
        raise NotImplementedError

    def delete(self, object_id) -> None:
        raise NotImplementedError


class MongoWorker:

    def create_db(self) -> None:
        raise NotImplementedError

    def save_to_db(self, object) -> None:
        raise NotImplementedError

    def load_from_db(self, object_id) -> None:
        raise NotImplementedError

    def update_doc(self, object_id, fields) -> None:
        raise NotImplementedError

    def delete(self, object_id) -> None:
        raise NotImplementedError
