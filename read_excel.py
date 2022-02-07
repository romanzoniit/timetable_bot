import openpyxl
import parsetable

book = openpyxl.open(parsetable.timetable, read_only=True)

sheet = book.active


def parse_time():
     time_list = []
     for row in range(33, 46, 2):
          time_list.append(sheet[row][1].value)
     return time_list

def parse_groups():
     groups = []
     for column in range(2,sheet.max_column):
          groups.append(sheet[32][column].value)
     return groups

def parse_num_group(num_group):
     timetableday=9