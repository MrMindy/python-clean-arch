from faker import Faker
from app.infrastructure.repositories import FakerRepo

faker = Faker()


def test_insert():
    """Must insert a new User"""

    # name = faker.name()
    #  password = faker.word()

    repo = FakerRepo()
    repo.insert()
