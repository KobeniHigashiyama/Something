from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.model import db, Product
from . import crud
from typing import Annotated


async def product_by_id(
    product_id: Annotated[
        int, Path(title="Product ID", description="ID of the product to retrieve")
    ],
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> Product:
    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product with ID {product_id} not found",
    )
