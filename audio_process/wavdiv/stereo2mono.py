import wave, sys

FORMAT = {'11':'1b','12':'1h','21':'2b','22':'2h'}
# format for wave files encoded in 8 and 16 bits

SAMPLING = 128

class Stereo2Mono:
    '''open the wave file and get its parameters
        compare the channels
        it will be done in two steps.
        samples are first compared,
        then if the samples are identical
        further comparison is performed
        and the mono wave file created
        '''
    def __init__(self, name):
        self.name = name
        self.w = wave.open(self.name)

    def isStereo(self):
        if self.w.getnchannels() == 2:
            return 1
        else:
            return 0

    def format_in(self):
        self.fmt = ''.join((str(self.w.getnchannels()),
                            str(self.w.getsampwidth())))
        return FORMAT.get(self.fmt)

    def format_out(self):
        self.fmt = ''.join(('1',
                            str(self.w.getsampwidth())))
        return FORMAT.get(self.fmt)

    def Parameters(self):
        return self.w.getparams()

    def Compare(self, amplitude):
        if amplitude[0] == amplitude[1]:
            return 1
        else:
            return 0

    def CompareSampling(self):
        for s in range(0, self.Parameters()[3],SAMPLING):
            if self.Compare(wave.struct.unpack(
                self.format_in(),self.w.readframes(1))) == 1:
                pass
            else:
                print 'channels at %s are not identical,abort!'%s
                #sys.exit()
        print 'Samples pass test'

    def CompareAndSave(self):
        '''Compare all and save to mono'''
        self.w.rewind()
        self.chars = '/-\\|'
        self.Save = wave.open(self.name.split('.')[0]+
                              '-mono'+'.wav','w')
        self.newparams = (1,
                     self.Parameters()[1],
                     self.Parameters()[2],
                     self.Parameters()[3],
                     self.Parameters()[4],
                     self.Parameters()[5])

        self.Save.setparams(self.newparams)

        for i in range(1, self.Parameters()[3]+1):
            self.UnPack = wave.struct.unpack(
                self.format_in(), self.w.readframes(1))
            if self.Compare(self.UnPack) == 1:
                self.Save.writeframes(wave.struct.pack(
                    self.format_out(), self.UnPack[0]))
                sys.stdout.write(chr(13))
                sys.stdout.write('%s %i/%i     ' % (
                    self.chars[i % 4], i, self.Parameters()[3]))
                sys.stdout.flush()
            else:
                print 'Data at index %s are not the same, abort!'%i
        self.w.close()
        self.Save.close()

def main():
    try:
        name = sys.argv[1]

        w = Stereo2Mono(name)
        if w.isStereo() == 1:
            print '%s is in stereo'%name
            print 'Check for %s samples in the audio frame'%SAMPLING
            #w.CompareSampling()
            print 'Both channels seem to be identical'
            print 'Check all data frames and save to mono file'
            w.CompareAndSave()
            print 'Done'
        else:
            print '%s is already in mono'%name

    except:
        print '''usage : python stereo2mono.py the-stereo-wavefile.wav\n
        the wave file must be encoded in 8 or 16 bits'''

if __name__ == '__main__':
    main()
