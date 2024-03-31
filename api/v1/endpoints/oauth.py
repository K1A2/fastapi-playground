import hashlib

import httpx
from fastapi import APIRouter, Depends, Security, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from api.depends import get_mariadb
from crud.user import *

router = APIRouter()

security = HTTPBearer()

@router.get('/verify/google')
async def verify_google(
        credentials: HTTPAuthorizationCredentials = Security(security),
        db: Session = Depends(get_mariadb)):
    async with httpx.AsyncClient() as client:
        result = httpx.get('https://www.googleapis.com/oauth2/v3/userinfo', headers={
            'Authorization': f'Bearer {credentials.credentials}'
        })

    if result.status_code != 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Google User Not Found')
    result = result.json()
    id = hashlib.sha256(('google' + result['sub']).encode()).hexdigest()
    print(id)

@router.get('/verify/kakao')
async def verify_kakao(
        credentials: HTTPAuthorizationCredentials = Security(security),
        db: Session = Depends(get_mariadb)):
    async with httpx.AsyncClient() as client:
        result = httpx.get('https://kapi.kakao.com/v2/user/me', headers={
            'Authorization': f'Bearer {credentials.credentials}',
            'Content-type': f'application/x-www-form-urlencoded;charset=utf-8',
        })

    if result.status_code != 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Kakao User Not Found')

    result = result.json()
    id = hashlib.sha256(('kakao' + str(result['id'])).encode()).hexdigest()
    print(id)

@router.get('/verify/naver')
async def verify_kakao(
        credentials: HTTPAuthorizationCredentials = Security(security),
        db: Session = Depends(get_mariadb)):
    async with httpx.AsyncClient() as client:
        result = httpx.get('https://openapi.naver.com/v1/nid/me', headers={
            'Authorization': f'Bearer {credentials.credentials}',
        })

    if result.status_code != 200:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Naver User Not Found')

    result = result.json()
    print(result)
    id = hashlib.sha256(('naver' + str(result['response']['id'])).encode()).hexdigest()
    print(id)
