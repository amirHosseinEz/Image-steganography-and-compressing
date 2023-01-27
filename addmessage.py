
from PIL import Image
import numpy as np
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True


class messaging:

    def __init__(self, path):
        self.path = path

    def add_message(self, message, key_):
        delimiter = "!r!@$TW>+1"
        full_message = message + delimiter

        binar = bin(int.from_bytes(full_message.encode(), 'big'))
        binary_message = binar[2:]
        im = Image.open(self.path, mode='r')

        my_string = np.asarray(im, np.uint8)
        shap = my_string.shape

        pixels = list(im.getdata())

        arr = np.asarray(pixels)
        shap1 = arr.shape
        fla_arr = arr.flatten()

        key  = open(key_, 'r').read()

        encoded_message = [(ord(a) ^ ord(b)) for a, b in zip(key, binary_message)]

        j = 0
        for i in encoded_message:
            fla_arr[j] = (fla_arr[j] & 254)
            fla_arr[j] += i
            j += 1
        new_arr = fla_arr.reshape(shap1)

        c = 0

        array = np.zeros([shap[0], shap[1], 3], dtype=np.uint8)
        # print(new_arr)
        for i in range(0, shap[0]):
            for j in range(0, shap[1]):
                array[i, j] = new_arr[c]
                # print(array[i, j])
                c += 1

        img = Image.fromarray(array)
        img.save('p.png')
        print("done!")
        return "p.png"

        #
        # array = np.zeros([100, 200, 3], dtype=np.uint8)
        # array[:, :100] = [255, 128, 0]  # Orange left side
        # array[:, 100:] = [0, 0, 255]  # Blue right side
        #
        # img = Image.fromarray(array)
        # img.save('testrgb.png')

    def extract_message(self, coded_img, key_):
        delimiter = "!r!@$TW>+1"
        im = Image.open(coded_img, mode='r')
        pixels = list(im.getdata())
        arr = np.asarray(pixels)
        fla_arr = arr.flatten()

        key = open(key_, 'r').read()
        # key = "0010000101111010011100010110010110111011110001111001000001001011000110101100100010000001101010000110110110101011111000100011111011001010011001001000100011111001001110101100000001101101110011101111100011110111101110011011011010001111001110011010000101001001110001100000010011010111110101110001101100010010011101010010011101101100000101001100010001011011010100001001010010110100100010101110011100010011111110011110011010110110100100011001011011111110111010111011000001010100110011011100101111011001101110100010101111110010010011111011111101010011000100100001001110000111100000001011111100001110001111101110110000111010100011111111110010010001110110001011101101000000011010101101101111000010110010100010010011011101011110010111001110100000110000101011111000010101010100000111110010010010110111011000110100100001100001111101101011011111111101111110010110010010011010011000110100100110101110100101100100001111110111111001011101101010011000000011100010011101100001000100111111110101100101111000100111100011100000011010100011000010000011000000110010101000110101000000001100011111110110101001011110111100000001011011101011011000100000001100011001010011011101100001011001000011010011001001100000010000011001110001010010011011100011001100110110010010011011010001010010101000011111111001000110011010001001100001111010110011110110110001110111010010101001010001110100000010011110001011011001110001111010101011010011010111001000011011010100100100000110011011111010010110011110101110000101000001001000011010000100101000110010101100010110110001111011000110111000100011111111100000011110000011111000101011010001111100000000110010011010000100011001101101000100000010111011101000011100001110110011101001010100010111010000000110010101110100101011010001010100010010111010000110111101110101111000011000011001110110011111100010000101110111001101101111000011010110010010111100100100010111100101000010000011011111111100101011101110110000000001010101010101011000110000010100000000000100000011100000101000000000001000101111000000101111111110110011101111011100111100101000111110001101100000001001110010001010010110011110000001010001101100010000010100010011010001001001110110111110011100011111110010110011010101110010101101001111010100110111011001000100010000001000111100111001110011111100101101011101101010101100010000101111101110101101100001110111101110110010111001001011011111001100101100011011000100101000100011011100010000110011010010111110010010100011000111011100011101011011010100110011100101100101011001101101101010111101001000100110100111000110000111100001101100010111010101100111011110011110001000101101100111011010011110001001001001100111011111010110111010111000110111101000011111011011111010111000110011101101111000111100001101110101001111101000010101101010010100100101101010001111101001111011101000101111000110010100101110110101101110111101100001000100000110001101110000110100010010101010000100000101000110100110101111110111001000100110001101101101010000000110000101110101010111100110101110001100001001110100101100011111110110001010011011000101111000010000100000001000011111100011011101110001111101110110101011011110001001101110101000000100101010101110110111010110100010101000101001010110100001000010001111011100100011110101011111011001111011100111000110000101111110100111111111101010001000001110111101001110111111101001110111110011101001011011101000110101111011111100000110101010101011001111110001110010110111100111100111000011000111001101010011000010100011011110110101011111100001101010000001010001110101010101111101011000011010010011011111110011110010100000001000001111011101000110011101000100111101000010000011110011110111111101101010100110101000001110011010010100010000010100111100010110100100110100111111011011101011100000110111110001101011101011111001010001011000001111000010101110100101010000101101110110001100010001111100010001000000011110001100110011101100101101001111000001110101111100011011001101010100000000110100001011111111010110010010111001100101100110110000111110111111010010111110010110111001000101111010001000001111111100011011011101001101110000101110100010001011100101001101110011110010100110111010111001110101111001011111011110001000101011111000010010000010011010011010111011110110110010101001010111010111110100101010110101000100111010100000010110000110100010100000100111101011011111000111110001110011110111000100101101100000010001000011001101001000001011001011111001010001011011000011011100001101111010001110010111110100001011100100110110011110101000110111001101000101100011011100101111001011001000101101011011001100001011000000011111000100010011111011001111111001100111010101101100110100110011000101011111010111101010001010011001010010010011001100101011001111001101010010000101001001101010001000111111100000001011110000100111011101111011100001000000000101011101111000011101010010111100100101111010100011001001010100101100100101011110010001011011101011011110100010100001011101111000000010001110111001011110111111110010011000011001010110101100011010110100101000000010100011110011010000010110111100001111010000000110111101110111010011111101010000100100010000100100000000010100100010010001010111011110010110001110110011101110111110011010010101100001100011000110010110100110001010001010011101100111111011001101110011001110011000010010001010000110110100100001000110000110111110101000000111000100011110001001000110101101111001011000001010000100000001101110000011100111001010101001000110010011001000111000111101010001111100110011000001101000110010000110001011010110011100111110101101100011011011001010100001111110001011011001010000011100011101010001000011101110001001000000110001001011011010100001011100010111010100000001110001011100100101110001000110111010001001101111101100110100100110011101011011001110100101011110000011101010001010111101101010110001101110010011111010010000011010111000011100111011101111000000110011100111001011001000101100011011001000010011001101000101000111101011111101001100101000110110100110101001101011110100000100101001010010010010010101001011110000000001110101000010010111111001001100100000011100110101100011010110110001011111101000111000010110111110111101101011100001111111011101011101010000001110110000011001000001111010000111000101110101101001101101011001011111000100001100111100111111110100010011011000000010010000011001100111110010010001000110011001001111101110101011110010010010100010101010001001111101101010101101000011001110000111100001001000101000011110111000010111111111000000000101001101100101100101111110010000101100001001000001000001010101001010000010110011110001111010101101001010000110011100110100111101001010100011100100101100101100011011101100001111000110111001011101111011000110111010111101111011111000000101110110011101010111011001100010001110100010111000110101111100101001001000000110011011000111110100001011111010110110011000001110010111111110100010000000001100101101011000001000101111110000111101010101111110100111111000001010001100011011101001100011011110101101100110010000010010111111101100000011111010110010101000111011010110001010100100011100011000101000011111010011010001010010110111001110100111010101001000110010101100011010011000011001111001110011111101110111110101011101001011111101100011111000010011110111010100010110010011001001011000100110111100100011101000010011011010011111100011001110011011011011001101111000101011101100011000001010100011001100010111011111101110000011001101100001001111101011110010101001010110100001011000100101001111110100101111011101001111011011010101100110011100111000110010011110001010101100001111000110110110111000101000011111000011111011000101100110111100100010110110111000110101000001001100100110111001100100101100001100110111100011001101110010001000100100100011001011000001111110010110100100000010101110100100110101110101001001011101110110011111010010011100110011000010111000100110101100101001111110000111000000101100010011100000101001100101000010011101110110110000110110011011001011001100110001000011010001010101111110000011111101101111111110001001101111101100010101110110100011010001010110000101111010110101100111011010010101100111011001101001010001011111000100111000000110110101110100001010100011100111000000110011101000001110111111011010011010010111011001101110000001100011111010010111101000010010011101000000100011001011011101110010101110000101000001010110110110100001101000100110100001101000111001000111101010010001011001101100101000010011110010001110000101100001000100001111000000011011010010010111000010010100001001111001110101100111000011001111001001011010111111001011011110010010011011010111000000011110011111000000110000111100011101100100001000111011100111011101001100000011101011101010001011101111110111011110011011101111001101000111100110100010010000101011011010100011100011011010110011100101011100011011010010111000111001010111101100000110111001111101011001010111110110001000010011000111011101111111111111000000001011101000100110010000110010100011001100010111101000101011001101011001001010111010001111100111101100001101111000011000000001001110100110011101111000101100110100001010101000111001001010010000010010110111100010011000001001000101101111010101110011111001100101110101000001010100111111000000111101001000011100010000110010011101111110011101110111011100110110010101110001011000001010101110111100000101100011110111000001110100000110001101011110011001110111110110101100011111101010011110001110110101000000001010100011001010111000000111110111111111001101111000001001010111010100100110010000000011101011111000001001011001101101110101010001111001101100000101100101100100010010100101110010110010110000100010110111110110101101011011111110100010000111001011100000000011111011111111011011100010111011101000101011010011111101000001110110010110010101110111110101101000000001010000100010111010101111001001001100000101111010001010001000101011010000000101101001101101010110101001110101110111011100001111001100010111100010101100101010011101111000000100110001100111010101011000101010010001111101101011101100101111000101100011100110011001000110011010000010001100011100011000111101000001100010101111010011010011"

        binary_delimeter = bin(int.from_bytes(delimiter.encode(), 'big'))
        binary_delimeter = binary_delimeter[2:]
        extracted = ""

        del_size = len(binary_delimeter)
        flag = 0
        j = 0
        for i in fla_arr:
            if (j >= len(key)):
                break
            extracted += str((i & 1) ^ int(key[j]))
            j += 1
            if(len(extracted) >= del_size):
                if(binary_delimeter == extracted[-del_size:]):
                    flag = 1
                    break
        if(flag == 0):
            ans = "no message found with your key!!!"
            return ans
        else:
            extracted = "0b" + extracted
            binared = int(extracted, 2)
            ans = binared.to_bytes((binared.bit_length() + 7) // 8, 'big').decode()
            ans = ans[:-len(delimiter)]
            return ans




