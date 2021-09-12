"""Implementation of RequirementsGroup model"""
from dataclasses import dataclass, field
from typing import List

from requirement import Requirement

@dataclass(frozen=True, order=True)
class RequirementsGroup:
    """Model representing a group of requirements, eg. Defaults in Shared Category

    Attributes
    ----------
    uuid : int
        number identifier of the Requirements Group, unique within parent Category
    name : str
        name of the Requirements Group
    code : str
        shortened Requirements Group name used as Requirement uuid prefix
    requirements : List[Requirement]
        list of Requirements within the Requirements Group

    Methods
    -------
    load_json(uuid, json)
        Initializes RequirementsGroup object with given JSON dictionary and unique identifier
    """

    uuid: int
    name: str
    code: str
    requirements: List[Requirement] = field(default_factory=List)

    @staticmethod
    def load_json(uuid, json):
        """Initializes Requirements Group object with given JSON dictionary and unique identifier.

        Returns new Requirements Group object.
        If JSON data doesn't contain required data will return None.

        Parameters
        ----------
        uuid: int
            number identifier of the Requirements Group, unique within parent Category
        json: dict
            dictionary with JSON data of the Requirements Group
        """

        try:
            return RequirementsGroup(
                uuid=uuid,
                name=json['name'],
                code=json['code'],
                requirements= RequirementsGroup.__load_requirements(json['requirements'])
            )
        except KeyError as e:
            print(f'Load RequirementsGroup error, no such key as {e}.')
            return None

    @staticmethod
    def __load_requirements(json):
        requirements = []
        for i, requirement_json in enumerate(json, 1):
            requirements.append(Requirement.load_json(i, requirement_json))
        return requirements
