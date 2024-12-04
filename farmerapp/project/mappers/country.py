from models.countries import Country
from dto.country_dto import CountryDTO

class CountryMapper:
    @staticmethod
    def to_dto(country: Country) -> CountryDTO:
        return CountryDTO(
            id=country.id,
            name=country.name
        )
    
    @staticmethod
    def to_model(country_dto: CountryDTO) -> Country:
        return Country(
            id=country_dto.id,
            name=country_dto.name
        )
