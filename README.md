# Sim→Real Validation: Contact + Thermal Transient

Goal: quantify and reduce sim→real error for a simple transient experiment by (1) defining metrics, (2) sweeping key realism parameters, and (3) selecting best-fit settings with repeatable scripts.

## What this repo demonstrates
- A measurable realism metric (RMSE/MAE/max error)
- Parameter sweep over a realism-sensitive term (contact effectiveness ≈ interface/contact losses)
- Automated comparison plots + metrics outputs in `/results`

## Quickstart
1) Put a measured CSV in `data/measured/` with columns:
- `t_s` (seconds)
- `T_C` (or `y`)

2) Update `configs/sweep_contact.yaml` to point to your file and set assumptions.

3) Run:
```bash
pip install -r requirements.txt
python run.py


## Requirements
- Python 3.10+
- numpy, scipy
- matplotlib
- pyyaml

Install dependencies:
pip install -r requirements.txt
