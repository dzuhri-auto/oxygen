from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)
    API_KEY: str

    MAX_FOOD_LVL: int = 50
    MAX_OXY_LVL: int = 50
    TASK_CODES: list[str] = [
        "okx",
        "tappc_c",
        "tappc_p",
        "oxy-yt",
        "oxy-tg",
        "join_tw",
        "oxy-chat",
        "oxy-chat-en",
        "join_ds",
        "join_guild",
        "acki",
        "vp_pig",
        "vp_qqq",
    ]
    AUTO_CLAIM_COMBO: bool = False
    AUTO_USE_ITEM: bool = False
    RANDOM_PLAY_GAME: list[int] = [2, 5]
    GAME_SCORES: list[int] = [80, 100]
    AUTO_PLAY_GAME: bool = False

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [1, 15]

    USE_PROXY_FROM_FILE: bool = False


settings = Settings()
