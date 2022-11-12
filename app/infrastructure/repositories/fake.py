from app.infrastructure.config import DBConnectionHandler
from app.infrastructure.models import User


class FakerRepo:
    """A simple Repository"""

    @classmethod
    def insert(cls):
        """A simple insert method"""

        with DBConnectionHandler() as connection:
            try:
                user = User(name="gnunes1530", password="j1k2l3153")
                connection.session.add(user)
                connection.session.commit()
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()
