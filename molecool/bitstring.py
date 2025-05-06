import numpy as np
import math      
import copy as cp       

class BitString:
    """
    Simple class to implement a config of bits
    """
    def __init__(self, N):
        self.N = N
        self.config = np.zeros(N, dtype=int) 

    def __repr__(self):
        out = ""
        for i in self.config:
            out += str(i)
        return out

    def __eq__(self, other):        
        return all(self.config == other.config)
    
    def __len__(self):
        return len(self.config)

    def on(self):
        """
        Return number of bits that are on
        """
        counter = 0
        for bit in self.config:
            if bit == 1:
                counter += 1
        return counter
    

    def off(self):
        """
        Return number of bits that are off
        """
        counter = 0
        for bit in self.config:
            if bit == 0:
                counter += 1
        return counter

    def flip_site(self,i):
        """
        Flip the bit at site i
        """
        self.config[i] = (self.config[i] + 1) % 2
    

    def integer(self):
        """
        Return the decimal integer corresponding to BitString
        """
        integer = 0
        n = len(self.config) - 1
        for bit in self.config:
            if bit == 1:
                integer += 2 ** n
            n-= 1
        return integer

    def set_config(self, s:list[int]):
        """
        Set the config from a list of integers
        """
        self.config = s

    def set_integer_config(self, dec:int):
        """
        convert a decimal integer to binary
    
        Parameters
        ----------
        dec    : int
            input integer
            
        Returns
        -------
        Bitconfig
        """
        binary = [0] * len(self.config)
        count = len(self.config) - 1
        while dec != 0 and count>=0:
            binary[count] = dec % 2
            dec = int(dec / 2)
            count -= 1
        self.config = np.array(binary)