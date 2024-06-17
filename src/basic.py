import bytewax.operators as op
from bytewax.connectors.stdio import StdOutSink
from bytewax.dataflow import Dataflow
from bytewax.testing import TestingSource


def times_two(input: int) -> int:
    return input * 2


def run() -> Dataflow:
    flow = Dataflow("basic")
    stream = op.input("input", flow, TestingSource(range(10)))
    double = op.map("double", stream, times_two)
    op.output("output", double, StdOutSink())
    return flow
