from pathlib import Path
import logging
import pandas as pd
from dataclasses import dataclass

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(module)s: %(message)s"
)
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class DataValidationConfig:
    project_root: Path = Path(__file__).resolve().parents[2]
    train_data_path: Path = project_root / "data" / "raw" / "train.csv"
    status_file: Path = project_root / "data" / "raw" / "validation_status.txt"
    
    # Expected columns and types for Telco Churn dataset
    expected_columns: tuple = (
        'customerID', 'gender', 'SeniorCitizen', 'Partner', 'Dependents',
        'tenure', 'PhoneService', 'MultipleLines', 'InternetService',
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
        'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
        'PaymentMethod', 'MonthlyCharges', 'TotalCharges', 'Churn'
    )


class DataValidation:
    def __init__(self, config: DataValidationConfig = DataValidationConfig()):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True
            data = pd.read_csv(self.config.train_data_path)
            all_cols = list(data.columns)

            for col in all_cols:
                if col not in self.config.expected_columns:
                    validation_status = False
                    logger.warning(f"Unexpected column found: {col}")

            for col in self.config.expected_columns:
                if col not in all_cols:
                    validation_status = False
                    logger.warning(f"Missing expected column: {col}")

            # Write status to file
            self.config.status_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.config.status_file, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            logger.info(f"Data Validation status: {validation_status}")
            return validation_status

        except Exception as e:
            logger.error(f"Error during Data Validation: {str(e)}")
            raise e


if __name__ == "__main__":
    validator = DataValidation()
    validator.validate_all_columns()