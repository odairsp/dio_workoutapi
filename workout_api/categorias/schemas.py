from typing import Annotated
from pydantic import Field

from workout_api.contrib.schemas import BaseSchema


class Categorias(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome da categoria", examples=["Scale"], max_length=10)
    ]
