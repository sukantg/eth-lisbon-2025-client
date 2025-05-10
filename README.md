# Market Forcaster

This project provides a Python script to automate calibrated forecasting requests using the `superforcaster` Mech, powered by the [Mech Protocol](https://olas.network/mech), on the Gnosis chain via the [Mech Marketplace](https://mech.olas.network).

---

## Features

- Sends requests to Mechs via `mech-client`
- Supports **on-chain** and **off-chain** delivery modes
- Preconfigured for the `superforcaster` tool
- Runs on the **Gnosis** network
- Fully scriptable interaction for automation or backend integration

---

## Requirements

| Requirement | Version            |
| ----------- | ------------------ |
| Python      | >= 3.10            |
| Poetry      | 1.8.4              |
| mech-client | latest (via `pip`) |

---

## Setup

```bash
pip install mech-client
```

```bash
mechx deposit-token --chain-config gnosis <amount>

```

## Run

```bash
python mech_superforcaster_request.py

```
