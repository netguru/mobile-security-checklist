from dataclasses import dataclass, field
from typing import List

from requirement import Requirement

@dataclass(frozen=True, order=True)
class RequirementsGroup:
    id: int
    name: str
    code: str
    requirements: List[Requirement] = field(default_factory=List)

    @staticmethod
    def load_json(id, json):
        try:
            return RequirementsGroup(
                id= id,
                name= json['name'],
                code= json['code'],
                requirements= RequirementsGroup.__load_requirements(json['requirements'])
            )
        except Exception as e:
            print('RequirementsGroup', str(e))

    @staticmethod
    def __load_requirements(json):
        requirements = []
        for i, requirement_json in enumerate(json, 1):
            requirements.append(Requirement.load_json(i, requirement_json))
        return requirements
