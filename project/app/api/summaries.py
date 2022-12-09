from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.tortoise import SummarySchema
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()


@router.post('/', response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_obj = {'id': summary_id, 'url': payload.url}
    return response_obj


@router.get('/{id}/', response_model=SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(
            status_code=404, detail='Summary with such id was not found')

    return summary


@router.get('/', response_model=list[SummarySchema])
async def read_all_summaries() -> list[SummarySchema]:
    summaries = await crud.get_all()
    return summaries
