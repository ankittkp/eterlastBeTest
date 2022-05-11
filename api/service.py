from api.models import NFT, Collection
from users.models import User


class NFTService:
    @staticmethod
    def mint(data: dict):
        data["collection"] = Collection.objects.get(id=data["collection"])
        NFT.objects.create(**data)


class CollectionService:
    @staticmethod
    def create(data: dict):
        data["creator"] = User.objects.get(user=data["creator"])
        Collection.objects.create(**data)