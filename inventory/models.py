from django.db import models


# Vendor Model to store vendor details
class Vendor(models.Model):
    name = models.CharField(max_length=255)  # Keep only this one
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    # name = models.CharField(max_length=255)
    # address = models.TextField()
    contact = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name


# Asset Model - Updated with Vendor, SIM/Dongle Fields, asset_type, and status
class Asset(models.Model):
    ASSET_TYPE_CHOICES = [
        ('laptop', 'Laptop'),
        ('desktop', 'Desktop'),
        ('server', 'Server'),
        ('keyboard', 'Keyboard'),
        ('mouse', 'Mouse'),
        ('network_switch', 'Network Switch'),
        ('firewall', 'Firewall'),
        ('router', 'Router'),
        ('sim_card', 'SIM Card'),
        ('phone', 'Phone'),
        ('camera', 'Camera'),
    ]

    STATUS_CHOICES = [
        ('issued', 'Issued'),
        ('pending', 'Pending'),
        ('available', 'Available'),
    ]

    # Adding Vendor ForeignKey
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True, blank=True)

    # Asset Type and Status
    asset_type = models.CharField(max_length=50, choices=ASSET_TYPE_CHOICES, default='laptop')
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='available'  # or 'pending', 'issued' — choose what fits your use case
    )

    # SIM/Dongle Fields
    SIM_or_Dongle = models.CharField(max_length=50, choices=[('SIM', 'SIM'), ('Dongle', 'Dongle')])
    dongle_type = models.CharField(max_length=100, blank=True, null=True)
    dongle_id = models.CharField(max_length=100, blank=True, null=True)

    # SIM Specific Fields
    sim_name = models.CharField(max_length=255, blank=True, null=True)
    sim_phone_number = models.CharField(max_length=20, blank=True, null=True)
    sim_ccid_number = models.CharField(max_length=30, blank=True, null=True)

    # General Fields for all assets
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    assigned_to = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True)
    purchase_date = models.DateField()

    def __str__(self):
        return f"{self.name} ({self.asset_type})"

    @property
    def is_issued(self):
        return self.status == 'issued'

    @property
    def is_pending(self):
        return self.status == 'pending'


# Employee Model to store Employee information
class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15) 

    def __str__(self):
        return self.name

    # Method to get all assets assigned to this employee
    def get_assets(self):
        return Asset.objects.filter(assigned_to=self)


# Laptop Model to store Laptop asset details
class Laptop(models.Model):
    serial_number = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    specifications = models.TextField()
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.serial_number


# Desktop Model to store Desktop asset details
class Desktop(models.Model):
    serial_number = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    specifications = models.TextField()
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.serial_number


# Server Model to store Server details
class Server(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True)
    os = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# VirtualMachine Model to store Virtual Machine details
class VirtualMachine(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Keyboard Model to store Keyboard details
class Keyboard(models.Model):
    brand = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.serial_number


# Mouse Model to store Mouse details
class Mouse(models.Model):
    brand = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.serial_number


# NetworkSwitch Model to store Network Switch details
class NetworkSwitch(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Firewall Model to store Firewall details
class Firewall(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Router Model to store Router details
class Router(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# SIMCard Model - Modified with SIM Details
class SIMCard(models.Model):
    sim_number = models.CharField(max_length=20)
    provider = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.sim_number


# Phone Model to store Phone details
class Phone(models.Model):
    model = models.CharField(max_length=100)
    imei = models.CharField(max_length=20)
    assigned_to = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    assigned_to = models.ForeignKey(
        'Employee', 
        on_delete=models.CASCADE,
        related_name='phones'  # Change this to something unique like 'phones'
    )
    def __str__(self):
        return self.model


# Camera Model to store Camera details
class Camera(models.Model):
    model = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    vendor = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.model
