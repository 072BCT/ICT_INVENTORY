from django.db import models
import datetime


# Create your models here.
class Item(models.Model):
    WORKING = 'WK'
    OUT_OF_ORDER = 'OO'
    IN_MAINTENANCE = 'IM'
    STATUS_CHOICES = (
        (WORKING, 'Working'),
        (OUT_OF_ORDER, 'Out of Order'),
        (IN_MAINTENANCE, 'In Maintenance')
    )
    id = models.CharField(max_length=20, primary_key=True, help_text='Enter the ID of the item')
    name = models.CharField(max_length=50, default='Generic', help_text='Enter the brand name of the item')
    model = models.CharField(max_length=50, default='Generic', help_text='Enter the model of the item')
    serial_no = models.CharField(max_length=50, unique=True, null='True',
                                 help_text='Enter the serial number of the item')
    cost = models.DecimalField(decimal_places=2, max_digits=10, null=True, help_text='Enter the cost of the item')
    room = models.ForeignKey('Room', null=True, on_delete=models.SET_NULL, help_text='Select room where it is kept')
    date_of_acquire = models.DateField(default=datetime.date.today, help_text='Enter the date of acquire')
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=WORKING)
    created = models.DateTimeField(auto_now_add=True, null=True)
    last_modified = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.name, self.model)


class Room(models.Model):
    id = models.CharField(max_length=20, primary_key=True, help_text='Enter the id of room')
    floor = models.PositiveSmallIntegerField(help_text='In which floor is this room?')
    additional_item = models.ManyToManyField('AdditionalItem', through='RoomHasAdditionalItem',
                                             through_fields=('room', 'additional_item'), help_text='Additional Item')

    def __str__(self):
        return self.id


class Computer(Item):
    name = models.CharField(max_length=50, default='Generic', help_text='Enter the brand name of the item')
    model = models.CharField(max_length=50, default='Generic', help_text='Enter the model of the item')


class Printer(Item):
    ip_address = models.GenericIPAddressField(help_text='Enter the ip address for this printer')


class Laptop(Item):
    pass


class NetworkSwitch(Item):
    no_of_ports = models.PositiveSmallIntegerField(help_text='Enter the number of ports')
    no_of_SFP_ports = models.PositiveSmallIntegerField(help_text='Enter the number of SFP ports')

    class Meta:
        verbose_name_plural = 'Network Switches'


class AdditionalItem(models.Model):
    id = models.CharField(max_length=10, primary_key=True, help_text='Enter the id of the item')
    name = models.CharField(max_length=20, help_text='What is the item called?')

    def __str__(self):
        return "{0} - {1}".format(self.name, self.id)


class RoomHasAdditionalItem(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, help_text='Select the Room')
    additional_item = models.ForeignKey(AdditionalItem, on_delete=models.CASCADE,
                                        help_text='Select the Additional Item')
    quantity = models.PositiveSmallIntegerField(help_text='Enter the number of items')
    no_of_defect_items = models.PositiveSmallIntegerField(help_text='How many items are defect?')
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "{0} - {1}".format(self.room, self.additional_item.name)


class StoreItemName(models.Model):
    name = models.CharField(max_length=50, help_text='Enter the name of the item')

    def __str__(self):
        return self.name


class StoreItem(models.Model):
    name = models.OneToOneField(StoreItemName, primary_key=True, on_delete=models.PROTECT,
                                help_text='Pick the Store Item Name')
    quantity = models.PositiveSmallIntegerField(help_text='Enter the quantity of Store Item')
    last_modified = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name.name
