from django.db import models

# Customer Model
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

# Category Model
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

# Brand Model
class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True)
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name

# Barcode Model
class Barcode(models.Model):
    barcode_id = models.AutoField(primary_key=True)
    barcode_value = models.CharField(max_length=50)

    def __str__(self):
        return self.barcode_value

# Product Model
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    barcode = models.ForeignKey(Barcode, on_delete=models.SET_NULL, null=True)
    store_keeping_unit = models.CharField(max_length=50)
    product_name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Product ID: {self.product_id}, Category: {self.category}, Brand: {self.brand}, Barcode: {self.barcode}, SKU: {self.store_keeping_unit}, Product Name: {self.product_name}, Description: {self.description}, Quantity: {self.quantity}, Reorder Level: {self.reorder_level}, Cost Price: {self.cost_price}, Selling Price: {self.selling_price}"

# Inventory Model
class Inventory(models.Model):
    history_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    availability = models.CharField(max_length=10, choices=[('In Stock', 'In Stock'), ('Sold', 'Sold'), ('Restocked', 'Restocked')])
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inventory for {self.product.product_name}"

# Sale Model
class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    date_time_stamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])
    payment_method = models.CharField(max_length=50)
    bank_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"Sale ID: {self.sale_id}, Customer: {self.customer}, Total Amount: {self.total_amount}"

# SaleDetail Model
class SaleDetail(models.Model):
    sale_detail_id = models.AutoField(primary_key=True)
    sale = models.ForeignKey(Sale, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale Detail ID: {self.sale_detail_id}, Sale: {self.sale}, Product: {self.product}, Quantity: {self.quantity}, Unit Price: {self.unit_price}"

# SalesReport Model
class SalesReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    report_type = models.CharField(max_length=10, choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')])
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_profit = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sales Report ID: {self.report_id}"

# StockReport Model
class StockReport(models.Model):
    report_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"Stock Report ID: {self.report_id}"
