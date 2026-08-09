class Car:
    """Przedstawia samochód i jego parametry"""

    def __init__(
            self,
            comfort_class: int,
            clean_mark: int,
            brand: str
    ) -> None:
        try:
            comfort_class = int(comfort_class)
            clean_mark = int(clean_mark)
        except (TypeError, ValueError):
            raise ValueError(
                "Klasa komfortu i stopień czystości musi być cyfrą"
            )

        if not isinstance(brand, str):
            raise TypeError("Marka samochodu musi być tekstem")

        if not (1 <= comfort_class <= 7):
            raise ValueError("Podaj zakres od 1 do 7")

        if not (1 <= clean_mark <= 10):
            raise ValueError("Podaj zakres od 1 do 10")

        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    """Dane techniczne i pomiarowe myjni"""

    def __init__(
            self,
            distance_from_city_center: float,
            clean_power: int,
            average_rating: float,
            count_of_ratings: int
    ) -> None:
        try:
            distance_from_city_center = float(distance_from_city_center)
            clean_power = int(clean_power)
            average_rating = float(average_rating)
            count_of_ratings = int(count_of_ratings)
        except (TypeError, ValueError):
            raise ValueError("Wartość podaj w liczbach")

        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

        if not (1.0 <= distance_from_city_center <= 10.0):
            raise ValueError("Podaj wartość w zakresie 1.0 - 10.0")

        if not (1.0 <= average_rating <= 5.0):
            raise ValueError("Podaj wartość w zakresie 1.0 - 5.0")

        self.distance_from_city_center = round(distance_from_city_center, 1)
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        """Myjnia samochodowa"""

        price_all_car = []
        for car in cars:
            if car.clean_mark < self.clean_power:
                print(f"Samochód {car.brand} jest myty")
                price_one_car = round(car.comfort_class
                                      * (self.clean_power - car.clean_mark)
                                      * self.average_rating
                                      / self.distance_from_city_center, 1)
                price_all_car.append(price_one_car)
            else:
                print
                (
                    f"""Samochód {car.brand} jest zbyt duży
                    aby go umyć w tej cenie"""
                )
        return sum(price_all_car)

    def calculate_washing_price(self, car: Car) -> float:
        """Obliczanie kosztu mycia pojedynczego samochodu"""

        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center, 1)

    def wash_single_car(self, car: str) -> None:
        if self.clean_power > car.clean_mark:
            print(f"Mycie samochodu {car.brand}")
            car.clean_mark = self.clean_power
            return car.clean_mark
        else:
            return f"""
                     Samochód {car.brand}
            ma za duży 'clean mark' nie może być umyty
            """


bmw = Car(comfort_class=3, clean_mark=9, brand="BMW")
audi = Car(comfort_class=4, clean_mark=9, brand="Audi")

wash_station = CarWashStation(
    distance_from_city_center=5,
    clean_power=6,
    average_rating=3.5,
    count_of_ratings=6
)

# income = wash_station.serve_cars([bmw, audi])
# print(bmw.clean_mark)
# print(audi.clean_mark)
# price_car = wash_station.calculate_washing_price(audi)
# print(price_car)

wash_car = wash_station.wash_single_car(bmw)
print(wash_car)
