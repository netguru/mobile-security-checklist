from dataclasses import dataclass, field
from typing import List

from requirements_group import RequirementsGroup

@dataclass(frozen=True, order=True)
class Category:
    id: int
    name: str
    description: str
    code: str
    groups: List[RequirementsGroup] = field(default_factory=List)

    def genereate_markdown(self):
        markdown = self.__generate_base_template()
        for requirements_group in self.groups:
            markdown += self.__generate_group_table(requirements_group, len(self.groups) > 1, self.code)
        return markdown

    def __generate_base_template(self):
        return f"# {self.description}\n"

    def __generate_group_table(self, group, should_add_header, category_code='', ):
        markdown = '' if not should_add_header else f'\n## {group.name}\n'
        markdown += '\n| ID  | Priority | Feature | Description | Link |\n| --  | -- | ---------------------- | ---------------------- | - |\n'
        for requirement in group.requirements:
            markdown += f'| {category_code}{group.code if should_add_header else ""}.{requirement.id} | {requirement.priority} | {requirement.feature} | {requirement.description} | {"".join([f"[{id}]({reference})" for id, reference in enumerate(requirement.references, 1)])} |\n'
        markdown += '\n'
        return markdown

    @staticmethod
    def load_json(id, json):
        try:
            return Category(
                id= id,
                name= json['name'],
                description= json['description'],
                code= json['code'],
                groups= Category.__load_requirements_groups(json['groups'])
            )
        except Exception as e:
            print('Category:', str(e))

    @staticmethod
    def __load_requirements_groups(json):
        requirements_groups = []
        for i, requirements_group_json in enumerate(json, 1):
            requirements_groups.append(RequirementsGroup.load_json(i, requirements_group_json))
        return requirements_groups
