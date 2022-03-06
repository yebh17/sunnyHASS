from __future__ import annotations

from ..repositories.base import HacsRepository
from .base import ActionValidationBase, ValidationException


async def async_setup_validator(repository: HacsRepository) -> Validator:
    """Set up this validator."""
    return Validator(repository=repository)


class Validator(ActionValidationBase):
    async def async_validate(self):
        filenames = [x.filename.lower() for x in self.repository.tree]
        if self.repository.data.render_readme and "readme" in filenames:
            pass
        elif self.repository.data.render_readme and "readme.md" in filenames:
            pass
        elif "info" in filenames:
            pass
        elif "info.md" in filenames:
            pass
        else:
            raise ValidationException("The repository has no information file")
