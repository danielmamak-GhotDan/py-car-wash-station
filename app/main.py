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
    # write your code here
    pass
