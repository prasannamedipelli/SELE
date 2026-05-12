import matplotlib.pyplot as plt

#line graph
students = ["ram","shyam","hari","tinu"]

marks =[89,65,99,69]

plt.bar(students,marks)

plt.title("Student marks")

plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()
             