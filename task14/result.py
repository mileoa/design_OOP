import copy
import pickle
from typing import TypeVar, Generic
from typing import List, Iterator, Union
from random import randint


class General(object):

    def copy_form(self, from_object: "General") -> None:
        for key, value in from_object.__dict__.items():
            setattr(self, key, value)

    def deep_copy(self, from_object: "General"):
        object_copy = copy.deepcopy(from_object)
        for key, value in object_copy.__dict__.items():
            setattr(self, key, value)

    def clone(self) -> "General":
        return copy.deepcopy(self)

    def serialize(self) -> bytes:
        return pickle.dumps(self)

    def deserialize(self, deserialized_object: bytes) -> None:
        obj = pickle.loads(deserialized_object)
        self.__dict__.update(obj.__dict__)

    # печать (наглядное представление содержимого объекта в текстовом формате); Реализовано в object.__repr__

    def is_eq_type(self, given_object: "General") -> bool:
        return isinstance(self, type(given_object))

    def get_type(self):
        return type(self)

    def assignment_attempt(self, target: "General") -> "General":
        if isinstance(self, type(target)):
            return copy.deepcopy(self)
        return Void()


class Any(General):
    pass


class Void(Any):
    pass


T = TypeVar("T", bound=General)


class Vector(General, Generic[T]):

    def __init__(self, values: List[T]):
        self._values: List[T] = copy.deepcopy(values)
        self._size: int = len(self._values)

    def __getitem__(self, index: int) -> T:
        return self._values[index]

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[T]:
        for i in range(self._size):
            yield self._values[i]

    def __add__(self, other: "Vector[T]") -> Union["Vector[T]", Void]:
        if not isinstance(other, Vector):
            return Void()
        if self._size != len(other):
            return Void()
        result_values = []
        for i in range(self._size):
            result_values.append(self._values[i] + other[i])
        return Vector(result_values)

    def __repr__(self) -> str:
        return f"Vector({self._values})"


class Integer(Any):

    def __init__(self, value: int):
        self._value = value

    @property
    def value(self):
        return self._value

    def __add__(self, other_int: "Integer"):
        return Integer(self._value + other_int.value)

    def __repr__(self) -> str:
        return f"Integer({self._value})"


if __name__ == "__main__":
    # Vector([Integer(0), Integer(1), Integer(2), Integer(3), Integer(4), Integer(5), Integer(6), Integer(7), Integer(8), Integer(9)])
    integers_1: Vector[Integer] = Vector([Integer(x) for x in range(10)])

    # Vector([Integer(10), Integer(11), Integer(12), Integer(13), Integer(14), Integer(15), Integer(16), Integer(17), Integer(18), Integer(19)])
    integers_2: Vector[Integer] = Vector([Integer(x) for x in range(10, 20)])

    # Vector([Integer(10), Integer(12), Integer(14), Integer(16), Integer(18), Integer(20), Integer(22), Integer(24), Integer(26), Integer(28)])
    sum_of_integers: Union[Vector[Vector[Integer]], Void] = integers_1 + integers_2

    # Vector([Vector([Integer(0), Integer(1), Integer(2), Integer(3), Integer(4), Integer(5), Integer(6), Integer(7), Integer(8), Integer(9)]),
    #         Vector([Integer(0), Integer(1), Integer(2), Integer(3), Integer(4), Integer(5), Integer(6), Integer(7), Integer(8), Integer(9)])])
    vector_of_vectors_1: Vector[Vector[Integer]] = Vector(
        [Vector([Integer(x) for x in range(10)]) for _ in range(2)]
    )

    # Vector([Vector([Integer(10), Integer(11), Integer(12), Integer(13), Integer(14), Integer(15), Integer(16), Integer(17), Integer(18), Integer(19)]),
    #         Vector([Integer(10), Integer(11), Integer(12), Integer(13), Integer(14), Integer(15), Integer(16), Integer(17), Integer(18), Integer(19)])])
    vector_of_vectors_2: Union[Vector[Vector[Integer]], Void] = Vector(
        [Vector([Integer(x) for x in range(10, 20)]) for _ in range(2)]
    )

    # Vector([Vector([Integer(10), Integer(12), Integer(14), Integer(16), Integer(18), Integer(20), Integer(22), Integer(24), Integer(26), Integer(28)]),
    #         Vector([Integer(10), Integer(12), Integer(14), Integer(16), Integer(18), Integer(20), Integer(22), Integer(24), Integer(26), Integer(28)])])
    sum_vectors_of_vectors: Vector[Vector[Integer]] = (
        vector_of_vectors_1 + vector_of_vectors_2
    )

    vector_of_vectors_3: Vector[Vector[Integer]] = Vector([Vector([]), Vector([1])])
    vector_of_vectors_4: Vector[Vector[Integer]] = Vector([Vector([1]), Vector([1])])

    # Vector([<__main__.Void object at 0x7f1556ace350>, Vector([2])])
    sum_vectors_of_vectors_not_eq: Union[Vector[Vector[Integer]], Void] = (
        vector_of_vectors_3 + vector_of_vectors_4
    )
