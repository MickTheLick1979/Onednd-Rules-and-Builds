import sys
from scripts._validation_common import run_standard_validation

if __name__ == "__main__":
    sys.exit(run_standard_validation(
        category="species",
        data_path="rules/2024/species.json",
        schema_path="schema/2024/v1/species.schema.json",
        array_keys=["species", "race", "races"]
    ))

