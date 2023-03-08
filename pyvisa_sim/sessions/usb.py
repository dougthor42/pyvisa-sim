# -*- coding: utf-8 -*-
"""USB simulated session class.

:copyright: 2014-2022 by PyVISA-sim Authors, see AUTHORS for more details.
:license: MIT, see LICENSE for more details.

"""
from pyvisa import constants, rname

from . import session


@session.Session.register(constants.InterfaceType.usb, "INSTR")
class USBInstrumentSession(session.Session):
    parsed: rname.USBInstr

    def after_parsing(self) -> None:
        self.attrs[constants.ResourceAttribute.interface_number] = int(
            self.parsed.board
        )
        self.attrs[
            constants.ResourceAttribute.manufacturer_id
        ] = self.parsed.manufacturer_id
        self.attrs[constants.ResourceAttribute.model_code] = self.parsed.model_code
        self.attrs[
            constants.ResourceAttribute.usb_serial_number
        ] = self.parsed.serial_number
        self.attrs[constants.ResourceAttribute.usb_interface_number] = int(
            self.parsed.board
        )


@session.Session.register(constants.InterfaceType.usb, "RAW")
class USBRawSession(session.Session):

    parsed: rname.USBRaw

    def after_parsing(self) -> None:
        self.attrs[constants.ResourceAttribute.interface_number] = int(
            self.parsed.board
        )
        self.attrs[
            constants.ResourceAttribute.manufacturer_id
        ] = self.parsed.manufacturer_id
        self.attrs[constants.ResourceAttribute.model_code] = self.parsed.model_code
        self.attrs[
            constants.ResourceAttribute.usb_serial_number
        ] = self.parsed.serial_number
        self.attrs[constants.ResourceAttribute.usb_interface_number] = int(
            self.parsed.board
        )
