from database.db_worker import DBLoader

if __name__ == '__main__':
  db_path = './project01/entity/person_data.csv'
  db = DBLoader(db_path)

  data = db.read_db()
  print(data)