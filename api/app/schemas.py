# Copyright (C) 2021-2024, Mindee.

# This program is licensed under the Apache License 2.0.
# See LICENSE or go to <https://opensource.org/licenses/Apache-2.0> for full license details.

from typing import Any, Dict, List, Tuple, Union

from pydantic import BaseModel, Field


class KIEIn(BaseModel):
    det_arch: str = Field(default="db_resnet50", examples=["db_resnet50"])
    reco_arch: str = Field(default="crnn_vgg16_bn", examples=["crnn_vgg16_bn"])
    assume_straight_pages: bool = Field(default=True, examples=[True])
    preserve_aspect_ratio: bool = Field(default=True, examples=[True])
    detect_orientation: bool = Field(default=False, examples=[False])
    detect_language: bool = Field(default=False, examples=[False])
    symmetric_pad: bool = Field(default=True, examples=[True])
    straighten_pages: bool = Field(default=False, examples=[False])
    det_bs: int = Field(default=2, examples=[2])
    reco_bs: int = Field(default=128, examples=[128])
    bin_thresh: float = Field(default=0.1, examples=[0.1])
    box_thresh: float = Field(default=0.1, examples=[0.1])


class OCRIn(KIEIn, BaseModel):
    resolve_lines: bool = Field(default=True, examples=[True])
    resolve_blocks: bool = Field(default=True, examples=[True])
    paragraph_break: float = Field(default=0.0035, examples=[0.0035])


class RecognitionIn(BaseModel):
    reco_arch: str = Field(default="crnn_vgg16_bn", examples=["crnn_vgg16_bn"])
    reco_bs: int = Field(default=128, examples=[128])


class DetectionIn(BaseModel):
    det_arch: str = Field(default="db_resnet50", examples=["db_resnet50"])
    assume_straight_pages: bool = Field(default=True, examples=[True])
    preserve_aspect_ratio: bool = Field(default=True, examples=[True])
    symmetric_pad: bool = Field(default=True, examples=[True])
    det_bs: int = Field(default=2, examples=[2])
    bin_thresh: float = Field(default=0.1, examples=[0.1])
    box_thresh: float = Field(default=0.1, examples=[0.1])


class RecognitionOut(BaseModel):
    name: str = Field(..., examples=["example.jpg"])
    value: str = Field(..., examples=["Hello"])
    confidence: float = Field(..., examples=[0.99])


class DetectionOut(BaseModel):
    name: str = Field(..., examples=["example.jpg"])
    geometries: List[List[float]] = Field(..., examples=[[0.0, 0.0, 0.0, 0.0]])


class OCRWord(BaseModel):
    value: str = Field(..., examples=["example"])
    geometry: List[float] = Field(..., examples=[[0.0, 0.0, 0.0, 0.0]])
    confidence: float = Field(..., examples=[0.99])
    crop_orientation: Dict[str, Any] = Field(..., examples=[{"value": 0, "confidence": None}])


class OCRLine(BaseModel):
    geometry: List[float] = Field(..., examples=[[0.0, 0.0, 0.0, 0.0]])
    words: List[OCRWord] = Field(
        ...,
        examples=[
            {
                "value": "example",
                "geometry": [0.0, 0.0, 0.0, 0.0],
                "confidence": 0.99,
                "crop_orientation": {"value": 0, "confidence": None},
            }
        ],
    )


class OCRBlock(BaseModel):
    geometry: List[float] = Field(..., examples=[[0.0, 0.0, 0.0, 0.0]])
    lines: List[OCRLine] = Field(
        ...,
        examples=[
            {
                "geometry": [0.0, 0.0, 0.0, 0.0],
                "words": [
                    {
                        "value": "example",
                        "geometry": [0.0, 0.0, 0.0, 0.0],
                        "confidence": 0.99,
                        "crop_orientation": {"value": 0, "confidence": None},
                    }
                ],
            }
        ],
    )


class OCRPage(BaseModel):
    blocks: List[OCRBlock] = Field(
        ...,
        examples=[
            {
                "geometry": [0.0, 0.0, 0.0, 0.0],
                "lines": [
                    {
                        "geometry": [0.0, 0.0, 0.0, 0.0],
                        "words": [
                            {
                                "value": "example",
                                "geometry": [0.0, 0.0, 0.0, 0.0],
                                "confidence": 0.99,
                                "crop_orientation": {"value": 0, "confidence": None},
                            }
                        ],
                    }
                ],
            }
        ],
    )


class OCROut(BaseModel):
    name: str = Field(..., examples=["example.jpg"])
    orientation: Dict[str, Union[float, None]] = Field(..., examples=[{"value": 0.0, "confidence": 0.99}])
    language: Dict[str, Union[str, float, None]] = Field(..., examples=[{"value": "en", "confidence": 0.99}])
    dimensions: Tuple[int, int] = Field(..., examples=[(100, 100)])
    items: List[OCRPage] = Field(
        ...,
        examples=[
            {
                "geometry": [0.0, 0.0, 0.0, 0.0],
                "lines": [
                    {
                        "geometry": [0.0, 0.0, 0.0, 0.0],
                        "words": [
                            {
                                "value": "example",
                                "geometry": [0.0, 0.0, 0.0, 0.0],
                                "confidence": 0.99,
                                "crop_orientation": {"value": 0, "confidence": None},
                            }
                        ],
                    }
                ],
            }
        ],
    )


class KIEElement(BaseModel):
    class_name: str = Field(..., examples=["example"])
    items: List[Dict[str, Union[str, List[float], float, Dict[str, Any]]]] = Field(
        ...,
        examples=[
            {
                "value": "example",
                "geometry": [0.0, 0.0, 0.0, 0.0],
                "confidence": 0.99,
                "crop_orientation": {"value": 0, "confidence": None},
            }
        ],
    )


class KIEOut(BaseModel):
    name: str = Field(..., examples=["example.jpg"])
    orientation: Dict[str, Union[float, None]] = Field(..., examples=[{"value": 0.0, "confidence": 0.99}])
    language: Dict[str, Union[str, float, None]] = Field(..., examples=[{"value": "en", "confidence": 0.99}])
    dimensions: Tuple[int, int] = Field(..., examples=[(100, 100)])
    predictions: List[KIEElement]
