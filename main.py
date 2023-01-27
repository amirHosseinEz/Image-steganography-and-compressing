from huffman import HuffmanCoding
from addmessage import messaging


####################### PART 1 ###########################
path = "kam.jpg"

h = HuffmanCoding(path)

output_path = h.compress()
print("Compressed file path: " + output_path)

decom_path = h.decompress(output_path)
print("Decompressed file path: " + decom_path)

final_img = h.extract_jpg_image(decom_path)
print("final img file path: " + final_img)

##########################################################
####################### PART 2 ###########################

path = final_img
h = messaging(path)
key = "key.txt"
msg = "now it looks it's working right!!! "
added = h.add_message(msg, key)
wrongkey = "wrong_key.txt"
hidden_msg = h.extract_message(added, key)
print("your encrypted message : ", hidden_msg)

##########################################################


