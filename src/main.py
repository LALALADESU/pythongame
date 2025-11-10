from spi.image import Image
from spi.text import Text, Font
from spi.window import Window
from spi.shape import Point
from spi.control import Input, KeyCode
from spi.clock import Clock


if __name__ == "__main__":
    window = Window(Point(640, 480))
    image = Image("./assets/test.webp")
    
    font = Font("./assets/fonts/unifont-17.0.03.otf")
    text_hello = Text("Hello 你好", font, 32)
    text_keyboard = Text("", font)
    text_mouse = Text("", font)
    text_fps = Text("", font)
    input = Input()
    clock = Clock()
    
    while True:
        clock.tick(60)
        
        input.update()
        
        if input.is_quit():
            break
        
        text_keyboard_text = "keys: "
        for keycode in KeyCode.get_all_keycode():
            if input.keyboard().is_key_holding(keycode):
                text_keyboard_text += KeyCode.get_keyname(keycode) + ","

        text_keyboard.set_text(text_keyboard_text)
        text_mouse.set_text(f"{input.mouse().get_position()}, {input._mouse.holding_keys}, {input._mouse.wheel_motion}")
        text_fps.set_text(f"fps: {clock.get_fps()}")
        
        window.clear()
        window.blit(image, Point(100, 100))
        window.blit(text_hello, Point(10, 10))
        window.blit(text_keyboard, Point(10, 42))
        window.blit(text_mouse, Point(10, 58))
        window.blit(text_fps, Point(10, 74))
        window.update()
