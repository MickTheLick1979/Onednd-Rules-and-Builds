import sys
from scripts._validation_common import run_standard_validation

if __name__ == "__main__":
    sys.exit(run_standard_validation(
        category="senses",
        data_path="rules/2024/sense.json",
        schema_path="schema/2024/v1/rules.sense.schema.json",
        array_keys=["sense", "senses"]
    ))
