import pygame
from .shape import Point


class KeyCode():
    # arrow keys
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT
    
    # main keyboard number
    KB_1 = pygame.K_1
    KB_2 = pygame.K_2
    KB_3 = pygame.K_3
    KB_4 = pygame.K_4
    KB_5 = pygame.K_5
    KB_6 = pygame.K_6
    KB_7 = pygame.K_7
    KB_8 = pygame.K_8
    KB_9 = pygame.K_9
    
    # alphabets
    A = pygame.K_a
    B = pygame.K_b
    C = pygame.K_c
    D = pygame.K_d
    E = pygame.K_e
    F = pygame.K_f
    G = pygame.K_g
    H = pygame.K_h
    I = pygame.K_i
    J = pygame.K_j
    K = pygame.K_k
    L = pygame.K_l
    M = pygame.K_m
    N = pygame.K_n
    O = pygame.K_o
    P = pygame.K_p
    Q = pygame.K_q
    R = pygame.K_r
    S = pygame.K_s
    T = pygame.K_t
    U = pygame.K_u
    V = pygame.K_v
    W = pygame.K_w
    X = pygame.K_x
    Y = pygame.K_y
    Z = pygame.K_z
    
    # F keys
    F1 = pygame.K_F1
    F2 = pygame.K_F2
    F3 = pygame.K_F3
    F4 = pygame.K_F4
    F5 = pygame.K_F5
    F6 = pygame.K_F6
    F7 = pygame.K_F7
    F8 = pygame.K_F8
    F9 = pygame.K_F9
    F10 = pygame.K_F10
    F11 = pygame.K_F11
    F12 = pygame.K_F12
    
    # other keys on main keyboard
    ESCAPE = pygame.K_ESCAPE
    INSERT = pygame.K_INSERT
    PRINTSCREEN = pygame.K_PRINTSCREEN
    DELETE = pygame.K_DELETE
    HOME = pygame.K_HOME
    END = pygame.K_END
    PAGEUP = pygame.K_PAGEUP
    PAGEDOWN = pygame.K_PAGEDOWN
    BACKQUOTE = pygame.K_BACKQUOTE
    MINUS = pygame.K_MINUS
    EQUALS = pygame.K_EQUALS
    BACKSPACE = pygame.K_BACKSPACE
    TAB = pygame.K_TAB
    LEFTBRACKET = pygame.K_LEFTBRACKET
    RIGHTBRACKET = pygame.K_RIGHTBRACKET
    BACKSLASH = pygame.K_BACKSLASH
    CAPSLOCK = pygame.K_CAPSLOCK
    SEMICOLON = pygame.K_SEMICOLON
    QUOTE = pygame.K_QUOTE
    ENTER = pygame.K_RETURN
    LSHIFT = pygame.K_LSHIFT
    COMMA = pygame.K_COMMA
    PERIOD = pygame.K_PERIOD
    SLASH = pygame.K_SLASH
    RSHIFT = pygame.K_RSHIFT
    LCTRL = pygame.K_LCTRL
    LALT = pygame.K_LALT
    SPACE = pygame.K_SPACE
    RALT = pygame.K_RALT
    RCTRL = pygame.K_RCTRL
    
    # small keypad number
    KP_0 = pygame.K_KP0
    KP_1 = pygame.K_KP1
    KP_2 = pygame.K_KP2
    KP_3 = pygame.K_KP3
    KP_4 = pygame.K_KP4
    KP_5 = pygame.K_KP5
    KP_6 = pygame.K_KP6
    KP_7 = pygame.K_KP7
    KP_8 = pygame.K_KP8
    KP_9 = pygame.K_KP9
    
    # other keypad keys
    NUMLOCK = pygame.K_NUMLOCK
    KP_DIVIDE = pygame.K_KP_DIVIDE
    KP_MULTIPLY = pygame.K_KP_MULTIPLY
    KP_MINUS = pygame.K_KP_MINUS
    KP_PLUS = pygame.K_KP_PLUS
    KP_PERIOD = pygame.K_KP_PERIOD
    KP_ENTER = pygame.K_KP_ENTER
    
    # mouse button
    LEFT_CLICK = -1
    MIDDLE_CLICK = -2
    RIGHT_CLICK = -3
    
    _keycode_list: list[int]
    _keyname_list: list[str]
    _keyname_to_keycode_dict: dict[str, int]
    _keycode_to_keyname_dict: dict[int, str]
    
    @classmethod
    def get_all_keycode(cls):
        return cls._keycode_list
    
    @classmethod
    def get_all_keyname(cls):
        return cls._keyname_list
    
    @classmethod
    def get_keyname(cls, keycode: int):
        return cls._keycode_to_keyname_dict[keycode]
    
    @classmethod
    def get_keycode(cls, keyname: str):
        try: return cls._keyname_to_keycode_dict[keyname]
        except KeyError: return None

KeyCode._keyname_to_keycode_dict = {k: v for k, v in KeyCode.__dict__.items() if not k.startswith("_")}
KeyCode._keycode_to_keyname_dict = {v: k for k, v in KeyCode._keyname_to_keycode_dict.items()}
KeyCode._keyname_list = list(KeyCode._keyname_to_keycode_dict.keys())
KeyCode._keycode_list = list(KeyCode._keycode_to_keyname_dict.keys())


class Keyboard():
    def __init__(self):
        self.downing_keys: list[int] = [] # is the key being pressing down at the moment
        self.upping_keys: list[int] = []
        self.holding_keys: list[int] = []
        
    def is_key_downing(self, keycode: int):
        return keycode in self.downing_keys
    
    def is_key_upping(self, keycode: int):
        return keycode in self.upping_keys
    
    def is_key_holding(self, keycode: int):
        return keycode in self.holding_keys


class Mouse():
    def __init__(self):
        self.downing_keys = [False, False, False]
        self.upping_keys = [False, False, False]
        self.holding_keys = [False, False, False]
        self.wheel_motion: int = 0  # >0: wheelup, 0: no motion, <0: wheel down
    
    def get_position(self):
        pos = pygame.mouse.get_pos()
        return Point(pos[0], pos[1])
    
    def is_key_downing(self, keycode: int):
        return self.downing_keys[keycode]
    
    def is_key_upping(self, keycode: int):
        return self.upping_keys[keycode]
    
    def is_key_holding(self, keycode: int):
        return self.holding_keys[keycode]
    
    def get_wheel_motion(self):
        return self.wheel_motion


class Input():
    
    _is_quit = False # Quit the game?
    _keyboard = Keyboard()
    _mouse = Mouse()
    
    @classmethod
    def update(cls):
        
        cls._keyboard.downing_keys = []
        cls._keyboard.upping_keys = []
        
        cls._mouse.downing_keys = [False, False, False]
        cls._mouse.upping_keys = [False, False, False]
        cls._mouse.wheel_motion = 0
        
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                cls._is_quit = True
            elif e.type == pygame.KEYDOWN:
                cls._keyboard.downing_keys.append(e.dict["key"])
                cls._keyboard.holding_keys.append(e.dict["key"])
            elif e.type == pygame.KEYUP:
                cls._keyboard.upping_keys.append(e.dict["key"])
                cls._keyboard.holding_keys.remove(e.dict["key"])
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if 0 <= (button := e.dict["button"] - 1) <= 2:
                    cls._mouse.downing_keys[button] = True
                    cls._mouse.holding_keys[button] = True
            elif e.type == pygame.MOUSEBUTTONUP:
                if 0 <= (button := e.dict["button"] - 1) <= 2:
                    cls._mouse.upping_keys[button] = True
                    cls._mouse.holding_keys[button] = False
            elif e.type == pygame.MOUSEWHEEL:
                cls._mouse.wheel_motion = e.dict["y"]
    
    @classmethod   
    def keyboard(cls):
        return cls._keyboard
    
    @classmethod
    def mouse(cls):
        return cls._mouse
    
    @classmethod
    def is_quit(cls):
        return cls._is_quit