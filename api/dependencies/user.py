# -*- coding: utf-8 -*-
from fastapi import Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from api import crud, models, schemas

from .auth.schemes import AccessTokenValidator
from .database import get_session

get_token_data = AccessTokenValidator()


async def get_current_user(
    session: AsyncSession = Depends(get_session),
    token_data: schemas.TokenPayload = Depends(get_token_data),
) -> models.User:
    user = await crud.user.get(session, id=token_data.sub)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not validate credentials, try to re-login.",
        )
    return user
