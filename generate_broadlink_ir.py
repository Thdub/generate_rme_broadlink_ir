#!/usr/bin/env python3
"""
Generate a Broadlink IR code for RME ADI-2 NEC commands.

Usage:
    python generate_broadlink_ir.py HEX_COMMAND

Example:
    python generate_broadlink_ir.py 2E

The RME documentation specifies the manufacturer ID as 0x1234.
Since NEC transmits each field LSB-first, the value appearing
in the transmitted bit stream is 0x4321.
"""

import sys


# RME manufacturer ID.
#
# Documented value: 0x1234
# Transmitted LSB-first: 0x4321
RME_MANUFACTURER_ID = 0x4321


# Broadlink: one unit ~= 8192 / 269 microseconds
BROADLINK_TICK_US = 8192 / 269


def nec_pulses(address, command):
    """Build raw NEC timings in microseconds."""

    # NEC frame:
    #   address  (16 bits)
    #   command  (8 bits)
    #   ~command (8 bits)
    #
    # Each field is transmitted LSB-first.

    bits = []

    for value, width in (
        (address, 16),
        (command, 8),
        (command ^ 0xFF, 8),
    ):
        for bit in range(width):
            bits.append((value >> bit) & 1)

    # NEC header
    pulses = [
        9000,  # MARK
        4500,  # SPACE
    ]

    # NEC bits
    for bit in bits:
        pulses.append(560)                  # MARK
        pulses.append(1690 if bit else 560) # SPACE

    # Final MARK
    pulses.append(560)

    # End-of-frame silence
    pulses.append(40000)

    return pulses


def broadlink_encode(pulses):
    """
    Convert timings to Broadlink format.

    Format:
        26 00 LL LL ...
    """

    data = bytearray([
        0x26,  # IR
        0x00,  # Repeat count
        0x00, 0x00,  # Data length
    ])

    for pulse_us in pulses:
        units = round(pulse_us / BROADLINK_TICK_US)

        if units < 256:
            data.append(units)
        else:
            # Broadlink extended timing:
            # 00 + 16-bit big-endian value
            data.extend([
                0x00,
                (units >> 8) & 0xFF,
                units & 0xFF,
            ])

    length = len(data) - 4
    data[2] = length & 0xFF
    data[3] = (length >> 8) & 0xFF

    return bytes(data)


def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("  python generate_broadlink_ir.py HEX_COMMAND")
        print()
        print("Example RME VOL Push:")
        print("  python generate_broadlink_ir.py 2E")
        sys.exit(1)

    command = int(sys.argv[1], 16)

    if not 0 <= command <= 0xFF:
        raise ValueError("COMMAND must be an 8-bit value")

    pulses = nec_pulses(RME_MANUFACTURER_ID, command)
    broadlink = broadlink_encode(pulses)

    print(f"Manufacturer : 0x{RME_MANUFACTURER_ID:04X}")
    print(f"Command      : 0x{command:02X}")
    print(f"Command inv  : 0x{command ^ 0xFF:02X}")
    print()
    print("Broadlink:")
    print(broadlink.hex().upper())


if __name__ == "__main__":
    main()