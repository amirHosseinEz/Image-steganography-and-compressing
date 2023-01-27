# Design_algorithm
## Introduction
The project consists of two parts, the first part is image compression and the second
part is image steganography.<br>For the first part of the project, we used Huffman’s algorithm to compress our photo.
Huffman Coding is a method of lossless compression. Lossless compression is valuable
because it can reduce the amount of information (or in your computer, memory) needed
to communicate the exact same message. That means that the process is perfectly
invertible.<br>For the second part of the project, we hide the desired message inside the image with
the help of the LSB algorithm so that only people with the secret key can read the
message.<br>In this method, we put the desired message inside the least valuable bit of some pixels,
so the original photo and the photo containing the message will not be different for
human eyes.

## History
### Huffman Coding:
The story of the invention of Huffman codes is a great story that demonstrates that
students can do better than professors. David Huffman (1925-1999) was a student in
an electrical engineering course in 1951. His professor, Robert Fano, offered students
a choice of taking a final exam or writing a term paper. Huffman did not want to
take the final so he started working on the term paper. The topic of the paper was to
find the most efficient (optimal) code. What Professor Fano did not tell his students
was the fact that it was an open problem and that he was working on the problem
himself. Huffman spent a lot of time on the problem and was ready to give up when
the solution suddenly came to him. The code he discovered was optimal, that is, it had
the lowest possible average message length. The method that Fano had developed for
this problem did not always produce an optimal code. Therefore, Huffman did better
than his professor. Later Huffman said that likely he would not have even attempted
the problem if he had known that his professor was struggling with it.

### Steganography:
Steganography comes from the Greek steganos (covered or secret) and -graphy (writing
or drawing). Steganography can be defined as the hiding of information by embedding
messages within other, seemingly harmless messages, graphics or sounds. The first
steganographic technique was developed in ancient Greece around 440 B.C. The Greek
ruler Histaeus employed an early version of steganography which involved: shaving the
head of a slave, tattooing the message on the slaves scalp, waiting for the growth of hair
to disclose the secret message, and sending the slave on his way to deliver the message.
The recipient would have the slave’s head to uncover the message. The recipient would
reply in the same form of steganography. In the same time period, another early form of
steganography was employed. This method involved Demerstus, who wrote a message
to the Spartans warning of eminent invasions from Xerxes. The message was carved
on the wood of wax tablet, and then covered with a fresh layer of wax. This seemingly
blank tablet was delivered with its hidden message successfully. Steganography continued development in the early 1600s as Sir Francis Bacon used a variation in type
face to carry each bit of the encoding. Steganography continued over time to develop
into new levels. During times of war steganography is used extensively. During the
American Revolutionary War both the British and American forces used various forms
of Invisible Inks. Invisible Ink involved common sources, this included milk, vinegar,
fruit juice, and urine, for the hidden text. To decipher these hidden messages required
light or heat. During World War II the Germans introduced microdots. The D1.1 microdots were complete documents, pictures, and plans reduced in size to the size of a
period and attached to common paperwork. Null ciphers were also used to pass secret
messages. Null ciphers are unencrypted messages with real messages embedded in the
current text. Hidden messages were hard to interpret within the innocent messages.<br>An example of an innocent message containing a null cipher is:<br>Fishing freshwater bends and saltwater coasts rewards anyone feeling stressed. Resourceful anglers usually find masterful leapers fun and admit swordfish rank overwhelming any day. By taking the third letter in each word the following message
emerges:<br>Send Lawyers, Guns, and Money

## Applications
### Huffman Coding:
Uses of Huffman encoding includes conjunction with cryptography and data compression. Huffman Coding is applied in compression algorithms like DEFLATE (used in
PKZIP), JPEG, and MP3.<br>ZIP is perhaps the most widely used compression tool that uses Huffman Encoding as
its basis.
### Steganography:

#### * Digital Watermarking : 
Digital watermarking is the procedure of embedding data into
a digital signal in a way that is complex to delete. The signal can be audio, pictures
or video.<br>For example, if the signal is copied, and then the data is also carried in the copy. A
signal can carry several multiple watermarks at the same time.
#### * Visible Watermarking :
In this visible watermarking, the information is visible in the picture or video. Generally, the information is text or a logo which recognizes the owner of the media. When a television broadcaster insert its logo to the corner of
transmitted video, and this is also a visible watermark.
#### * Invisible Watermarking :
In this invisible watermarking, information is inserted as digital data to audio, picture or video, but it cannot be perceived as such (although it
can be possible to recognize that some amount of data is hidden).<br>The watermark can be pre-determined for extensive use and is therefore create simply
to fetch or it can be a form of Steganography, where a party connects a hidden message installed in the digital signal.<br> 

## How it works?
### Huffman Coding:
The algorithm works by building a tree T in a bottoms-up manner using a priority
queue Q that selects the two least frequent objects and merges them together, in turn
creating a new object whose frequency is the sum of the frequencies of the two merged
objects. This process is repeated until all words in the input text are encoded. In this
way, the objects that have the highest frequency will have a shorter code.<br>For the first part of this project, I tried three different methods to implement the algorithm, so the objects I used for Huffman coding were:<br> 1- Pixels<br> 2- The text resulting
from opening the image in .txt format<br> 3- Open the image as a binary file and take
every 8 bits (1 byte) as an object<br> The first method that came to my mind was the first
method, that is, to consider each pixel as an object. After doing this method, I realized
that the size of my file increased significantly, and this issue confused me until I noticed
that the JPG format uses different compressions. Since I had to reduce the image size,
I needed another method. The second method was simple: I opened the photo file as
text and considered each object a character. Still, this method needed to be corrected
because there are bytes inside the photo file corresponding to the desired character in
the encoding (ANSI, UTF8). If it exists, this method will be entirely correct, and if it
doesn’t exist, it will be incorrect. So I decided to use the third method, opening the
image as a binary file.

### Steganography:

For the second part, I took the help of the LSR algorithm in such a way that I xored
the desired message with the secret key and then put the equivalent of the ASCII code
bit by bit in the last bit of the pixels. The receiver should use the same secret key to
extract the message from the pixels.

## Result
Since this project was supposed to compress images and formats such as JPG and PNG,
which are already compressed, running the Huffman algorithm on them will compress
a small volume because they have been compressed considerably. And depending on
the image itself, the amount of compression will differ. For example, the image I used for compression changed size from 36.8 KB to 36.6 KB, which includes only 0.2 KB of
volume reduction, or in other words, CR = 0.54%<br>
There are many ways for steganography. I got help from LSR in this project and saved
the message inside the image using the secret key. I considered the secret key as a key
that is xored with the message, but I could also use other methods, for example, to
put my message in certain indexes of the pixels and send the address of the index as a
secret key to the recipient.


