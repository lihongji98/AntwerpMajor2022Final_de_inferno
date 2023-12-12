import tkinter as tk
from PIL import Image, ImageTk  # 需要安装 Pillow 库

def on_selection_change(*args):
    selected_indices = listbox.curselection()
    selected_images = [images[index] for index in selected_indices]
    print("Selected images:", selected_images)

root = tk.Tk()
root.title("Multiple Images Selection Example")

# 使用 Pillow 打开多张图片
images = [
    Image.open("icons/faze/ropz.png"),
    Image.open("icons/faze/twistzz.png"),
    Image.open("icons/faze/rain.png"),
    # Add more image paths as needed
]

photo_list = [ImageTk.PhotoImage(image) for image in images]

# 创建 Listbox
listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
listbox.pack()

# 将图片添加到 Listbox
for i, photo in enumerate(photo_list):
    listbox.insert(tk.END, f"Image {i+1}")

# 绑定选择变化的事件
listbox.bind("<<ListboxSelect>>", on_selection_change)

root.mainloop()
