import os

from lib.mpyq import WC3Map_MPQ, UnsupportedCompressionAlgorithm

# This object will provide an interface for accessing the 
# various data of a wc3 map. It will unpack the MPQ data from
# the map, and it will automatically use the read_<insert file format>
# scripts to extract the information from the files.
class WC3Map():
    def __init__(self, filehandle, useListfile = False):
        self.mpq = WC3Map_MPQ(filehandle, useListfile)
        self.listfile = []
        
        self.createListfile()
        
        
    def createListfile(self):
        standard_list = open(os.path.join("lib", "wc3Files.txt"), "r")
        
        for line in standard_list:
            line = line.rstrip()
            
            try:
                file = self.mpq.read_file(line)
            except UnsupportedCompressionAlgorithm:
                print line, "has unsupported compression"
            except:
                pass
            else:
                if file != None:
                    print line, "found"
                    self.listfile.append(file)


if __name__ == "__main__":
    with open("input/trollsnelves.w3x", "rb") as f:
        mymap = WC3Map(f)