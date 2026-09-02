from pathlib import Path
import logging
import pandas as pd
from dataclasses import dataclass

# Setup Logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(module)s: %(message)s"
)
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DataIngestionConfig:
    """Configuration for data paths and ingestion parameters."""
    project_root: Path = Path(__file__).resolve().parents[2] # Adjust depth if file is in src/components/
    raw_data_dir: Path = project_root / "data" / "raw"
    source_file: Path = project_root / "source_data" / "telco_churn.csv"
    raw_data_path: Path = raw_data_dir / "raw_telco_churn.csv"
    train_data_path: Path = raw_data_dir / "train.csv"
    test_data_path: Path = raw_data_dir / "test.csv"
    test_size: float = 0.2
    random_state: int = 42


class DataIngestion:
    """Handles data ingestion, validation, and preliminary train/test splitting."""
    
    def __init__(self, config: DataIngestionConfig = DataIngestionConfig()):
        self.config = config

    def initiate_data_ingestion(self) -> tuple[Path, Path]:
        logger.info("Starting Data Ingestion Pipeline...")
        
        try:
            # 1. Check if source file exists
            if not self.config.source_file.exists():
                raise FileNotFoundError(f"Source file not found at: {self.config.source_file}")

            # 2. Read raw data
            logger.info(f"Reading dataset from {self.config.source_file}")
            df = pd.read_csv(self.config.source_file)

            # 3. Basic schema sanity check
            if df.empty:
                raise ValueError("Ingested dataset is empty.")
            
            # 4. Create directories if missing
            self.config.raw_data_dir.mkdir(parents=True, exist_ok=True)

            # 5. Save raw local copy
            df.to_csv(self.config.raw_data_path, index=False)
            logger.info(f"Raw data successfully backed up to {self.config.raw_data_path}")

            # 6. Perform preliminary Train/Test Split (Standard MLOps step)
            from sklearn.model_selection import train_test_split
            logger.info("Splitting dataset into train and test sets...")
            train_set, test_set = train_test_split(
                df, 
                test_size=self.config.test_size, 
                random_state=self.config.random_state
            )

            # 7. Save train & test split datasets
            train_set.to_csv(self.config.train_data_path, index=False)
            test_set.to_csv(self.config.test_data_path, index=False)
            logger.info(f"Train data saved at: {self.config.train_data_path}")
            logger.info(f"Test data saved at: {self.config.test_data_path}")

            logger.info("Data Ingestion Pipeline completed successfully.")
            return self.config.train_data_path, self.config.test_data_path

        except Exception as e:
            logger.error(f"Error during Data Ingestion: {str(e)}")
            raise e


if __name__ == "__main__":
    ingestion = DataIngestion()
    ingestion.initiate_data_ingestion()