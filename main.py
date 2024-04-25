from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from os import environ
from os.path import join
import shutil
import zipfile


appdata = environ.get("appdata")
resource_packs = join(appdata, ".minecraft", "resourcepacks")

print(resource_packs)


def get_texture_pack() -> str:
    global texture_pack_path
    global file_label
    file_path = filedialog.askopenfilename(filetypes=[("Zip files", "*.zip")])
    if file_path:
        texture_pack_path = file_path
        file_label.config(text=texture_pack_path)


def install_texture_pack() -> None:
    if not texture_pack_path:
        messagebox.showerror("Error!", "You haven't selected a texture pack.")
        return
    
    with zipfile.ZipFile(texture_pack_path, 'r') as zip_ref:
        print(zip_ref.namelist())
        for name in zip_ref.namelist():
            if 'assets' in name:
                try:
                    shutil.copy2(texture_pack_path, resource_packs)
                    messagebox.showinfo("Installing complete!","Texturepack successfully installed!")
                    return
                except shutil.SameFileError:
                    messagebox.showerror("Error!", "The texture pack file already exists in the resourcepacks folder. This texture pack is probably already installed.")
                    return
        messagebox.showerror("Error!", "This zip file does not contain an 'assets' folder. It's probably not a minecraft texturepack.")
        return
        


def main() -> None:
    global texture_pack_path
    global file_label
    texture_pack_path = "" 
    root = Tk()
    root.title("Minecraft Texture Pack Installer for Windows by Keremino™")

    file_frame = ttk.Frame(master=root)
    file_label = ttk.Label(master=file_frame, text="Select a texture pack")
    file_button = ttk.Button(master=file_frame, text="Search", command=get_texture_pack)

    install_pack_button: ttk.Button = ttk.Button(master=root, text="Install pack", command=install_texture_pack)

    file_button.pack(side=RIGHT)
    file_label.pack()
    file_frame.pack()
    install_pack_button.pack()
    root.mainloop()

if __name__ == "__main__":
    main()
