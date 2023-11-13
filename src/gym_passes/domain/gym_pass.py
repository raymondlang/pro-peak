from typing import Any

from dateutil.relativedelta import relativedelta

from src.building_blocks.clock import Clock
from src.gym_passes.domain.date_range import DateRange
from src.gym_passes.domain.errors import GymPassError
from src.gym_passes.domain.gym_pass_id import GymPassId
from src.gym_passes.domain.pause import Pause
from src.gym_passes.domain.status import Status

OwnerId = str
GymPassSnapshot = dict[str, Any]


class GymPass:
    def __init__(
        self,
        gym_pass_id: GymPassId,
        owner_id: OwnerId,
        status: Status,
        period_of_validity: DateRange,
        clock: Clock,
        pauses: list[Pause] | None,
    ) -> None:
        self._gym_pass_id = gym_pass_id
        self._owner_id = owner_id
        self._status = status
        self._period_of_validity = period_of_validity
        self._clock = clock
        self._pauses = pauses if pauses else []

    @property
    def id(self) -> GymPassId:
        return self._gym_pass_id

    @classmethod
    def create_for(
        cls, owner_id: OwnerId, period_of_validity: DateRange, clock: Clock = Clock.system_clock()
    ) -> "GymPass":
        return cls(
            gym_pass_id=GymPassId.new_one(),
            owner_id=owner_id,
            status=Status.activated,
            period_of_validity=period_of_validity,
            clock=clock,
            pauses=None,
        )
