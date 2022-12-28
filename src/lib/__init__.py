from gym.envs.registration import register

register(
    id='base-env-v0',
    entry_point='lib.envs:BaseEnv',
)
