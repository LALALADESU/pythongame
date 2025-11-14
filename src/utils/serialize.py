from typing import Union, Any
from spi.shape import Point, Line, Rectangle, Circle
from spi.image import Image, Animation
import json


class DataType():  # take it as an Enum
    NONE = "none"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    STRING = "string"
    LIST = "list"
    TUPLE = "tuple"
    SET = "set"
    DICT = "dict"
    
    POINT = "point"
    LINE = "line"
    RECTANGLE = "rectangle"
    CIRCLE = "circle"
    
    IMAGE = "image"
    ANIMATION = "animation"
    
    UNKNOWN = "unknown"
    
    _class_dict: dict[type, "DataType"]
    
    @classmethod
    def get(cls, obj):
        return DataType.NONE if obj is None else cls._class_dict.get(type(obj), DataType.UNKNOWN)

DataType._class_dict = {
    int:        DataType.INT,
    float:      DataType.FLOAT,
    bool:       DataType.BOOL,
    str:        DataType.STRING,
    list:       DataType.LIST,
    tuple:      DataType.TUPLE,
    set:        DataType.SET,
    dict:       DataType.DICT,
    
    Point:      DataType.POINT,
    Line:       DataType.LINE,
    Rectangle:  DataType.RECTANGLE,
    Circle:     DataType.CIRCLE,
    
    Image:      DataType.IMAGE,
    Animation:  DataType.ANIMATION,
}


class Serializer():
    @classmethod
    def serialize(cls, obj): ...
    @classmethod
    def deserialize(cls, data): ...


class JsonDictSerializer(Serializer):
    @classmethod
    def serialize(cls, obj):
        type = DataType.get(obj)
        
        if   type == DataType.NONE: return None
        elif type in [DataType.INT, DataType.FLOAT, DataType.BOOL]: return obj
        elif type == DataType.STRING: return obj
        elif type in [DataType.LIST, DataType.TUPLE, DataType.SET]: return [cls.serialize(x) for x in obj]
        elif type == DataType.DICT: return obj  # how to do ?
        
        elif type == DataType.POINT:     return {"_type": DataType.POINT,     "x": obj.x, "y": obj.y}
        elif type == DataType.LINE:      return {"_type": DataType.LINE,      "x": obj.x, "y": obj.y, "x2": obj.x2, "y2": obj.y2}
        elif type == DataType.RECTANGLE: return {"_type": DataType.RECTANGLE, "x": obj.x, "y": obj.y, "w": obj.w, "h": obj.h}
        elif type == DataType.CIRCLE:    return {"_type": DataType.CIRCLE,    "x": obj.x, "y": obj.y, "r": obj.r}
        
        elif type == DataType.IMAGE: return {
            "_type": DataType.IMAGE,
            "path": obj.path,
            "area": cls.serialize(obj.area),
            "offset": cls.serialize(obj.offset)}
        elif type == DataType.ANIMATION: return {
            "_type": DataType.ANIMATION,
            "images": cls.serialize(obj.images),
            "durations": obj.durations,
            "is_loop": obj.is_loop}
        
    
    @classmethod
    def deserialize(cls, data: Union[None, int, float, bool, str, list, dict]) -> Any:
        type = DataType.get(data)
        
        # data is basic types
        if type in [DataType.NONE, DataType.INT, DataType.FLOAT, DataType.BOOL, DataType.STRING, DataType.LIST, DataType.TUPLE, DataType.SET]:
            return data
        
        # data is a normal dict
        if "_type" not in data:
            return data
        
        # data is an object
        type = data["_type"]
        
        if   type == DataType.POINT: return Point(data["x"], data["y"])
        elif type == DataType.LINE: return Line(data["x"], data["y"], data["x1"], data["y2"])
        elif type == DataType.RECTANGLE: return Rectangle(data["x"], data["y"], data["w"], data["h"])
        elif type == DataType.CIRCLE: return Circle(data["x"], data["y"], data["r"])
        
        elif type == DataType.IMAGE: return Image(
            data["path"],
            cls.deserialize(data["area"]),
            cls.deserialize(data["offset"]))
        elif type == DataType.ANIMATION: return Animation(
            [cls.deserialize(x) for x in data["images"]],
            data["durations"],
            data["is_loop"]
        )


class JsonSerializer(Serializer):
    @classmethod
    def serialize(cls, obj):
        return json.dumps(JsonDictSerializer.serialize(obj))
    
    @classmethod
    def deserialize(cls, data):
        return JsonDictSerializer.deserialize(json.loads(data))