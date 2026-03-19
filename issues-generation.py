import json


class Issue:
    def __init__(self, package_name, issue_name, file_name, cwe_id, risk, severity):
        self.package_name = package_name
        self.issue_name = issue_name
        self.file_name = file_name
        self.cwe_id = cwe_id
        self.risk = risk
        self.severity = severity


def main():
    output_file_path = "issues.json"
    issues = []

    target_name = "target1"



    for i in range(1,1001):

         issues.append(Issue(
            f"package {target_name} {i}",
            f"Low Issue {i} for {target_name}",
            f"file{i}.java",
            "259",
            "low",
            3
        ))

         issues.append(Issue(
            f"package {target_name} {i}",
            f"Low Issue {i} for {target_name}",
            f"file{i}.java",
            "259",
            "low",
            3
        ))

         issues.append(Issue(
             f"package {target_name} {i}",
            f"Medium Issue {i} for {target_name}",
            f"file{i}.java",
            "259",
            "medium",
            4
        ))


         issues.append(Issue(
            f"package {target_name} {i}",
            f"High  Issue {i} for {target_name}",
            f"file{i}.java",
            "259",
            "high",
            7
        ))

         issues.append(Issue(
            f"package {target_name} {i}",
            f"Critical Issue {i} for {target_name}",
            f"file{i}.java",
            "259",
            "critical",
            10
        ))

         






    # Generate 1000 high severity issues
    # for i in range(1, 1001):
    #     issues.append(Issue(
    #         f"package {i}",
    #         f"High Issue {i}",
    #         f"file{i}.java",
    #         "259",
    #         "high",
    #         7
    #     ))

    # # Generate 1000 critical severity issues
    # for i in range(1, 1001):
    #     issues.append(Issue(
    #         "critical-package",
    #         f"Critical Issue {i}",
    #         f"file{i}.java",
    #         "259",
    #         "critical",
    #         10
    #     ))

    #     issues.append(Issue(
    #         "medium-package",
    #         f"Medium Issue {i}",
    #         f"file{i}.java",
    #         "259",
    #         "medium",
    #         4
    #     ))

    # # Generate 1000 medium severity issues
    # for i in range(1, 1001):
    #     issues.append(Issue(
    #         "medium-package",
    #         f"Medium Issue {i}",
    #         f"file{i}.java",
    #         "259",
    #         "medium",
    #         4
    #     ))

    # # Generate 1000 low severity issues
    # for i in range(1, 1001):
    #     issues.append(Issue(
    #         "low-package",
    #         f"Low Issue {i}",
    #         f"file{i}.java",
    #         "259",
    #         "low",
    #         3
    #     ))

    # # Generate 1000 info severity issues
    # for i in range(1, 1001):
    #     issues.append(Issue(
    #         "info-package",
    #         f"Info Issue {i}",
    #         f"file{i}.java",
    #         "259",
    #         "info",
    #         0
    #     ))

    # Build JSON structure
    root = {
        "meta": {
            "key": ["packageName"],
            "subproduct": "MyCustomScanner"
        },
        "issues": []
    }

    for issue in issues:
        issue_json = {
            "packageName": issue.package_name,
            "subproduct": "MyCustomScanTool",
            "issueName": issue.issue_name,
            "issueDescription": "Lorem ipsum...",
            "fileName": issue.file_name,
            "remediationSteps": "Fix me fast.",
            "risk": issue.risk,
            "severity": issue.severity,
            "status": "open",
            "referenceIdentifiers": [
                {
                    "type": "cwe",
                    "id": issue.cwe_id
                }
            ]
        }
        root["issues"].append(issue_json)

    # Write to file
    try:
        with open(output_file_path, "w") as f:
            json.dump(root, f, indent=2)
        print(f"✅ Scan results written to: {output_file_path}")
    except IOError as e:
        print(f"❌ Failed to write file: {e}")


if __name__ == "__main__":
    main()