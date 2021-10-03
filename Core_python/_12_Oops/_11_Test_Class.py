class DataList:
    def _init_(self, data):
        self.data = data

    def sort_super_elements(self):
        list_elements = self.data
        try:
            if isinstance(self.data, list):
                self.data = sorted(list_elements)
            self.print_input_data()
        except TypeError as te:
            print("Some elemets inside list are not integers")
            return "Unable to sort"

    def print_input_data(self):
        print("List Data of elements after sorting:: ", self.data)
        try:
            if self.subdata:
                print("Dict Data of elements after sorting:: ", self.subdata)
        except:
            return "Unable to print dict data"


class SubData(DataList):
    def _init_(self, data, subdata):
        super(SubData, self)._init_(data)
        self.subdata = subdata

    def sort_sub_elements(self):
        # super().sort_super_elements(self)
        sub_dict = self.subdata
        try:
            if isinstance(sub_dict, dict):
                dict2 = sorted(sub_dict.items(), key=lambda val: val[1], reverse=False)
                self.store_data_to_file(dict2)
                self.read_data_from_file()
            super(SubData, self).print_input_data()
        except TypeError as te:
            print("Some elemets inside list are not integers")
            return "Unable to sort"

    def store_data_to_file(self, dict_data):
        with open("data.txt", 'w') as write_file:
            print("Writing data to file")
            write_file.write(dict_data)

    def read_data_from_file():
        with open("data.txt", 'r') as read_data:
            print("Reading data from  file")
            read_data.readlines()


# list_obj = DataList(list(1,12,7,4,21,2))
# list_obj.sort_super_elements()


sub_obj = SubData([2, 13, 8, 5, 22, 3], {'A': 4, 'B': 1, 'C': 2, 'D': 3})
sub_obj.sort_sub_elements()
