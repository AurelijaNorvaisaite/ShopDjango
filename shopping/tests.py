
import pytest

# pip install django-stubs, pip istall djangopytest
from django.db.models.aggregates import Avg, Count
# agregacijos labai svarbios, norint greiciau atlikti skaiciavimus ir neapkrauti duombazes vis nuskaitinejant duomenis

from products.models import Product, Category


@pytest.mark.django_db  # feikinė duombazė
def test():
    category = Category.objects.create(name="1")
    product = Product.objects.create(name="Hello world!", price=50, category=category)
    assert Product.objects.get(pk=product.pk).name == "Hello world!"
    assert Product.objects.count() == 1
    assert Product.objects.latest("pk").name == "Hello world!"
    assert Product.objects.filter(name="Hello world!").count() == 1
    assert Product.objects.filter(name="Hello world!").exists()
    assert Product.objects.filter(name__startswith="Hel")
    # Total number of products with name="Hello world!"
    assert Product.objects.filter(name='Hello world!').count()
    assert Product.objects.aggregate(Avg('price'))
    assert Product.objects.annotate(Count('name'))


@pytest.mark.django_db
def test_product_view(client):
    response = client.get('/products')
    assert response.status_code == 301

@pytest.mark.django_db
def test_product_list(client):
    laptops = Category.objects.create(name='Laptops')
    Product.objects.create(name='ThingPad T450', price='700', category=laptops)
    Product.objects.create(name='Latitude E6530', price='700', category=laptops)
    resp = client.get('/products/list/')
    assert resp.status_code == 200
    assert 'products' in resp.context
    assert list(resp.context['products'].values_list('name', flat=True)) == [
        'ThingPad T450',
        'Latitude E6530',
    ]






