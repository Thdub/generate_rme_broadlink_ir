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

## Notes

### RME IR command tables (.ods)

- ADI-2 DAC: https://www.rme-audio.de/downloads/adi2dac_ir_commands.zip
- ADI-2 Pro: https://www.rme-audio.de/downloads/adi2pro_ir_commands.zip
- ADI-2/4 Pro: https://rme-audio.de/downloads/adi24pro_ir_commands.zip

### Errors in the RME tables

In three rows of the RME tables, the hex column and the binary column do not match:

- **ADI-2 DAC, Setup 7:** hex `30`, binary `3C`. `30` is already the code for B-, so the correct value is `3C`.
- **ADI-2 DAC, Setup 8:** hex `3C`, binary `3D`. The correct value is `3D` (next in sequence).
- **ADI-2/4, Volume -:** hex `61`, binary `A1`. Here the binary column is wrong. The correct value is `61`, which matches the `0x6_` prefix used by the other ADI-2/4 commands.
