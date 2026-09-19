Generate a Broadlink IR code for RME ADI-2/ADI-2 Pro/ADI-2/4 NEC commands.

Usage:
    python generate_broadlink_ir.py HEX_COMMAND

Example:
    python generate_broadlink_ir.py 2E

The RME documentation specifies the manufacturer ID as 0x1234.
Since NEC transmits each field LSB-first, the value appearing
in the transmitted bit stream is 0x4321.

