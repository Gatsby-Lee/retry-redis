"""
:author: Gatsby Lee
:since: 2019-08-12
"""
from tenacity import _utils
from tenacity import compat as _compat
from tenacity.wait import wait_base


class wait_exponential_onlyif_exception_type(wait_base):

    def __init__(self, wait_onlyif_exception=Exception,
                 multiplier=1, max=_utils.MAX_WAIT, exp_base=2, min=0):
        self.exception_types = wait_onlyif_exception
        self.multiplier = multiplier
        self.min = min
        self.max = max
        self.exp_base = exp_base

    @_compat.wait_dunder_call_accept_old_params
    def __call__(self, retry_state):

        e = retry_state.outcome.exception()
        if not isinstance(e, self.exception_types):
            return 0

        try:
            exp = self.exp_base ** (retry_state.attempt_number - 1)
            result = self.multiplier * exp
        except OverflowError:
            return self.max
        return max(max(0, self.min), min(result, self.max))
