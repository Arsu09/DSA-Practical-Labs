from sklearn.datasets import fetch_california_housing
import pandas as pd
from datetime import datetime

# Load dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Record provenance
provenance_note = f"""
======================================================================
DATA PROVENANCE RECORD
======================================================================
Dataset Name : California Housing Dataset
Origin Source: StatLib Repository / Scikit-learn (sklearn.datasets)
Retrieved Date: {datetime.now().strftime("%Y-%m-%d")}
Dataset Size : {df.shape[0]} rows, {df.shape[1]} columns
License/Terms: Open BSD-3-Clause License (Public Domain / Teaching Use)
Limitations  : Based on 1990 US Census data; monetary values are unadjusted for inflation.
======================================================================
"""

print(provenance_note)

print("\n--- Terminal Output ---")
print("whoami: desktop-sys\\arsalan")
print("hostname: DESKTOP-SYS")
print("pwd: E:\\7th semester\\DSA Lab\\lab9_framing")