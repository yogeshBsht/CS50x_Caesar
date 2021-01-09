# CS50x_Caesar
A program that encrypts text messages using Caesar’s cipher. The program is based on Harvard's CS50's Introduction to Computer Science 2021 OpenCourseWare's problem set-2.

The program takes plain text and key (integer) as inputs. It generates the cipher by "rotating" each letter of the plain text by key positions. Special characters, numbers and the case (lower/upper) of the letter is not changed. The cipher is printed on screen.

For instance, output for key of 13 and a plaintext of hello, world:  
&nbsp;&nbsp;&nbsp; plain&nbsp;&nbsp;text:  hello, world  
&nbsp;&nbsp;&nbsp; cipher text:  uryyb, jbeyq

References:
1. https://www.edx.org/course/cs50s-introduction-to-computer-science
2. https://cs50.harvard.edu/x/2021/psets/2/caesar/#:~:text=Implement%20a%20program%20that%20encrypts%20messages%20using%20Caesar%E2%80%99s%20cipher
