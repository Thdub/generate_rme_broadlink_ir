# generate_broadlink_ir.py

Generate a Broadlink IR code for RME ADI-2 / ADI-2 Pro / ADI-2/4 NEC commands.

## Usage

```
python generate_broadlink_ir.py HEX_COMMAND
```

### Example

```
python generate_broadlink_ir.py 2E
```

RME documentation and IR tables are available at https://rme-audio.de

## Note
RME documents the address as "1234": bytes 0x12 then 0x34, in transmit order.
nec_pulses() sends the 16-bit value low byte first, so the constant is stored byte-swapped: 0x3412.
