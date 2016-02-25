import csv
import re
i = 0
def clean(s):
  return " ".join(re.findall(r'\w+', s,flags = re.UNICODE | re.LOCALE)).lower()
with open("train.csv", "r") as infile, open("train.vw", "wb") as outfile:
  reader = csv.reader(infile)
  for line in reader:
    i+= 1
    if i > 1:
      vw_line = ""
      if str(line[1]) == "1":
        vw_line += "1 '"
      else:
        vw_line += "-1 '"
      vw_line += str(line[0]) + " |f "
      vw_line += "passenger_class_"+str(line[2])+" "

      vw_line += "last_name_" + clean(line[3].split(",")[0]).replace(" ", "_") + " "
      vw_line += "title_" + clean(line[3].split(",")[1]).split()[0] + " "
      vw_line += "sex_" + clean(line[4]) + " "
      if len(str(line[5])) > 0:
        vw_line += "age:" + str(line[5]) + " "
      vw_line += "siblings_onboard:" + str(line[6]) + " "
      vw_line += "family_members_onboard:" + str(line[7]) + " "
      vw_line += "embarked_" + str(line[11]) + " "
      outfile.write(vw_line[:-1] + "\n")
i = 0
with open("test.csv", "r") as infile, open("test.vw", "wb") as outfile:
  reader = csv.reader(infile)
  for line in reader:
    i+= 1
    if i > 1:
      vw_line = ""
      vw_line += "1 '"
      vw_line += str(line[0]) + " |f "
      vw_line += "passenger_class_"+str(line[1])+" "
      vw_line += "last_name_" + clean(line[2].split(",")[0]).replace(" ", "_") + " "
      vw_line += "title_" + clean(line[2].split(",")[1]).split()[0] + " "
      vw_line += "sex_" + clean(line[3]) + " "
      if len(str(line[4])) > 0:
        vw_line += "age:" + str(line[4]) + " "
      vw_line += "siblings_onboard:" + str(line[5]) + " "
      vw_line += "family_members_onboard:" + str(line[6]) + " "
      vw_line += "embarked_" + str(line[10]) + " "
      outfile.write(vw_line[:-1] + "\n")