from PIL import Image
import numpy as np
import pyfiglet
from colorama import init, Fore

init(autoreset=True)

# ASCII karakter seti
ASCII_CHARS = "@%#*+=-:.1234567890 "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def pixel_to_ascii(pixel):
    r, g, b = pixel
    brightness = (r + g + b) / 3
    ascii_index = int((brightness / 255) * (len(ASCII_CHARS) - 1))
    return ASCII_CHARS[ascii_index]

def image_to_ascii(image_path, new_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Resim açılırken hata oluştu: {e}")
        return
    
    image = resize_image(image, new_width)
    image = image.convert("RGB")
    pixels = np.array(image)
    
    ascii_image = []
    
    for row in pixels:
        ascii_row = "".join([pixel_to_ascii(pixel) for pixel in row])
        ascii_image.append(ascii_row)
    
    return "\n".join(ascii_image)

def print_ascii_image_in_green(ascii_image):
    if ascii_image:
        print(Fore.GREEN + ascii_image)

def text_to_ascii(text, font="slant", width=500, size=1):
    ascii_art = pyfiglet.figlet_format(text, font=font, width=width)
    
    if size > 1:
        ascii_art = enlarge_ascii(ascii_art, size)
    
    return ascii_art

def enlarge_ascii(ascii_art, size):
    enlarged = ""
    for line in ascii_art.split("\n"):
        enlarged_line = "".join([char * size for char in line])
        enlarged += "\n".join([enlarged_line] * size) + "\n"
    return enlarged

def load_shapes_from_file(filename):
    """Dosyadaki şekilleri yükler ve bir sözlükte saklar."""
    shapes = {}
    try:
        with open(filename, 'r') as file:
            content = file.read()
            shape_name = None
            shape_content = []
            for line in content.splitlines():
                if line.endswith(":"):
                    if shape_name:
                        shapes[shape_name] = "\n".join(shape_content)
                    shape_name = line[:-1].strip()  # Başlığı al (":" hariç)
                    shape_content = []
                else:
                    shape_content.append(line)
            if shape_name:
                shapes[shape_name] = "\n".join(shape_content)
    except FileNotFoundError:
        print("Şekil dosyası bulunamadı.")
    return shapes

def print_shape(shape_name, shapes):
    """Verilen şekil adını kullanarak ASCII sanatını yazdırır."""
    shape = shapes.get(shape_name.lower())
    if shape:
        print(Fore.GREEN + shape)  
    else:
        print("Bu şekil bulunamadı. Lütfen geçerli bir şekil girin.")

def get_user_choice():
    print("Yöntem Seçiniz:")
    print("1: Fotoğrafı ASCII Sanatına Dönüştür")
    print("2: Kelimeyi ASCII Sanatına Dönüştür")
    print("3: Şekil ASCII Sanatını Göster")
    
    choice = input("Seçiminizi yapın (1, 2 veya 3): ")
    return choice

def get_font_choice():
    available_fonts = pyfiglet.FigletFont.getFonts()
    
    print("Mevcut ASCII Yazı Tipleri:")
    for i, font in enumerate(available_fonts, 1):
        print(f"{i}. {font}")
    
    while True:
        try:
            choice = int(input(f"\nBir yazı tipi seçin (1-{len(available_fonts)}): "))
            if 1 <= choice <= len(available_fonts):
                return available_fonts[choice - 1]
            else:
                print("Geçersiz seçim, lütfen tekrar deneyin.")
        except ValueError:
            print("Geçersiz seçim, lütfen bir sayı girin.")

if __name__ == "__main__":
    choice = get_user_choice()

    if choice == '1':  # Fotoğrafı ASCII Sanatına dönüştürme
        image_path = input("Lütfen görselin yolunu girin: ")
        new_width = int(input("Görselin genişliğini girin (varsayılan 100): ") or 100)
        ascii_image = image_to_ascii(image_path, new_width)
        print_ascii_image_in_green(ascii_image)

    elif choice == '2':  # Kelimeyi ASCII Sanatına dönüştürme
        text = input("Lütfen bir kelime girin: ")
        selected_font = get_font_choice()  # Yazı tipi seçimi
        size = int(input("Yazı boyutunu seçin (1-10): "))
        ascii_image = text_to_ascii(text, font=selected_font, size=size)
        print_ascii_image_in_green(ascii_image)

    elif choice == '3':  # Şekil ASCII Sanatını dosyadan okuma
        shapes = load_shapes_from_file("nesne.txt")  # Burada dosya adı 'nesne.txt' olarak değiştirildi
        shape_name = input("Hangi şekli görmek istersiniz? (kare, yuvarlak, telefon, kalp, emoji_smile, emoji_love, emoji_wink): ")
        print_shape(shape_name, shapes)

    else:
        print("Geçersiz seçim. Lütfen 1, 2 veya 3'ü girin.")
