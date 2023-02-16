import json
import betterproto
from typing import Union, List
from dataclasses import dataclass
from paloma_sdk.core import AccAddress


@dataclass(eq=False, repr=False)
class ScheduleTrigger(betterproto.Message):
    """
    """


@dataclass(eq=False, repr=False)
class EventTrigger(betterproto.Message):
    """
    """


@dataclass(eq=False, repr=False)
class Trigger(betterproto.Message):
    """
    """
    trigger: ScheduleTrigger = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Runner(betterproto.Message):
    """
    """
    chainType: str = betterproto.string_field(1)
    chainReferenceID: str = betterproto.string_field(2)
    address: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class Permissions(betterproto.Message):
    """
    """
    whitelist: List[Runner] = betterproto.message_field(1)
    blacklist: List[Runner] = betterproto.message_field(2)

@dataclass(eq=False, repr=False)
class Routing(betterproto.Message):
    """
    """
    chainType: str = betterproto.string_field(1)
    chainReferenceID: str = betterproto.string_field(2)

@dataclass(eq=False, repr=False)
class Job(betterproto.Message):
    """
    """
    ID: str = betterproto.string_field(1)
    owner: str = betterproto.string_field(2)
    routing: Routing = betterproto.message_field(3)
    definition: str = betterproto.string_field(5)
    payload: str = betterproto.string_field(6)
    isPayloadModifiable: bool = betterproto.bool_field(7)
    permissions: Permissions = betterproto.message_field(8)
    triggers: bytes = betterproto.message_field(9)
    address: str = betterproto.string_field(10)


@dataclass(eq=False, repr=False)
class MsgCreateJob(betterproto.Message):
    """
    MsgExecuteContract submits the given message data to a smart contract
    """

    # Job creator
    creator: str = betterproto.string_field(1)
    # Job json
    job: Job = betterproto.message_field(2)
    # Msg json encoded message to be passed to the contract

def parse_msg(msg: Union[dict, str, bytes]) -> dict:
    if type(msg) is dict:
        return msg
    return json.loads(msg)