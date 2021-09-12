"""Implementation of Category model"""
from dataclasses import dataclass, field
from typing import List

from requirements_group import RequirementsGroup


@dataclass(frozen=True, order=True)
class Category:
    """Model representing a category of requirements, eg. GDPR, iOS

    Attributes
    ----------
    uuid : int
        unique number identifier of the Category
    name : str
        name of the Category
    description : str
        short description of the Category
    code : str
        shortened Category name used as Requirement uuid prefix
    requirements : List[RequirementsGroup]
        list of Requirements Groups within the Category

    Methods
    -------
    genereate_markdown()
        Generates Markdown content with the Category data
    load_json(uuid, json)
        Initializes Category object with given JSON dictionary and unique identifier
    """
    uuid: int
    name: str
    description: str
    code: str
    groups: List[RequirementsGroup] = field(default_factory=List)

    def genereate_markdown(self):
        """Generates Markdown content with the Category data"""
        markdown = self.__generate_base_template()
        should_add_header = len(self.groups) > 1
        for group in self.groups:
            markdown += self.__generate_group_table(group, should_add_header, self.code)
        return markdown

    def __generate_base_template(self):
        return f"# {self.description}\n"

    @classmethod
    def __generate_group_table(cls, group, should_add_header, category_code='', ):
        markdown = '' if not should_add_header else f'\n## {group.name}\n\n'
        markdown += '| ID  | Priority | Feature | Description | Link |\n'
        markdown += '| --  | -- | ---------------------- | ---------------------- | - |\n'
        for requirement in group.requirements:
            group_code = group.code if should_add_header else ""
            markdown += f'| {category_code}{group_code}.{requirement.id} | '
            markdown += f'{requirement.priority} | '
            markdown += f'{requirement.feature} | '
            markdown += f'{requirement.description} | '
            refs = [f"[{cls.uuid}]({ref})" for id, ref in enumerate(requirement.references, 1)]
            markdown += f'{"".join(refs)} |\n'
        markdown += '\n'
        return markdown

    @staticmethod
    def load_json(uuid, json):
        """Initializes Category object with given JSON dictionary and unique identifier

        Returns new Category object.
        If JSON data doesn't contain required data will return None.

        Parameters
        ----------
        uuid: int
            unique number identifier of the Category
        json: dict
            dictionary with JSON data of the Category
        """
        try:
            return Category(
                uuid=uuid,
                name=json['name'],
                description=json['description'],
                code=json['code'],
                groups=Category.__load_requirements_groups(json['groups'])
            )
        except KeyError as e:
            print(f'Load RequirementsGroup error, no such key as {e}.')
            return None

    @staticmethod
    def __load_requirements_groups(json):
        requirements_groups = []
        for i, group_json in enumerate(json, 1):
            requirements_groups.append(RequirementsGroup.load_json(i, group_json))
        return requirements_groups
