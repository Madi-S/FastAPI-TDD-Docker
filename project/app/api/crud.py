from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary, SummarySchema


async def post(payload: SummaryPayloadSchema) -> int:
    '''Returns created summary id'''
    summary = TextSummary(
        url=payload.url,
        summary='test summary'
    )
    await summary.save()
    return summary.id


async def get(id: int) -> dict | None:
    '''Returns summary by id'''
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary

    return None


async def get_all() -> list:
    summaries = await TextSummary.all().values()
    return summaries
