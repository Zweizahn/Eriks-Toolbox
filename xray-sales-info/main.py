__author__ = 'Erik'

test_file = "D:/work/Kunden/QSC/QSC XRAYs 26102015/QSC XRAYs 26102015/NSS10A-G6-xray-151027-111334-build7088.xml"

# We need the following items
item_list = ['Host name', 'Total physical storage', 'Licensed physical storage', 'Prepared for Virtualization',
             'License Value']

if (__name__ == "__main__"):
    with open(test_file) as file:
        for line in file:
            line.strip()
            for item in item_list:
                if line.find(item) > 0:
                    output = line.split('"')
                    try:
                        print('{} {}'.format(output[1],output[3]))
                    except:
                        print('{}'.format(output[1]),end='')
