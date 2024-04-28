import uuid
import pydenticon

generator = pydenticon.Generator(10, 10)

class Identicon:

    def __init__(self, inp_str:str = None) -> None:
        
        if inp_str == None:
            inp_str = str(uuid.uuid4())
        self.__uuid = inp_str

    def save(self, fname):

        identicon = generator.generate(self.__uuid, 30, 30, output_format="png")
        f = open(fname, "wb")
        f.write(identicon)
        f.close()

if __name__ == '__main__':

    identicon_list = [ Identicon() for i in range(0, 10) ]
    for x in range(0, len(identicon_list)):
        print(f'saving hash_{x}.png')
        identicon_list[x].save(f'hash_{x}.png')