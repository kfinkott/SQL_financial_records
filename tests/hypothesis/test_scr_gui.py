None
# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import scr_gui
from hypothesis import given, strategies as st


@given(
    cls=st.none(),
    init=st.booleans(),
    repr=st.booleans(),
    eq=st.booleans(),
    order=st.booleans(),
    unsafe_hash=st.booleans(),
    frozen=st.booleans(),
    match_args=st.booleans(),
    kw_only=st.booleans(),
    slots=st.booleans(),
)
def test_fuzz_dataclass(
    cls, init, repr, eq, order, unsafe_hash, frozen, match_args, kw_only, slots
):
    scr_gui.dataclass(
        cls,
        init=init,
        repr=repr,
        eq=eq,
        order=order,
        unsafe_hash=unsafe_hash,
        frozen=frozen,
        match_args=match_args,
        kw_only=kw_only,
        slots=slots,
    )

