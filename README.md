# generate_broadlink_ir.py

Generate a Broadlink IR code for RME ADI-2 / ADI-2 Pro / ADI-2/4 NEC commands.

## Usage

    python generate_broadlink_ir.py HEX_COMMAND

### Example

    python generate_broadlink_ir.py 2E

## Notes

- Verified on ADI-2 Pro hardware (codes match the original remote bit for bit).
- ADI-2 DAC and ADI-2/4 codes are generated from the RME tables and have not been tested on hardware.

### RME IR command tables (.ods)

IR codes are calculated from RME's own published tables, © Ralf Männel for RME GmbH:

- ADI-2 DAC: https://www.rme-audio.de/downloads/adi2dac_ir_commands.zip
- ADI-2 Pro: https://www.rme-audio.de/downloads/adi2pro_ir_commands.zip
- ADI-2/4 Pro: https://rme-audio.de/downloads/adi24pro_ir_commands.zip

### RME table errors (Fixed by RME in September 2026)
 
Make sure you download the current RME tables from the links above, in previous files three rows used to have a mismatch between the hex column and the binary column.
 
- ADI-2 DAC, Setup 7: hex `30` vs binary `3C`
- ADI-2 DAC, Setup 8: hex `3C` vs binary `3D`
- ADI-2/4, Volume -: hex `61` vs binary `A1`
The values used here (`3C`, `3D`, `61`) match the corrected tables.
