# This test code was written by the `hypothesis.extra.ghostwriter` module
# and is provided under the Creative Commons Zero public domain dedication.

import scr_sql_tasks
import typing
from hypothesis import given, strategies as st

# TODO: replace st.nothing() with an appropriate strategy


@given(
    _Column__name_pos=st.none(),
    _Column__type_pos=st.none(),
    name=st.none(),
    type_=st.none(),
    autoincrement=st.just("auto"),
    default=st.none(),
    doc=st.none(),
    key=st.none(),
    index=st.none(),
    unique=st.none(),
    info=st.none(),
    nullable=st.sampled_from(sqlalchemy.sql.schema.SchemaConst),
    onupdate=st.none(),
    primary_key=st.booleans(),
    server_default=st.none(),
    server_onupdate=st.none(),
    quote=st.none(),
    system=st.booleans(),
    comment=st.none(),
    insert_sentinel=st.booleans(),
    _omit_from_statements=st.booleans(),
    _proxies=st.none(),
)
def test_fuzz_Column(
    _Column__name_pos,
    _Column__type_pos,
    name,
    type_,
    autoincrement,
    default,
    doc,
    key,
    index,
    unique,
    info,
    nullable,
    onupdate,
    primary_key,
    server_default,
    server_onupdate,
    quote,
    system,
    comment,
    insert_sentinel,
    _omit_from_statements,
    _proxies,
) -> None:
    scr_sql_tasks.Column(
        _Column__name_pos=_Column__name_pos,
        _Column__type_pos=_Column__type_pos,
        name=name,
        type_=type_,
        autoincrement=autoincrement,
        default=default,
        doc=doc,
        key=key,
        index=index,
        unique=unique,
        info=info,
        nullable=nullable,
        onupdate=onupdate,
        primary_key=primary_key,
        server_default=server_default,
        server_onupdate=server_onupdate,
        quote=quote,
        system=system,
        comment=comment,
        insert_sentinel=insert_sentinel,
        _omit_from_statements=_omit_from_statements,
        _proxies=_proxies,
    )


@given(
    precision=st.one_of(st.none(), st.integers()),
    asdecimal=st.booleans(),
    decimal_return_scale=st.one_of(st.none(), st.integers()),
)
def test_fuzz_Float(
    precision: typing.Optional[int],
    asdecimal: bool,
    decimal_return_scale: typing.Optional[int],
) -> None:
    scr_sql_tasks.Float(
        precision=precision,
        asdecimal=asdecimal,
        decimal_return_scale=decimal_return_scale,
    )


@given(
    schema=st.none(),
    quote_schema=st.none(),
    naming_convention=st.none(),
    info=st.none(),
)
def test_fuzz_MetaData(schema, quote_schema, naming_convention, info) -> None:
    scr_sql_tasks.MetaData(
        schema=schema,
        quote_schema=quote_schema,
        naming_convention=naming_convention,
        info=info,
    )


@given(
    length=st.one_of(st.none(), st.integers()),
    collation=st.one_of(st.none(), st.text()),
)
def test_fuzz_String(
    length: typing.Optional[int], collation: typing.Optional[str]
) -> None:
    scr_sql_tasks.String(length=length, collation=collation)


@given(url=st.nothing())
def test_fuzz_create_engine(url) -> None:
    scr_sql_tasks.create_engine(url=url)


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
) -> None:
    scr_sql_tasks.dataclass(
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

