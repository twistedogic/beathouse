from .envs.register import register
from .envs.sic_bo.sic_bo_env import SicBoEnv

register(id="sic_bo-v0", entry_point=SicBoEnv)
