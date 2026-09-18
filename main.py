def check_capacity_car(is_ready_car: bool, capacity: int, requested_passengers: int) -> bool:
    return ((capacity >= requested_passengers) and (requested_passengers > 0) and (is_ready_car))

def calculate_trip_cost(distance: float, rate_for_km: float, is_cargo: bool, is_urgent: bool):

    base_sum = distance * rate_for_km

    if is_cargo and is_urgent:
        base_sum *= 2
    elif is_cargo and not is_urgent :
        base_sum *= 1.5
    elif not is_cargo and is_urgent:
        base_sum *= 1.3

    return round(base_sum, 2)

def calculation_travel_time(distance: float, avg_speed_kmh: float, has_trafic: bool):
    base_time = distance / avg_speed_kmh
    base_time *= 3600

    if has_trafic:
        base_time *= 1.4

    return f"Время пути составит {int(base_time // 3600)} ч. {int((base_time % 3600) / 60)} мин."

    
def main():
    route_name = "Москва - Тверь"
    distance = 340.0
    car_model = "Газель"
    capacity = 25
    is_ready = True

    passengers = 10
    is_cargo = True
    is_urgent = False
    trafic = False

    if check_capacity_car(is_ready, capacity, passengers):
        return {
            "Маршрут": route_name,
            "Модель машины": car_model,
            "Стоимоcть поездки": calculate_trip_cost(distance, 70, is_cargo, is_urgent),
            "Время поездки": calculation_travel_time(distance, 70, trafic)
        }

    else:
        return ("Назначенное транспортное средство не может выполнить рейс!")

if __name__ == "__main__":
    print(main())
