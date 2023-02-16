from __future__ import annotations

import attr
import json

from paloma_sdk.core import AccAddress
from paloma_sdk.core.msg import Msg
from paloma_sdk.util.remove_none import remove_none
from .data import parse_msg
from .data import MsgCreateJob as MsgCreateJob_pb, Job as Job_pb, Routing as Routing_pb, Permissions as Permissions_pb, Trigger as Trigger_pb, ScheduleTrigger as ScheduleTrigger_pb
from paloma_sdk.util.json import JSONSerializable

__all__ = [
    "MsgCreateJob",
]

@attr.s
class Job(JSONSerializable):
    type_amino = "scheduler/Job"
    type_url = "/palomachain.paloma.scheduler.Job"
    prototype = Job_pb
    ID: str = attr.ib()
    owner: str = attr.ib()
    routing: dict = attr.ib()
    definition: str = attr.ib()
    payload: str = attr.ib()
    isPayloadModifiable: bool = attr.ib()
    permissions: dict = attr.ib()
    triggers: list = attr.ib()
    address: str = attr.ib()



@attr.s
class MsgCreateJob(Msg):
    """Execute a state-mutating function on a smart contract.

    Args:
        sender: address of sender
        contract: address of contract to execute function on
        msg (dict|str): ExecuteMsg to pass
        coins: coins to be sent, if needed by contract to execute.
            Defaults to empty ``Coins()``
    """

    type_amino = "scheduler/MsgCreateJob"
    """"""
    type_url = "/palomachain.paloma.scheduler.MsgCreateJob"
    """"""
    prototype = MsgCreateJob_pb
    """"""

    creator: AccAddress = attr.ib()
    job: Job = attr.ib()

    def to_amino(self) -> dict:
        return {
            "type": self.type_amino,
            "value": {
                "creator": self.creator,
                "job": remove_none(self.job),
            },
        }

    @classmethod
    def from_data(cls, data: dict) -> MsgCreateJob:
        return cls(
            creator=data["sender"],
            job=parse_msg(data["job"]),
        )

    def to_proto(self) -> MsgCreateJob_pb:
        return MsgCreateJob_pb(
            creator=self.creator,
            job=Job_pb(
                ID=self.job["ID"],
                owner=self.job["owner"],
                routing=Routing_pb(
                    chainType=self.job["routing"]["chainType"],
                    chainReferenceID=self.job["routing"]["chainReferenceID"]
                ),
                definition=self.job["definition"],
                payload=self.job["payload"],
                isPayloadModifiable=self.job["isPayloadModifiable"],
                permissions=Permissions_pb(
                    whitelist=self.job["permissions"]["whitelist"],
                    blacklist=self.job["permissions"]["blacklist"]
                ),
                triggers=[Trigger_pb(
                    trigger=ScheduleTrigger_pb()
                )],
                address=self.job["address"]
            ),
            # bytes(json.dumps(self.job), "utf-8"),
        )

    @classmethod
    def from_proto(cls, proto: MsgCreateJob_pb) -> MsgCreateJob:
        return cls(
            creator=proto.creator,
            job=parse_msg(proto.job),
        )
