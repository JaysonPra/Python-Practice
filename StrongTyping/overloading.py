from typing import Literal, Union, overload


@overload
def fetch_model(name: Literal["xgb"]) -> str: ...


@overload
def fetch_model(name: Literal["bert"]) -> int: ...


def fetch_model(name: str) -> Union[str, int]:
    if name == "xgb":
        return "XGBoost_v1.bin"
    elif name == "bert":
        return 512
    raise ValueError("Unknown Model")


model_path = fetch_model("xgb")
max_len = fetch_model("bert")
