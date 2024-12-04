from models.farms import Farm
from dto.farm_dto import FarmDTO

class FarmMapper:
    @staticmethod
    def to_dto(farm: Farm) -> FarmDTO:
        return FarmDTO(
            id=farm.id,
            area=farm.area,
            village=farm.village,
            crop_grown=farm.crop_grown,
            sowing_date=farm.sowing_date,
            farmer_id=farm.farmer_id,
            country_id=farm.country_id
        )

    @staticmethod
    def to_model(farm_dto: FarmDTO) -> Farm:
        return Farm(
            id=farm_dto.id,
            area=farm_dto.area,
            village=farm_dto.village,
            crop_grown=farm_dto.crop_grown,
            sowing_date=farm_dto.sowing_date,
            farmer_id=farm_dto.farmer_id,
            country_id=farm_dto.country_id
        )
