from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

# print(img)
# img.show()

filtered_img = img.filter(ImageFilter.BLUR)

filtered_img.save("blur.png", 'png')        # convert to png because jpg doesn't support the filters

converted_img = img.convert('L')            # convert to grey scale

converted_img.save("converted.png", 'png')

crooked = converted_img.rotate(90)

crooked.save("crooked.png", 'png')

resized = converted_img.resize((300, 300))

resized.save("resized.png", 'png')

box = (100, 100, 400, 400)
cropped = filtered_img.crop(box)

cropped.save("cropped.png", 'png')

# astro exercise

img1 = Image.open('./astro.jpg')
img1.thumbnail((400, 400))                  # keeps the image ratio
img1.save('astro_resized.png', 'png')
