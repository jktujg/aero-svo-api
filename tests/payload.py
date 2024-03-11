from pydantic import BaseModel, ConfigDict


class Payload(BaseModel):
    model_config = ConfigDict(extra='allow')


class AircraftPayload(Payload):
    aircraft_type_id: int = 25
    aircraft_type_name: str = 'Boeing 777-300ER'


class CountryPayload(Payload):
    region: str = 'NORTH AMERICA'
    country: str = 'Куба'


class CityPayload(Payload):
    city_eng: str = 'Moscow'
    city: str = 'Москва'
    timezone: str = 'DOMESTIC'
    country: CountryPayload = CountryPayload()


class AirportPayload(Payload):
    id: int = 5
    iata: str = 'VRA'
    icao: str = 'MUVR'
    rus: str = 'ВРА'
    airport: str = 'Хуан\xa0Гуальберто\xa0Гомес'
    airport_rus: str = 'Хуан\xa0Гуальберто\xa0Гомес'
    region: str = 'NORTH AMERICA'
    country: str = 'Куба'
    city: str = 'Варадеро'
    city_eng: str = 'Varadero'
    lat: str = '23.039896'
    long: str = '-81.436943'
    timezone: str = 'America/Havana'


class CompanyPayload(Payload):
    name: str = 'Nordwind Airlines'
    code: str = 'N4'
    onlineBuy: str = 'https://nordwindairlines.ru/'
    onlineRegister: str = 'https://airbook.nordwindairlines.ru/check-in/?lang=ru#search'


class FlightPayload(Payload):
    i_id: str = '8770878'
    ad: str = 'A'
    flt: str = '556'
    dat: str = '2023-12-19T00:00:00+03:00'
    mar1: AirportPayload = AirportPayload()
    mar2: AirportPayload = AirportPayload()
    co: CompanyPayload = CompanyPayload()
    fplTime: str = '2023-12-19T18:55:00+03:00'
    marArrivalEt: str = '2023-12-19T18:55:00+03:00'
    t_at: str = '2023-12-20T04:27:02+03:00'
    term: str = 'C'
    old_term: str = 'C'
    t_st: str = '2023-12-19T18:55:00+03:00'
    t_et: str = '2023-12-20T04:54:00+03:00'
    chin_id: str = '312-315'
    t_chin_start: str = '2023-12-19T18:55:00+03:00'
    t_chin_finish: str = '2023-12-19T18:55:00+03:00'
    gate_id: str = '1a'
    old_gate_id: str = '12'
    t_boarding_start: str = '2023-12-19T18:55:00+03:00'
    t_bording_finish: str = '2023-12-19T18:55:00+03:00'
    bbel_id: str = '1-2'
    old_bbel_id: str = '1-2'
    bbel_start: str = '2023-12-20T04:56:00+03:00'
    bbel_finish: str = '2023-12-20T05:25:00+03:00'
    main_flight: str = '8770879'
    status_code: str = '12'
    status_id: str = '70'
    aircraft_type_id: str = '25'
    estimated_chin_start: str = '2023-12-19T18:55:00+03:00'
    estimated_chin_finish: str = '2023-12-19T18:55:00+03:00'
    estimated_bag_start: str = '2023-12-20T04:56:00+03:00'
    t_st_mar: str = '2023-12-19T05:00:00+03:00'
    t_at_mar: str = '2023-12-19T16:00:00+03:00'
    way_time: str = '693'
    t_otpr: str = '2023-12-19T18:55:00+03:00'
    t_prb: str = ''
    term_gate: str = 'C'
    old_term_gate: str = 'C'
    aircraft_type_name: str = 'Boeing 777-300ER'






