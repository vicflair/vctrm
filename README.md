# vctrm

A small Flask app with two tennis-booking utilities:

- **Kallang Tennis Centre** — generates targeted ActiveSG booking URLs.
- **Kallang Tennis Hub** — generates Perfect Gym staging/target URLs and a timed-click bookmarklet for any available court.

## Run locally

```bash
python flask_app.py
```

Then open `http://127.0.0.1:5000`.

The Hub bookmarklet stops at the first booking modal. The user manually completes **Next → Add to cart → Book now**. It does not poll the server, make payments, or solve CAPTCHAs.
