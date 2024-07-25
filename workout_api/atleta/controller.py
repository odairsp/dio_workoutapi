from uuid import uuid4
from fastapi import APIRouter, Body, status
from workout_api.atleta.models import AtletaModel
from workout_api.atleta.schemas import AtletaIn, AtletaOut
from workout_api.contrib.dependencies import DatabaseDependency
from datetime import datetime, timezone

router = APIRouter()


@router.post(
    path="/", summary="Criar um novo atleta", status_code=status.HTTP_201_CREATED
)
async def post(db_session: DatabaseDependency, atleta_in: AtletaIn = Body(...)):

    atleta_out = AtletaOut(
        id=uuid4(), created_at=datetime.now(timezone.utc), **atleta_in.model_dump()
    )
    atleta_model = AtletaModel(**atleta_out.model_dump())
    db_session.add(atleta_model)
    await db_session.commit()

    return atleta_out
