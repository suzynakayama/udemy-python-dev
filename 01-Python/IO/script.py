from translate import Translator

try:
    with open('text.txt') as my_file:
        text = my_file.read()
        translator = Translator(to_lang='ja')
        translation = translator.translate(text)
        print(text)
        print(translation)
        with open('text-ja.txt', mode='w') as my_file:
            my_file.write(translation)
except:
    print('Something went wrong.')