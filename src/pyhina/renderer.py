from jinja2 import Environment, PackageLoader, select_autoescape
from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class ProjectInfo:
    project_name: str
    package_name: str
    python_minimum: str
    description: str = None
    license: str = None
    install_requires: List[str] = field(default_factory=list)


class SetuptoolsPackage:
    TEMPLATES = [
        "{{project_name}}/src/{{package_name}}/__init__.py.j2",
        "{{project_name}}/setup.cfg.j2",
        "{{project_name}}/setup.py.j2",
        "{{project_name}}/pyproject.toml.j2",
    ]

    def __init__(self):
        self._env = Environment(
            loader=PackageLoader(__package__, package_path="templates/setuptools"),
            autoescape=select_autoescape(),
        )
        self.paths = {t: self._env.from_string(t) for t in self.TEMPLATES}
        self.templates = {t: self._env.get_template(t) for t in self.TEMPLATES}

    def render_as_string(self, info: ProjectInfo) -> List[Tuple[str, str]]:
        return [
            (self._render_path(path, info), self._render_string(path, info))
            for path in self.TEMPLATES
        ]

    def _render_path(self, template_name, info: ProjectInfo) -> str:
        assert template_name in self.paths
        return self.paths[template_name].render(vars(info))

    def _render_string(self, template_name: str, info: ProjectInfo) -> str:
        assert template_name in self.templates
        return self.templates[template_name].render(vars(info))
