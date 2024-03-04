from rest_framework.test import APITestCase
from rest_framework import status
from .models import Invoice, InvoiceDetail

class InvoiceAPITestCase(APITestCase):
    def setUp(self):
        self.invoice_data = {'date': '2024-03-05', 'customer_name': 'John Doe'}
        self.invoice_detail_data = {'description': 'Product A', 'quantity': 1, 'unit_price': 10, 'price': 10}

    def test_create_invoice(self):
        response = self.client.post('/invoices/', self.invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Create Invoice Response:", response.content)

    def test_create_invoice_detail(self):
        invoice = Invoice.objects.create(**self.invoice_data)
        self.invoice_detail_data['invoice'] = invoice.id
        response = self.client.post('/invoicedetails/', self.invoice_detail_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print("Create Invoice Detail Response:", response.content)

    def test_update_invoice(self):
        invoice = Invoice.objects.create(**self.invoice_data)
        updated_invoice_data = {'date': '2024-03-06', 'customer_name': 'Jane Doe'}
        response = self.client.put(f'/invoices/{invoice.id}/', updated_invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Update Invoice Response:", response.content)

    def test_update_invoice_detail(self):
        invoice = Invoice.objects.create(**self.invoice_data)
        invoice_detail = InvoiceDetail.objects.create(invoice=invoice, **self.invoice_detail_data)
        updated_invoice_detail_data = {'description': 'Updated Product A', 'quantity': 2, 'unit_price': 20, 'price': 40, 'invoice': invoice.id}
        response = self.client.put(f'/invoicedetails/{invoice_detail.id}/', updated_invoice_detail_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Update Invoice Detail Response:", response.content)
