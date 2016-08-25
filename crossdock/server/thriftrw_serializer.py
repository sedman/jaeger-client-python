def trace_response_to_thriftrw(service, tr):
    return service.TraceResponse(span=tr.span,
                                 downstream=tr.downstream,
                                 notImplementedError=tr.notImplementedError)


def downstream_to_thriftrw(service, downstream):
    if downstream is None:
        return None
    return service.Downstream(downstream.serviceName,
                              downstream.serverRole,
                              downstream.host,
                              downstream.port,
                              downstream.transport,
                              downstream.downstream)


def join_trace_request_to_thriftrw(service, jtr):
    return service.JoinTraceRequest(jtr.serverRole, downstream_to_thriftrw(service, jtr.downstream))


def observed_span_to_thriftrw(service, observed_span):
    return service.ObservedSpan(traceId=observed_span.traceId,
                                sampled=observed_span.sampled,
                                baggage=observed_span.baggage)
