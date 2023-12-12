import tkinter as tk
from __init__ import Config
from PIL import Image, ImageTk, ImageDraw


def create_circle_image(image_path, size):
    original_image = Image.open(image_path)

    # Crop the image to remove excess white space
    bbox = original_image.getbbox()
    original_image = original_image.crop(bbox)

    # Resize the cropped image
    original_image = original_image.resize((size, size), Image.LANCZOS)

    # Create a circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Create a result image with a black background
    result = Image.new("RGBA", (size, size), Config.bg_color)
    result.paste(original_image, mask=mask)

    return ImageTk.PhotoImage(result)


def create_map(frame, image_path, map_size):
    map_fig = Image.open(image_path)
    map_fig = map_fig.resize((map_size, map_size), Image.LANCZOS)
    map_fig = ImageTk.PhotoImage(map_fig)
    map_label = tk.Label(frame, image=map_fig, bg=Config.bg_color)
    map_label.image = map_fig
    map_label.place(x=Config.window_height // 2 - map_size // 2, y=Config.window_width // 2 - map_size // 2 + 100)

    return map_label


def remove_background(input_path, output_path, threshold=200):
    image = Image.open(input_path)

    gray_image = image.convert("L")

    binary_image = gray_image.point(lambda x: 255 if x > threshold else 0, '1')

    result_image = Image.new("RGBA", image.size, (255, 255, 255, 0))
    result_image.paste(image, mask=binary_image)

    result_image.save(output_path)


def center_window(window, width, height):
    # 获取屏幕的宽度和高度
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 计算窗口的左上角坐标，使其居中
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2 - 50

    # 设置窗口的位置
    window.geometry(f"{width}x{height}+{x}+{y}")
