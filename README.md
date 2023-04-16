#MICROPROCESSOR COMPILATOR FOR IMTC20 PROCESSOR.
This is a personal project I started to create a tool that will help to verify the microprocesor
I designed for mi Tesis. After some trainings in Python OOP, I managed to reach a better version
of the compilator, using OOP, classes for the commands and applying heritance and override of methods
from the parent classes. This helped to condese the code and the methods to identify the type of command.
The original purpose of this project is to apply the studied in python and train my skills in Python OOP.

Notes for future upgrades:
    -   Add support to use Labels in the code, to avoid the user to manually calculate the address
        he wants to the code jump to when using a conditional or undontional jump.
    -   Implementing the use of labels will help to create variables in the code and use them along
        the commands.
    -   Add suport to use different number base to the values, at the moment, the program just supports
        hexadecimal base numbers.
    -   Support to use parameters defining the length of the Address bus and the Data bus to make the
        code scalable for future changes to the processor IMTC20.