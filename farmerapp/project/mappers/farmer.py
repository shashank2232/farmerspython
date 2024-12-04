from models.farmer import Farmer
from dto.farmer_dto import FarmerDTO

class FarmerMapper:
    @staticmethod
    def to_dto(farmer: Farmer) -> FarmerDTO:
        return FarmerDTO(
            id=farmer.id,
            phone_number=farmer.phone_number,
            name=farmer.name,
            language=farmer.language,
            country_id=farmer.country_id
        )

    @staticmethod
    def to_model(farmer_dto: FarmerDTO) -> Farmer:
        return Farmer(
            id=farmer_dto.id,
            phone_number=farmer_dto.phone_number,
            name=farmer_dto.name,
            language=farmer_dto.language,
            country_id=farmer_dto.country_id
        )
