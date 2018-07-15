import dbus

SERVICE_NAME = "org.bluez"
AGENT_IFACE = SERVICE_NAME + '.Agent1'
ADAPTER_IFACE = SERVICE_NAME + ".Adapter1"
DEVICE_IFACE = SERVICE_NAME + ".Device1"
PLAYER_IFACE = SERVICE_NAME + '.MediaPlayer1'
TRANSPORT_IFACE = SERVICE_NAME + '.MediaTransport1'

import dbus

SERVICE_NAME = "org.bluez"
OBJECT_IFACE =  "org.freedesktop.DBus.ObjectManager"
ADAPTER_IFACE = SERVICE_NAME + ".Adapter1"
DEVICE_IFACE = SERVICE_NAME + ".Device1"
PROPERTIES_IFACE = "org.freedesktop.DBus.Properties"
bus = dbus.SystemBus()
manager = dbus.Interface(bus.get_object("org.bluez", "/"), "org.freedesktop.DBus.ObjectManager")

objects = manager.GetManagedObjects()
for path, ifaces in objects.items():
    adapter = ifaces.get(ADAPTER_IFACE)
    if adapter is None:
        continue
    obj = bus.get_object(SERVICE_NAME, path)
    adapterPath = dbus.Interface(obj, ADAPTER_IFACE)

adapter = dbus.Interface(bus.get_object('org.bluez', adapterPath._obj.__dbus_object_path__), 'org.freedesktop.DBus.Adapter')
for devicePath in adapter.ListDevices():
    device = dbus.Interface(bus.get_object('org.bluez', devicePath),'org.bluez.Device')
    deviceProperties = device.GetProperties()
    print(deviceProperties["Address"])