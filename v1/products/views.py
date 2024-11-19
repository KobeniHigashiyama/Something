from typing import List
from core.model import db
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends, HTTPException
from . import crud
from .schemas import ProductCreate, Product, ProductUpdate, ProductUpdatePartical
from dependencies import product_by_id

router = APIRouter(prefix="/products", tags=["products"])


@router.get("/", response_model=List[Product])
async def get_products(
    session: AsyncSession = Depends(db.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}", response_model=Product)
async def get_product(
    product: Product = Depends(product_by_id),
):
    return product


@router.put(
    "/{product_id}",
)
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
):
    return await crud.update_product(
        session=session, product=product, product_update=product_update
    )


@router.patch(
    "/{product_id}",
)
async def update_product_partial(
    product_update: ProductUpdatePartical,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
):
    return await crud.update_product(
        session=session, product=product, product_update=product_update, partial=True
    )


@router.delete(
    "/{product_id}",
)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db.scoped_session_dependency),
) -> None:
    await crud.delete_product(session=session, product=product)
