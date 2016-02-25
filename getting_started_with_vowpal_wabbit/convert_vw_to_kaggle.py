import csv
with open("preds_titanic.txt", "r") as infile, open("kaggle_preds.csv", "wb") as outfile:
  outfile.write("PassengerId,Survived\n")
  for line in infile.readlines():
    kaggle_line = str(line.split(" ")[1]).replace("\n","")
    if str(int(float(line.split(" ")[0]))) == "1":
      kaggle_line += ",1\n"
    else:
      kaggle_line += ",0\n"
    outfile.write(kaggle_line)