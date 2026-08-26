from pathlib import Path
import logging
import shutil


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DATA_FILE = RAW_DATA_DIR / "Visadataset.csv"

SOURCE_FILE = PROJECT_ROOT / "raw" /  "Visadataset.csv"
RAW_DATA_FILE = RAW_DATA_DIR /  "Visadataset.csv"