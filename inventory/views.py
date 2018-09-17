from django.shortcuts import render
from .models import Computer, Room, Printer, NetworkSwitch, Laptop, RoomHasAdditionalItem


# Create your views here.


def index(request):
    opts = Computer._meta
    floor_values = Room.objects.values('floor').distinct().order_by('floor')
    room_ids = Room.objects.values('id').order_by('id')
    return render(
        request,
        'index.html', {
            'hello': 'hello',
            'opts': opts,
            'floor_values': floor_values,
            'room_ids': room_ids
        }
    )


def floor_view(request, floor):
    floor_values = Room.objects.values('floor').distinct().order_by('floor')
    room_ids = Room.objects.filter(floor__exact=floor).values('id').order_by('id')

    return render(
        request,
        'index.html', {
            'floor_values': floor_values,
            'room_ids': room_ids
        }
    )


def room_view(request, room):
    floor_values = Room.objects.values('floor').distinct().order_by('floor')
    room = Room.objects.get(id__exact=room)
    room_ids = Room.objects.filter(floor__exact=room.floor).values('id').order_by('id')
    computer_admin = Computer._meta
    printer_admin = Printer._meta
    switch_admin = NetworkSwitch._meta
    laptop_admin = Laptop._meta
    other_admin = RoomHasAdditionalItem._meta

    return render(
        request,
        'room_view.html', {
            'floor_values': floor_values,
            'room_ids': room_ids,
            'room': room,
            'computer_admin': computer_admin,
            'printer_admin': printer_admin,
            'switch_admin': switch_admin,
            'laptop_admin': laptop_admin,
            'other_admin': other_admin
        }
    )
