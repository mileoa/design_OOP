from abc import ABC

class SocialMediaUser(ABC):

    def __init__(self, user_id: int):
        """
        Постусловие: Создается объект пользователя
        """
        pass

    def send_message(self, text: str) -> int:
        """
        Предусловие: текст не пуст
        Постусловие: пользователю отправлено сообщение
        """
        pass


class TelegramUser(SocialMediaUser):

    def __init__(self, user_id: int):
        self._iuser_id int = user_id

    def send_message(self, text: str) -> int:
        print("Отправка сообщения через api telegram")


class VKUser(SocialMediaUser):

    def __init__(self, user_id: int):
        self._user_id: int = user_id

    def send_message(self, text: str) -> int:
        print("Отправка сообщения через api VK")


# Можно было бы использовать поле type для типа социальной сети, но при добавлении новых
# социальных сетей необходимо было расширять этот тип и вводить дополнительные проверки.