# generated by datamodel-codegen:
#   filename:  schema.json
#   timestamp: 2021-05-14T11:16:39+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel, Field


class StacExtensions(BaseModel):
    stac_extensions: List


class Type(BaseModel):
    pass


class TypeSpatial(BaseModel):
    __root__: str


class AxisXy(Enum):
    x = "x"
    y = "y"


class AxisZ(BaseModel):
    __root__: str


class VariableType(Enum):
    data = "data"
    auxiliary = "auxiliary"


class ExtentClosed(BaseModel):
    __root__: List[float] = Field(..., max_items=2, min_items=2)


class ExtentOpen(BaseModel):
    __root__: List[Optional[float]] = Field(..., max_items=2, min_items=2)


class ValuesNumeric(BaseModel):
    __root__: List[float] = Field(..., min_items=1)


class Values(BaseModel):
    __root__: List[Union[float, str]] = Field(..., min_items=1)


class Step(BaseModel):
    __root__: Optional[float]


class Unit(BaseModel):
    __root__: str


class ReferenceSystemSpatial(BaseModel):
    __root__: Union[str, float, Dict[str, Any]]


class Description(BaseModel):
    __root__: str


class AdditionalDimension(BaseModel):
    type: Optional[Type] = None
    description: Optional[Description] = None
    extent: Optional[ExtentOpen] = None
    values: Optional[Values] = None
    step: Optional[Step] = None
    unit: Optional[Unit] = None
    reference_system: Optional[str] = None
    dimensions: Optional[List[str]] = None


class HorizontalSpatialDimension(BaseModel):
    type: TypeSpatial
    axis: AxisXy
    description: Optional[Description] = None
    extent: ExtentClosed
    values: Optional[ValuesNumeric] = None
    step: Optional[Step] = None
    reference_system: Optional[ReferenceSystemSpatial] = None


class VerticalSpatialDimension(BaseModel):
    type: Optional[TypeSpatial] = None
    axis: Optional[AxisZ] = None
    description: Optional[Description] = None
    extent: Optional[ExtentOpen] = None
    values: Optional[Values] = None
    step: Optional[Step] = None
    unit: Optional[Unit] = None
    reference_system: Optional[ReferenceSystemSpatial] = None


class TemporalDimension(BaseModel):
    type: str
    description: Optional[Description] = None
    values: Optional[List[str]] = Field(None, min_items=1)
    extent: List[Optional[str]] = Field(..., max_items=2, min_items=2)
    step: Optional[Optional[str]] = None


class Variable(BaseModel):
    type: Optional[VariableType] = None
    description: Optional[Description] = None
    dimensions: List[str]
    values: Optional[List] = Field(None, min_items=1)
    extent: Optional[List[Optional[Union[str, float]]]] = Field(
        None, max_items=2, min_items=2
    )
    step: Optional[Optional[str]] = None
    unit: Optional[Unit] = None
    shape: Optional[List[Optional[int]]] = None
    chunks: Optional[List[Optional[int]]] = None
    attrs: Optional[dict] = None


class Datacube(BaseModel):
    cube_dimensions: Optional[
        Dict[
            str,
            Union[
                AdditionalDimension,
                HorizontalSpatialDimension,
                VerticalSpatialDimension,
                TemporalDimension,
            ],
        ]
    ] = Field(None, alias="cube:dimensions")
    cube_variables: Optional[Dict[str, Variable]] = Field(None, alias="cube:variables")


class DatacubeExtensionItem(StacExtensions):
    type: Any
    properties: Datacube
    assets: Dict[str, Datacube]


class DatacubeExtensionItem1(StacExtensions, Datacube):
    type: Any
    assets: Optional[Dict[str, Datacube]] = None
    item_assets: Optional[Dict[str, Datacube]] = None


class DatacubeExtension(BaseModel):
    __root__: Union[DatacubeExtensionItem, DatacubeExtensionItem1] = Field(
        ...,
        description="Datacube Extension for STAC Items and STAC Collections.",
        title="Datacube Extension",
    )
