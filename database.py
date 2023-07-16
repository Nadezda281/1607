def write_info(info):
    with open("data.txt","a",encoding="utf-8") as file:
        file.write(info)

def find_info(char):
    with open("data.txt","r",encoding="utf-8") as file:
        lst_sel= []
        lst = file.readlines()
        count = 0
        for line in lst:
            if char in line:
                count += 1
                print(f"{count}) {line.strip()}")
                lst_sel.append(line)
                return lst_sel


def view_all():
   with open("data.txt","a",encoding="utf-8") as file:
       print(file.read()) 

def change_data(old_data, new_data):
    with open("data.txt","r",encoding="utf-8") as file:
        lst_old = file.readlines()
    with open("data.txt","w",encoding="utf-8") as file:
      for line in lst_old:
          if old_data in line:
              file.write(new_data)
          else:
              file.write(line)

              
def delite_data(old_data):
    with open("data.txt","r",encoding="utf-8") as file:
        lst_old = file.readlines()
    with open("data.txt","w",encoding="utf-8") as file:
      for line in lst_old:
          if old_data in line:
              continue
          else:
              file.write(line)

def sort_data(x):
    year=str ( x.split(",")[1]).split(".")[2]         
    month=str ( x.split(",")[1]).split(".")[1]          
    day=str ( x.split(",")[1]).split(".")[0]
    return year, month, day       
                      

def sort (sort_num):
    with open("data.txt","r",encoding="utf-8") as file:
        lst_old = file.readlines()  
        if sort_num==1:
            lst_old.sort(key = lambda x : x.split(",")[0])
        elif sort_num==2:
            lst_old.sort(key = sort_data)
        elif sort_num ==3:
            lst_old.sort(key=lambda x: int(x.split(",")[2]))
            with open("data.txt","w",encoding="utf-8") as file:
             file.writelines(lst_old)

           