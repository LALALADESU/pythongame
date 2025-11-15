from spi.image import Image, Animation
from spi.text import Text, Font
from spi.window import Window
from spi.shape import Point, Rectangle
from spi.control import Input, KeyCode
from spi.time import Time
from utils.serialize import JsonSerializer, DataType
import json


if __name__ == "__main__":
    image: Image = JsonSerializer.deserialize('{"_type": "image", "path": "./assets/test.webp", "area": null, "offset": null}')
    
    anim_data = '{"_type": "animation", "images": [{"_type": "image", "path": "./assets/anim_test.png", "area": {"_type": "rectangle", "x": 0, "y": 0, "w": 50, "h": 50}, "offset": null}, {"_type": "image", "path": "./assets/anim_test.png", "area": {"_type": "rectangle", "x": 50, "y": 0, "w": 50, "h": 50}, "offset": null}, {"_type": "image", "path": "./assets/anim_test.png", "area": {"_type": "rectangle", "x": 100, "y": 0, "w": 50, "h": 50}, "offset": null}, {"_type": "image", "path": "./assets/anim_test.png", "area": {"_type": "rectangle", "x": 150, "y": 0, "w": 50, "h": 50}, "offset": null}, {"_type": "image", "path": "./assets/anim_test.png", "area": {"_type": "rectangle", "x": 200, "y": 0, "w": 50, "h": 50}, "offset": null}], "durations": [0.5, 0.5, 1, 1, 1], "is_loop": true}'
    animation: Animation = JsonSerializer.deserialize(anim_data)
    animation.start()
    
    font = Font("./assets/fonts/unifont-17.0.03.otf")
    text_hello = Text("Hello 你好", font, 32)
    text_keyboard = Text("", font)
    text_mouse = Text("", font)
    text_fps = Text("", font)
    
    while True:
        Time.tick(60)
        
        Input.update()
        animation.update()
        
        if Input.is_quit():
            break
        
        text_keyboard_text = "keys: "
        for keycode in KeyCode.get_all_keycode():
            if Input.keyboard().is_key_holding(keycode):
                text_keyboard_text += KeyCode.get_keyname(keycode) + ","

        text_keyboard.set_text(text_keyboard_text)
        text_mouse.set_text(f"{Input.mouse().get_position()}, {Input._mouse.holding_keys}, {Input._mouse.wheel_motion}")
        text_fps.set_text(f"fps: {round(Time.get_average_fps())}, timedelta: {Time.get_timedelta()}")
        
        Window.clear()
        Window.blit(image, Point(100, 100))
        Window.blit(text_hello, Point(10, 10))
        Window.blit(text_keyboard, Point(10, 42))
        Window.blit(text_mouse, Point(10, 58))
        Window.blit(text_fps, Point(10, 74))
        Window.blit(animation, Point(200, 400))
        Window.update()
