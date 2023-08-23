def updateRemainingDays():
  print(read_date()[0:10], str(datetime.now().date()))
  if read_date()[0:10] == str(datetime.now().date()):
    #print(read_date()[0:10],str(datetime.now().date()))
    #print('aaj ka din ')
    pass
  else:
    #current_date=str(read_date()[8:10])
    #print(current_date)
    #print(int(current_date))
    #print(int(str(datetime.now().date())[8:]))
    #x= int(str(datetime.now().date())[8:]) - int(current_date)
    write_date()
    #all_parts=Form.query.all()
    #print('in update remaining days')
    #last_update=read_date()
    forms = Form.query.all()
    for form in forms:
      c_date = datetime.strptime(form.nextCalibarationDate, "%d-%m-%Y")
      if (c_date - timedelta(days=int(form.reminderInDays))
          ).date() <= datetime.now().date():
        if int(form.reminderInDays) > 0:
          form.reminderInDays = str(int(form.reminderInDays) - 1)
        db.session.commit()

    #for part in all_parts:


def read_date():
  file_path = 'date.txt'
  # Read the date from the text file
  with open(file_path, 'r') as file:
    date_string = file.read()
    file.close
  date_object = datetime.strptime(date_string.strip(), '%Y-%m-%d')
  return str(date_object)
  print(date_object)


def write_date():
  current_date = datetime.now()
  date_string = current_date.strftime('%Y-%m-%d')
  file_path = 'date.txt'
  with open(file_path, 'w') as file:
    file.write(date_string)
    file.close()


