import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Product
from mediapark import parse_and_store

# Setup a test database
SQLITE_TEST_DB = "sqlite:///./test.db"
engine = create_engine(SQLITE_TEST_DB)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_parse_and_store(test_db):
    html = """
    <div class="product-card">
        <div class="product-name">Test Product</div>
        <div class="product-price">$99.99</div>
        <div class="product-category">Electronics</div>
        <img src="http://example.com/image.jpg" />
        <div class="product-description">A sample description</div>
    </div>
    """
    parse_and_store(test_db, html)

    # Verify that data was inserted
    product = test_db.query(Product).first()
    assert product.name == "Test Product"
    assert product.price == 99.99
    assert product.category == "Electronics"
    assert product.image_url == "http://example.com/image.jpg"
    assert product.description == "A sample description"