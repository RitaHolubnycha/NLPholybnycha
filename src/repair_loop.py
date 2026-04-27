def repair(obj):
    fixed = {}

    for k in ["persons","orgs","locations","legal_acts","dates"]:
        v = obj.get(k, [])
        if not isinstance(v, list):
            v = []
        fixed[k] = v

    return fixed
