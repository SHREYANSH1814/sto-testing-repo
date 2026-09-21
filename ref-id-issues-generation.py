import json
import random


# ==================== CONFIGURATION ====================
ISSUE_COUNT = 50
OCCURRENCES_PER_ISSUE = 20
REF_IDS_PER_OCCURRENCE = 5
SHARED_OCCURRENCES = True  # All issues share same ref-IDs at each occurrence position
DISTRIBUTION = {"cve": 40, "cwe": 20, "ghsa": 20, "snyk": 20}
OUTPUT_FILE = "ref-id-perf-test.json"
TARGET_NAME = "refid-perf-target"
NULL_RATIO = 0.0   # 0.0-1.0: ratio of occurrences with absent referenceIdentifiers
EMPTY_RATIO = 0.0  # 0.0-1.0: ratio of occurrences with empty [] referenceIdentifiers
SEED = 42          # Set to None for random each run
# =======================================================


def generate_cve_ref(index):
    year = random.choice([2019, 2020, 2021, 2022, 2023, 2024, 2025])
    return {"type": "cve", "id": f"{year}-{10000 + index}"}


def generate_cwe_ref(index):
    common_cwes = [79, 89, 94, 119, 200, 250, 259, 276, 287, 311, 352, 400, 502, 611, 798, 918]
    cwe_id = common_cwes[index % len(common_cwes)]
    return {"type": "cwe", "id": str(cwe_id)}


def generate_ghsa_ref(_index):
    def segment():
        chars = "23456789abcdefghjkmnpqrstvwxyz"
        return "".join(random.choices(chars, k=4))
    return {"type": "ghsa", "id": f"{segment()}-{segment()}-{segment()}"}


def generate_snyk_ref(index):
    languages = ["JS", "JAVA", "PYTHON", "GOLANG", "DOTNET", "RUBY"]
    packages = ["LODASH", "LOG4J", "MIXINDEEP", "EXPRESS", "SPRING", "DJANGO", "RAILS", "NUMPY"]
    lang = languages[index % len(languages)]
    pkg = packages[index % len(packages)]
    return {"type": "snyk", "id": f"{lang}-{pkg}-{400000 + index}"}


def generate_xray_ref(index):
    return {"type": "xray", "id": str(100000 + index)}


def generate_rhsa_ref(index):
    year = random.choice([2022, 2023, 2024, 2025])
    return {"type": "rhsa", "id": f"{year}-{1000 + index}"}


REF_ID_GENERATORS = {
    "cve": generate_cve_ref,
    "cwe": generate_cwe_ref,
    "ghsa": generate_ghsa_ref,
    "snyk": generate_snyk_ref,
    "xray": generate_xray_ref,
    "rhsa": generate_rhsa_ref,
}


def distribute_ref_ids(total_count, distribution):
    ref_ids = []
    allocated = 0

    types_list = list(distribution.items())
    for i, (ref_type, percentage) in enumerate(types_list):
        if i == len(types_list) - 1:
            count = total_count - allocated
        else:
            count = round(total_count * percentage / 100)
        allocated += count

        generator = REF_ID_GENERATORS[ref_type]
        for j in range(count):
            ref_ids.append(generator(len(ref_ids) + j))

    random.shuffle(ref_ids)
    return ref_ids


def generate_shared_ref_ids_per_occurrence(occurrences_per_issue, ref_ids_per_occurrence, ref_distribution):
    """
    Pre-generate ref-IDs for each occurrence position.
    Index N = the ref-IDs that ALL issues will use at their Nth occurrence.
    """
    return [
        distribute_ref_ids(ref_ids_per_occurrence, ref_distribution)
        for _ in range(occurrences_per_issue)
    ]


def generate_occurrences(issue_index, occurrences_per_issue, ref_ids_per_occurrence, ref_distribution, shared_ref_ids_map=None):
    occurrences = []
    severities = ["Critical", "High", "Medium", "Low"]

    for occ_idx in range(occurrences_per_issue):
        if shared_ref_ids_map:
            occ_ref_ids = shared_ref_ids_map[occ_idx]
        else:
            occ_ref_ids = distribute_ref_ids(ref_ids_per_occurrence, ref_distribution)

        occurrence = {
            "packageName": f"pkg-issue{issue_index}",
            "issueName": f"Issue {issue_index} Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "issueDescription": f"Occurrence {occ_idx} of issue {issue_index} for ref-ID performance testing",
            "fileName": f"src/module{issue_index}/file{occ_idx}.java",
            "remediationSteps": "Upgrade to latest version.",
            "risk": severities[occ_idx % len(severities)].lower(),
            "severity": [10, 7, 4, 3][occ_idx % 4],
            "status": "open",
            "referenceIdentifiers": occ_ref_ids,
        }
        occurrences.append(occurrence)

    return occurrences


def main():
    if SEED is not None:
        random.seed(SEED)

    # Validate distribution
    total_pct = sum(DISTRIBUTION.values())
    if total_pct != 100:
        print(f"ERROR: Distribution percentages must sum to 100, got {total_pct}")
        return

    for ref_type in DISTRIBUTION:
        if ref_type not in REF_ID_GENERATORS:
            print(f"ERROR: Unknown ref-ID type '{ref_type}'. Available: {list(REF_ID_GENERATORS.keys())}")
            return

    # Pre-generate shared ref-IDs per occurrence position if needed.
    # When enabled, occurrence N of every issue gets the SAME ref-IDs.
    shared_ref_ids_map = None
    if SHARED_OCCURRENCES:
        shared_ref_ids_map = generate_shared_ref_ids_per_occurrence(
            OCCURRENCES_PER_ISSUE, REF_IDS_PER_OCCURRENCE, DISTRIBUTION
        )

    # Build issues
    root = {
        "meta": {
            "key": ["packageName"],
            "subproduct": "RefIdPerfScanner"
        },
        "issues": []
    }

    total_ref_ids_generated = 0
    total_occurrences_generated = 0

    for issue_idx in range(ISSUE_COUNT):
        occurrences = generate_occurrences(
            issue_idx,
            OCCURRENCES_PER_ISSUE,
            REF_IDS_PER_OCCURRENCE,
            DISTRIBUTION,
            shared_ref_ids_map,
        )

        # Apply null/empty ratio to some occurrences
        for occ in occurrences:
            roll = random.random()
            if roll < NULL_RATIO:
                del occ["referenceIdentifiers"]
            elif roll < NULL_RATIO + EMPTY_RATIO:
                occ["referenceIdentifiers"] = []
            else:
                total_ref_ids_generated += len(occ.get("referenceIdentifiers", []))

        root["issues"].extend(occurrences)
        total_occurrences_generated += len(occurrences)

    # Write output
    try:
        with open(OUTPUT_FILE, "w") as f:
            json.dump(root, f, indent=2)
    except IOError as e:
        print(f"Failed to write file: {e}")
        return

    # Print summary
    total_ops = ISSUE_COUNT * OCCURRENCES_PER_ISSUE * REF_IDS_PER_OCCURRENCE
    print(f"Generated: {OUTPUT_FILE}")
    print(f"")
    print(f"  Configuration:")
    print(f"    Issues:              {ISSUE_COUNT}")
    print(f"    Occurrences/Issue:   {OCCURRENCES_PER_ISSUE}")
    print(f"    RefIDs/Occurrence:   {REF_IDS_PER_OCCURRENCE}")
    print(f"    Distribution:        {DISTRIBUTION}")
    print(f"    Shared Occurrences:  {SHARED_OCCURRENCES}")
    print(f"    Null Ratio:          {NULL_RATIO}")
    print(f"    Empty Ratio:         {EMPTY_RATIO}")
    print(f"")
    print(f"  Output Stats:")
    print(f"    Total Issues (JSON): {len(root['issues'])}")
    print(f"    Total RefIDs:        {total_ref_ids_generated}")
    print(f"    Total Occurrences:   {total_occurrences_generated}")
    print(f"")
    print(f"  Performance Estimate (search with pageSize=30):")
    print(f"    Ops per page:        {min(30, ISSUE_COUNT) * OCCURRENCES_PER_ISSUE * REF_IDS_PER_OCCURRENCE}")
    print(f"    Ops max page (100):  {min(100, ISSUE_COUNT) * OCCURRENCES_PER_ISSUE * REF_IDS_PER_OCCURRENCE}")
    print(f"")
    if total_ops > 150000:
        print(f"  WARNING: Total ops ({total_ops}) exceeds timeout threshold (~150,000).")
        print(f"           Expected DB timeout at 15s read deadline.")
    elif total_ops > 50000:
        print(f"  CAUTION: Total ops ({total_ops}) in warning zone (50k-150k).")
        print(f"           May be slow (3-10s) under load.")
    else:
        print(f"  OK: Total ops ({total_ops}) within safe limits (<50k).")


if __name__ == "__main__":
    main()