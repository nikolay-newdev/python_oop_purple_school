from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional


string = TypeVar('string', bound=str)
number = TypeVar('number', bound=int)

@dataclass
class Cache(Generic[string, number]):
    data: list[dict[string, number]] = field(default_factory=list)

    def set(self, key: string, val: number) -> list[dict[string, number]]:
        self.data.append({key: val})
        return self.data

    def get(self, key: string) -> Optional[number]:
        for d in self.data:
            k, *other = d
            if k == key:
                return d[key]
        return None

    def keys(self) -> list[string]:
        lst = []
        for d in self.data:    
            lst.append(next(iter(d)))
        return lst

    def values(self) -> list[number]:
        lst = []
        for d in self.data:
            name = next(iter(d))
            lst.append(d[name])
        return lst
   


hits = Cache[str, int]()
hits.set("home", 10)
hits.set("about", 3)
print(hits.data)
x = hits.get("home")        # x: int | None
print(x)
paths = hits.keys()         # list[str]
print(paths)
counts = hits.values()      # list[int]
print(counts)

hits.set("contacts", "5")   # ❌ ошибка типов
print(hits.set("contacts", "5"))
hits.get(123)               # ❌ ошибка типов
print(hits.get(123))