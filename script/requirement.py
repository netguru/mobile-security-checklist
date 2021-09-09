from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True, order=True)
class Requirement:
    id: int
    priority: str
    feature: str
    description: str
    references: List[str] = field(default_factory=List)

    @staticmethod
    def load_json(id, json):
        try:
            return Requirement(
                id= id,
                priority= json['priority'].capitalize(),
                feature= json['feature'],
                description= json['description'],
                references= json['references']
            )
        except Exception as e:
            print('Requirement', str(e))
