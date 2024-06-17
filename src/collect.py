from datetime import timedelta

import bytewax.operators as op
from bytewax.dataflow import Dataflow
from bytewax.connectors.stdio import StdOutSink
from bytewax.testing import TestingSource


def run() -> Dataflow:
    flow = Dataflow("collect")
    stream = op.input("input", flow, TestingSource(list(range(10))))
    keyed_stream = op.key_on("key", stream, lambda _: "ALL")
    collected_stream = op.collect(
        "collect",
        keyed_stream,
        timeout=timedelta(seconds=10),
        max_size=3,
    )
    op.output("output", collected_stream, StdOutSink())
    return flow
