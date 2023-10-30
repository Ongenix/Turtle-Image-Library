import turtle
from PIL import Image

class turtleImage:
    def __init__(self, turtle_obj):
        self.t = turtle_obj

    def draw_image(self, img_path, x, y):
        original_speed = self.t._speed

        with Image.open(img_path).convert('RGB') as img:
            full_size = img.size
            length = full_size[0]
            height = full_size[1]
            start_x = int((x - length) / 2)
            start_y = int((y + height) / 2)
            turtle.tracer(0, 0)
            turtle.speed(0)

            section_size = 100
            positions = []

            for height_i in range(0, height, section_size):
                for length_i in range(0, length, section_size):
                    new_x = start_x + length_i
                    new_y = start_y - height_i
                    section_end_x = min(length_i + section_size, length)
                    section_end_y = min(height_i + section_size, height)

                    if new_y < y:
                        new_y += section_size
                    if new_y < (height / 2):
                        new_y += section_size

                    for i in range(length_i, section_end_x):
                        for j in range(height_i, section_end_y):
                            rgb_colour = img.getpixel((i, j))

                            if rgb_colour != (0, 0, 0):
                                positions.append((new_x + i - length_i, new_y - j, rgb_colour))
          
            for pos in positions:
                hex_color = '#%02x%02x%02x' % pos[2]
                self.t.pencolor(hex_color)
                self.t.goto(pos[0], pos[1])
                self.t.dot(size=2.5)

            turtle.update()
        self.t.speed(original_speed)
