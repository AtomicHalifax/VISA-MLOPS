from pathlib import Path
import logging
import shutil

# Adjust .parents[N] based on script depth relative to the project root:
# - If script is in 'src/ingest_data.py', use .parents[1]
# - If script is in 'src/pipelines/ingest_data.py', use .parents[2]
PROJECT_ROOT = Path(__file__).resolve().parents[1]

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
SOURCE_FILE = PROJECT_ROOT / "source_data" / "telco_churn.csv"
RAW_DATA_FILE = RAW_DATA_DIR / "telco_churn.csv"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def ingest_data():
    logger.info("Starting data ingestion")

    if not SOURCE_FILE.exists():
        raise FileNotFoundError(
            f"Source dataset not found: {SOURCE_FILE}"
        )

    # Ensure raw data directory exists
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Copy raw file to destination directory
    shutil.copy2(SOURCE_FILE, RAW_DATA_FILE)

    logger.info(f"Raw dataset stored at: {RAW_DATA_FILE}")


if __name__ == "__main__":
    ingest_data()