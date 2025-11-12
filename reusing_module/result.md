# Принципы повторного использования модуля
В python поддерживаются следующие приципы повторного использования модуля:
1. Параметризация другими типами:
```
from typing import Generic, TypeVar

T = TypeVar("T")

class PowerSet(PowerSetATD, Generic[T]):
    pass

class PowerSetBasic(PowerSetATD, Generic[int | str]):
    pass

ps = PowerSet[int]()

ps_int = PowerSetBasic()
```
2. Объединение несколько функций
```
# math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
```
3. Объединение модулей в семейство модулей
```
# На уровне пакета
# project/
#   ── data_processing/
#      ── __init__.py
#      ── parsers.py
#      ── transformers.py
#      ── validators.py

# На уровне модуля
# validators.py
class ValidateXML:
    pass

class ValidateCSV:
    pass
```
4. Частично может предлагать конкретную реализацию родительского модуля, которая должна выбираться динамически (полиморфно). Работает только с первым параметром в сигнатруе.
```
from functools import singledispatch

@singledispatch
def hello(arg):
    raise TypeError("Unsupported type")

@hello.register
def _(arg: str):
    print(f"Hello {arg}")

@hello.register
def _(arg: int):
    print(f"Your age is {arg}")
```
