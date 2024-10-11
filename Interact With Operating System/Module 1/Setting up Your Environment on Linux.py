# from PIL import Image
# image = Image.open("./houses.png")
# print(image.size)

import pandas
visitor = [1234, 9764, 3456, 2345, 7643]
err = [23, 12, 34, 55, 77]
df = pandas.DataFrame({"Visitor": visitor, "Error": err}, index = ["Mon", "Tues", "Wed", "Thu", "Fri"])
print(df)
print(df["Error"].mean())