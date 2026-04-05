import csv

class DBLoader:
  def __init__(self, file_path, fieldnames=None):
    self.path = file_path
    if fieldnames is None:
      with open(file_path) as f:
        self.fieldnames = csv.DictReader(f).fieldnames
    else:
      self.fieldnames = fieldnames
    print('connection sucessfully!')
  
  def read_db(self):
    db_rows = []
    with open(self.path) as db:
      db_reader =csv.DictReader(db)
      for db in db_reader:
        db_rows.append(db)
    
    return db_rows
  
  def add_new_data(self, obj):
    with open(self.path, 'a', newline="") as db:
      writer = csv.DictWriter(db, self.fieldnames)
      writer.writerow(obj)
    
    return obj