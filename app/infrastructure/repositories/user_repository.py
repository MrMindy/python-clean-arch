from app.infrastructure.config import DBConnectionHandler
from app.infrastructure.models import User


class UserRepository:
    """Class to manager User Repository"""

    @classmethod
    def insert(cls):
        """
        Insert data into user entity
        :params - name: person name
                - password: user password
        :return
        """

        with DBConnectionHandler() as connection:
            try:
                user = User("teste", "teste")
                connection.session.add(user)
                connection.session.commit()
            except:
                connection.session.rollback()
                raise
            finally:
                connection.session.close()
