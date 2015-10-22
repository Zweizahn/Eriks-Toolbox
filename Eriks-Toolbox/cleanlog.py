import sys
import os
import os.path
from datetime import datetime


class conffile():
    def __init__(self):
        self.to_delete = []
        self.count = dict()
        self.deletenr = 0
        self.max_length = 0
        self.conffile = os.path.dirname(os.path.abspath(__file__)) + '/' + 'clean-log.conf'
        self.error = ''

        on = False
        line = ''

        try:
            with open(self.conffile) as config:
                for line in config:
                    line = line.strip()
                    if line.startswith('[on]'):
                        on = True
                    elif line.startswith('[off]'):
                        on = False
                    elif on and not line.startswith('#') and not line == '':
                        self.to_delete.append(line)
        except IOError as err:
            self.error = 'Conf-File error ' + str(err)
            return

        # Compute longest string to delete. Just used for a statistical output at the end
        for key in self.to_delete:
            if len(key) > self.max_length: self.max_length = len(key)

        return

    def show_strings(self):
        output = 'Deleting lines from input file containing the following strings:\n'
        for key in self.to_delete:
            output += '{}\n'.format(key)
        return output

    def create_output_file(self, infile):
        # Constructing output file name
        time1 = str(datetime.now())
        time2 = time1.replace(" ", "_")
        time = time2.replace(":", "-")
        outfile = os.path.dirname(os.path.abspath(__file__)) + '/results/' + "messages_reduced-{}.txt".format(time)

        try:
            with open(outfile, 'a') as outhandle:
                with open(infile, 'r', encoding="ISO-8859-1") as inhandle:
                    linenr = 0
                    self.deletenr = 0
                    for line in inhandle:
                        linenr += 1
                        bool = True
                        for word in self.to_delete:
                            if word in line:
                                self.count[word] = self.count.get(word, 0) + 1
                                self.deletenr += 1
                                bool = False
                                break
                        if bool:
                            print(line.rstrip(), file=outhandle)
        except IOError as err:
            self.error = 'Messages-File error ' + str(err)
            return

        return