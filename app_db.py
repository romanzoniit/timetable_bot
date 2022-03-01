from db_utils import MongodbService
from read_excel import parse_day, parse_group_idx
storage = MongodbService.get_instance()

data_day = parse_day()
data_group = parse_group_idx()

storage.save_data_days(data_day)
storage.save_data_groups(data_group)

