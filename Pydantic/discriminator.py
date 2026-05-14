from typing import Annotated, Literal, Union

from pydantic import BaseModel, Field, TypeAdapter


class ImageCapture(BaseModel):
    source_type: Literal["image"]
    resolution: str
    format: str


class AudioCapture(BaseModel):
    source_type: Literal["audio"]
    bitrate: int
    frequency: int


type AnyCapture = Annotated[
    Union[ImageCapture, AudioCapture], Field(discriminator="source_type")
]

data = {"source_type": "audio", "bitrate": 320, "frequency": 44100}
adapter = TypeAdapter(AnyCapture)
obj = adapter.validate_python(data)
print(type(obj))
