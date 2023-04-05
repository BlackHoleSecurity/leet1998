import sys

__banner__ = 'Csv Reader python v3.0 Created by @ciku370'
__author__ = '@ciku370'

class CSVReader:
    def get_content(self):
        """take the title and fill from the file"""
        self.FILE = open(self.FILE_NAME,'r').readlines()
        for i in self.FILE:
            # take the title
            if self.S_ == True:
                self.TITLE = i.strip().split(',')
                self.S_ = False
            # take the contents
            else:
                if i.strip() != '':
                    ai = {}
                    for i_ in range(0,len(self.TITLE)):
                        try:
                            ai.update({self.TITLE[i_]:i.strip().split(',')[i_]})
                        except IndexError: # If there is an empty column
                            ai.update({self.TITLE[i_]:''})
                    self.RESULTS.append(ai)
        self.get_long_word()
    def get_long_word(self):
        """looking for the longest word"""
        self.MAX_ALL = {i:len(i) for i in self.TITLE}
        for i in range(0,len(self.RESULTS)):
            for _ in self.TITLE:
                if len(self.RESULTS[i][_]) >= self.MAX_ALL[_]:
                    self.MAX_ALL[_] = len(self.RESULTS[i][_])
        self.create_table()
    def header_footer(self):
        """create header and footer"""
        for i in self.TITLE:
            sys.stdout.write((self.MAX_ALL[i]+2)*'-'+'+')
    def create_table(self):
        """Create and display table in the terminal"""
        # print title
        sys.stdout.write('\nread the CSV file from: %s\n\nTable:\n  +' % (self.FILE_NAME))
        self.header_footer()
        sys.stdout.write('\n  |')
        for i in self.TITLE:
            sys.stdout.write(i.center(self.MAX_ALL[i]+2)+'|')
        sys.stdout.write('\n  +')
        self.header_footer()
        # print data
        print '' # new line
        for x in range(0,len(self.RESULTS)):
            sys.stdout.write('  |')
            for i in self.TITLE:
                sys.stdout.write(' '+self.RESULTS[x][i]+((self.MAX_ALL[i]-len(self.RESULTS[x][i])+1)*' ')+'|')
            print '' # new line
	if len(self.FILE) != 1:
	    sys.stdout.write('  +')
            self.header_footer()
            print ''
        print '\n%s\n' % __banner__
    def __init__(self,file):
        self.FILE_NAME = file
        self.S_ = True
        self.RESULTS = []
        self.get_content()
if __name__ == '__main__':
    try:
        CSVReader(sys.argv[1])
    except IndexError:
       print '\n%s\nUsage: python2 %s data.csv\n' % (__banner__,sys.argv[0])
    except Exception as e:
       print('\n%s\n'%str(e))
