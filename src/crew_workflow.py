def run_pipeline(text):

    triage = triager(text)

    ext = extractor(text)

    review = reviewer(text, ext)

    if review["needs_fallback"]:
        fb = fallback(text)
        final = fb
        status = "fallback_used"
    else:
        fb = None
        final = ext
        status = "ok"

    return {
        "input": text,
        "triager": triage,
        "extractor": ext,
        "reviewer": review,
        "fallback": fb,
        "final": final,
        "status": status
    }
