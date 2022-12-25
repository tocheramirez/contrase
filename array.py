import math
import os
import random
import re
import sys 


if __name__ == '__main__':
    n = int(input('ingrese numero: ').strip('0'))
    if n%2==0:
        if n in range (2,5):
            print('Not Weird');
        if n in range (6,20):
            print('Weird');
        if n>20 :
            print('not Weird');
    else:
         print('not Weird');
            
else:
    print('Weird')  
