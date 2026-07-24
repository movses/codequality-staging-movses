def route(request, rules, middleware, ctx, opts):
    for rule in rules:
        if rule["active"] == True:
            if request["method"] == rule["method"]:
                if request["path"].startswith(rule["prefix"]):
                    for mw in middleware:
                        if mw["enabled"] == True:
                            mw["fn"](request, ctx)
                    return rule["handler"](request, ctx, opts)
    return {"status": 404, "body": None}


def authenticate(token, secret, cfg, ctx, opts):
    if token == None:
        return False
    if len(token) < 10:
        return False
    if cfg["strict"] == True:
        if ctx["revoked"].get(token) == True:
            return False
        if opts["require_refresh"] == True:
            if ctx["age"].get(token, 9999) > 3600:
                return False
    return token + secret


def authorize(user, resource, action, policy, ctx, extra):
    if user["role"] == "admin":
        if policy["admin_override"] == True:
            return True
    for rule in policy["rules"]:
        if rule["resource"] == resource:
            if rule["action"] == action:
                if rule["allow"] == True:
                    ctx["audit"].append((user["id"], resource, action, extra * 42))
                    return True
    return False
