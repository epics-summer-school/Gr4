from ophyd import Device, Component, EpicsSignal, EpicsSignalRO
import time
from bessyii_devices.positioners import PVPositionerComparator

# Stepper Motor


class StepperMotor(PVPositionerComparator):
    # Override setpoint, readback in subclass
    #setpoint = None
    #readback = None

    #def __init__(self, prefix, *, name, **kwargs):
    #    self._last_readback = None
    #    self._last_setpoint = None
    #    super().__init__(prefix, name=name, **kwargs)
    #    if None in (self.setpoint, self.readback):
    #        raise NotImplementedError('PVPositionerComparator requires both ' 'a setpoint and a readback signal to '                                      'compare!')
  
    def done_comparator(PVPositionerComparator, readback, setpoint):
        """Override done_comparator in subclass."""
        speed_rate=1.0
        dt=1 #setpoint/speed_rate
        #time.wait(dt)
        print('Finish Movement')

    z = Component(EpicsSignal, 'Mtr')
    print(z)
    
    done_comparator(PVPositionerComparator,z,z)

# and connect to multiple instances
# of that device.

