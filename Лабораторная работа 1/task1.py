# TODO Написать 3 класса с документацией и аннотацией типов
class AbstractMaterialEntity:
    """Абстрактный класс для материальных сущностей."""

    def __init__(self, weight: float, color: str):
        """
        Конструктор абстрактного класса материальной сущности.

        :param weight: Вес сущности. Должен быть положительным числом.
        :param color: Цвет сущности. Не должен быть пустым.
        """
        if weight <= 0:
            raise ValueError("Вес должен быть положительным числом.")
        if not color:
            raise ValueError("Цвет не может быть пустым.")

        self.weight = weight
        self.color = color

    @abstractmethod
    def describe(self) -> str:
        """Метод для описания сущности."""
        ...

    @abstractmethod
    def get_weight(self) -> float:
        """Метод для получения веса сущности."""
        ...


class Table(AbstractMaterialEntity):
    """Класс, представляющий стол."""

    def describe(self) -> str:
        """Возвращает описание стола.

        :return: Описание стола в виде строки.

        >>> table = Table(20.0, "brown")
        >>> table.describe()
        'Стол: цвет - brown, вес - 20.0 кг.'
        """
        return f"Стол: цвет - {self.color}, вес - {self.weight} кг."

    def get_weight(self) -> float:
        """Возвращает вес стола.

        :return: Вес стола.
        """
        return self.weight


class AbstractDigitalEntity(ABC):
    """Абстрактный класс для цифровых сущностей."""

    def __init__(self, name: str, created_at: str):
        """
        Конструктор абстрактного класса цифровой сущности.

        :param name: Имя сущности. Не должен быть пустым.
        :param created_at: Дата создания в формате 'YYYY-MM-DD'. Должна соответствовать формату даты.
        """
        if not name:
            raise ValueError("Имя не может быть пустым.")
        if not self.validate_date(created_at):
            raise ValueError("Некорректный формат даты. Ожидается 'YYYY-MM-DD'.")

        self.name = name
        self.created_at = created_at

    @staticmethod
    def validate_date(date_string: str) -> bool:
        """Проверяет корректность формата даты."""
        ...

    @abstractmethod
    def interact(self) -> str:
        """Метод для взаимодействия с цифровой сущностью."""
        ...

    @abstractmethod
    def get_name(self) -> str:
        """Метод для получения имени цифровой сущности."""
        ...


class SocialMediaPlatform(AbstractDigitalEntity):
    """Класс, представляющий социальную сеть."""

    def interact(self) -> str:
        """Возвращает сообщение о взаимодействии с платформой.

        :return: Сообщение о взаимодействии.

        >>> platform = SocialMediaPlatform("Facebook", "2004-02-04")
        >>> platform.interact()
        'Вы взаимодействуете с Facebook!'
        """
        return f"Вы взаимодействуете с {self.name}!"

    def get_name(self) -> str:
        """Возвращает имя платформы.

        :return: Имя платформы.
        """
        return self.name

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
