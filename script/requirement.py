"""Implementation of Requirement model"""
from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True, order=True)
class Requirement:
    """Model representing a single security requirement

    Attributes
    ----------
    uuid : int
        number identifier of the Requirement, unique within parent Group
    priority : str
        priority of the Security Requirement, can be one of [low, medium, high, critical]
    feature : str
        short description of application feature that implies this Requirement
    description : str
        description of the Requirement and required implementation
    references : List[str]
        list of URLs to articles that provide broader description of the security issue

    Methods
    -------
    load_json(uuid, json)
        Initializes Requirement object with given JSON dictionary and unique identifier
    """

    uuid: int
    priority: str
    feature: str
    description: str
    references: List[str] = field(default_factory=List)

    @staticmethod
    def load_json(uuid, json):
        """Initializes Requirement object with given JSON dictionary and unique identifier.

        Returns new Requirement object.
        If JSON data doesn't contain required data will return None.

        Parameters
        ----------
        uuid: int
            number identifier of the Requirement, unique within parent Category
        json: dict
            dictionary with JSON data of the Requirement
        """

        try:
            return Requirement(
                uuid=uuid,
                priority=json['priority'].capitalize(),
                feature=json['feature'],
                description=json['description'],
                references=json['references']
            )
        except KeyError as e:
            print(f'Load Requirement error, no such key as {e}.')
            return None
