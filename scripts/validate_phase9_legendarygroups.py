import sys
from scripts._validation_common import run_standard_validation

if __name__ == "__main__":
    sys.exit(run_standard_validation(
        category="legendary groups",
        data_path="rules/2024/legendaryGroup.json",
        schema_path="schema/2024/v1/rules.legendarygroup.schema.json",
        array_keys=["legendaryGroup", "legendaryGroups"]
    ))
