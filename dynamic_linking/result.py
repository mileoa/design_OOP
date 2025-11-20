from abc import ABC, abstractmethod


class Sender(ABC):
    @abstractmethod
    def send(text: str, destination: str) -> bool:
        pass


class EmailSenser(Sender):
    def send(text: str, destination: str) -> bool:
        print("Отправлен через email")


class SMSSenser(Sender):
    def send(text: str, destination: str) -> bool:
        print("Отправлен через sms")


class TelegramSenser(Sender):
    def send(text: str, destination: str) -> bool:
        print("Отправлен через telegram")


senders = [EmailSenser(), SMSSenser(), TelegramSenser()]
for sender in senders:
    sender.send(text, destination, sender)  # Динамическое связывание
