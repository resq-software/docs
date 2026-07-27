# @resq-systems/ui/lib/instrument-dial

## Fileoverview

Shared geometry for round-dial instruments (airspeed, altimeter,
vertical-speed, …). Pure functions over a fixed 200×200 user-space box; all
angles are degrees measured clockwise from the top (12 o'clock).

## Interfaces

- [Point](./interfaces/Point)

## Variables

- [INSTRUMENT\_CENTER](./variables/INSTRUMENT_CENTER)
- [INSTRUMENT\_VIEW](./variables/INSTRUMENT_VIEW)

## Functions

- [clamp](./functions/clamp)
- [describeArc](./functions/describeArc)
- [linearTicks](./functions/linearTicks)
- [polar](./functions/polar)
- [toFinite](./functions/toFinite)
- [valueToAngle](./functions/valueToAngle)
