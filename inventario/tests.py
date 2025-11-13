from django.test import TestCase
from .models import Categoria, Producto

class CategoriaProductoTestCase(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nombre="Fútbol", descripcion="Ropa y accesorios deportivos")
        self.producto = Producto.objects.create(
            nombre="Balón Adidas",
            descripcion="Balón profesional de entrenamiento",
            precio=129900,
            cantidad=10,
            categoria=self.categoria
        )

    def test_categoria_creada(self):
        self.assertEqual(self.categoria.nombre, "Fútbol")

    def test_producto_relacionado_con_categoria(self):
        self.assertEqual(self.producto.categoria.nombre, "Fútbol")

    def test_precio_es_decimal(self):
        self.assertIsInstance(self.producto.precio, type(self.producto.precio))
