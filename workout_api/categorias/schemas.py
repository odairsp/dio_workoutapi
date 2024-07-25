from typing import Annotated
from pydantic import UUID4, Field

from workout_api.contrib.schemas import BaseSchema


class Categorias(BaseSchema):
    nome: Annotated[
        str, Field(description="Nome da categoria", examples=["Scale"], max_length=10)
    ]


class CategoriaIn(Categorias):
    pass


class CategoriaOut(Categorias):
    id: Annotated[UUID4, Field(description="Identificador da categoria")]
    pass
