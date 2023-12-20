# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import scr_logging
from hypothesis import given, strategies as st

# TODO: replace st.nothing() with an appropriate strategy


@given(name=st.text(), filename=st.nothing())
def test_fuzz_set_logging(name, filename):
    scr_logging.set_logging(name=name, filename=filename)

