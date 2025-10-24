import sys
from scripts._validation_common import run_standard_validation

if __name__ == "__main__":
    sys.exit(run_standard_validation(
        category="actions",
        data_path="rules/2024/action.json",
        schema_path="schema/2024/v1/rules.action.schema.json",
        array_keys=["action", "actions"]
    ))
