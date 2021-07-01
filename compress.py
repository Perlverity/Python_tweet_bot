from PIL import Image, ImageFilter

def compress():

    print('圧縮中...')
    
    # 1
    image = Image.open('illusts/illust_id_1.jpg')

    resize_img = image.resize((2560 , 2048), Image.LANCZOS) 

    resize_img.save("illusts/illust_id_1.jpg")
    image_pillow = Image.open('illusts/illust_id_1.jpg')

    # 2
    image = Image.open('illusts/illust_id_2.jpg')

    resize_img = image.resize((2560 , 2048), Image.LANCZOS) 

    resize_img.save("illusts/illust_id_2.jpg")
    image_pillow = Image.open('illusts/illust_id_2.jpg')

    # 3
    image = Image.open('illusts/illust_id_3.jpg')

    resize_img = image.resize((2560 , 2048), Image.LANCZOS) 

    resize_img.save("illusts/illust_id_3.jpg")
    image_pillow = Image.open('illusts/illust_id_3.jpg')

    print('圧縮完了!')

if __name__ == "__main__":
    compress()