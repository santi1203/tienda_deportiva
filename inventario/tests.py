from django.test import TestCase
from .models import Categoria, Producto
from decimal import Decimal

class CategoriaProductoTestCase(TestCase):

    def setUp(self):
        self.categoria = Categoria.objects.create(
            nombre="Fútbol",
            descripcion="Ropa y accesorios deportivos"
        )

        self.producto = Producto.objects.create(
            nombre="Balón Adidas",
            descripcion="Balón profesional de entrenamiento",
            precio=Decimal("129900.00"),
            cantidad=10,
            categoria=self.categoria
        )

    def test_categoria_creada(self):
        """Verifica que la categoría se haya creado correctamente."""
        self.assertEqual(self.categoria.nombre, "Fútbol")

    def test_producto_relacionado_con_categoria(self):
        """Verifica que el producto esté correctamente asociado a la categoría."""
        self.assertEqual(self.producto.categoria, self.categoria)

    def test_precio_es_decimal(self):
        """Verifica que el precio del producto sea tipo Decimal (como requiere Django)."""
        self.assertIsInstance(self.producto.precio, Decimal)
