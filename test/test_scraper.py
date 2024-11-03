import pytest
import pytest_asyncio
import aiohttp
from aioresponses import aioresponses
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from database import Base
from scraper import ProductScraperTexnoMart
from models import Product

DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


@pytest_asyncio.fixture
async def test_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield TestingSessionLocal
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture
async def db_session(test_db):
    async with test_db() as session:
        try:
            yield session
        finally:
            await session.rollback()


@pytest_asyncio.fixture
async def http_session():
    async with aiohttp.ClientSession() as session:
        yield session


@pytest.mark.asyncio
async def test_simple_http_mock():
    url = "https://texnomart.uz/katalog/noutbuki/"

    mocked_data = {"products": [{"name": "Laptop A", "price": 1000}]}

    with aioresponses() as m:
        m.get(url, status=200, payload=mocked_data)

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                assert response.status == 200
                data = await response.json()
                print("Mocked response data:", data)
                assert data == mocked_data, "The mocked response data should match expected data"

