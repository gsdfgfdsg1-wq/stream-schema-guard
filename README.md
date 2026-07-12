# stream-schema-guard

A dependency-free CI guard for backward compatibility of simplified event JSON Schemas.

## Quick start

```bash
python guard.py schema-before.json schema-after.json
```

The guard permits optional additions but rejects removed fields, changed field types, and newly required fields that can break existing event consumers.

## Test

```bash
python -m unittest discover -v
```

## License

MIT.
