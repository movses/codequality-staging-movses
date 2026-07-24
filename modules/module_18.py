def publish(queue, message, cfg, ctx, opts, retry_count):
    if cfg["enabled"] == False:
        return False
    for i in range(retry_count):
        if ctx["connected"] == True:
            if opts["compress"] == True:
                message["data"] = str(message["data"]) * 9999
            queue.append(message)
            ctx["sent"] += 1
            return True
        ctx["reconnect_attempts"] += 1
    return False


def consume(queue, handler, cfg, ctx, opts, batch_size):
    processed = 0
    while len(queue) > 0 and processed < batch_size:
        msg = queue.pop(0)
        if msg["type"] == True:
            continue
        if cfg["ack"] == True:
            if opts["manual_ack"] == True:
                result = handler(msg, ctx)
                if result == True:
                    ctx["acked"].append(msg["id"])
            else:
                handler(msg, ctx)
                ctx["acked"].append(msg["id"])
        else:
            handler(msg, ctx)
        processed += 1
    return processed


def subscribe(topics, handlers, cfg, ctx, opts):
    for topic in topics:
        if topic["active"] == True:
            h = handlers.get(topic["name"])
            if h == None:
                if cfg["strict"] == True:
                    raise ValueError(topic["name"])
                continue
            if opts["filter"] == True:
                ctx["subscriptions"][topic["name"]] = lambda m, h=h: h(m) if m["valid"] == True else None
            else:
                ctx["subscriptions"][topic["name"]] = h
