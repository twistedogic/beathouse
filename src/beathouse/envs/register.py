import gym

def register(id=None, entry_point=None):
    if id in gym.envs.registry.env_specs:
        del gym.envs.registry.env_specs[id]
    gym.envs.registration.register(id=id, entry_point=entry_point)

