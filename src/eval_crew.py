results = []

for text in tqdm(test_cases):
    res = run_pipeline(text)
    results.append(res)

    print("="*80)
    print("INPUT:", text)
    print("EXTRACTOR:", res["extractor"])
    print("REVIEW:", res["reviewer"])
    print("FALLBACK:", res["fallback"])
    print("FINAL:", res["final"])
  total = len(results)

valid_outputs = sum(
    1 for r in results
    if (
        len(r["final"]["persons"]) +
        len(r["final"]["orgs"]) +
        len(r["final"]["locations"])
    ) > 0
)

fallback_used = sum(1 for r in results if r["status"] == "fallback_used")

reviewer_catches = sum(
    1 for r in results if len(r["reviewer"]["issues"]) > 0
)

print("Valid final output rate:", valid_outputs / total)
print("Fallback activation rate:", fallback_used / total)
print("Reviewer catch rate:", reviewer_catches / total)
