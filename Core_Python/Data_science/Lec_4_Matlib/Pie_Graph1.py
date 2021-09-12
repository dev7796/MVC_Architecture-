import matplotlib.pyplot as plt

# The slice names of a population distribution pie chart

pieLabels   = 'Asia', 'Africa', 'Europe', 'North America', 'South America', 'Australia'

# Population data

populationShare     = [59.69, 16, 9.94, 7.79, 5.68, 0.54]


figureObject, axesObject = plt.subplots()

print('figureObject>>>',figureObject)
print('axesObject>>>>>',axesObject)

# Draw the pie chart
explodeTuple = (0.0, 0.0, 0.0, 0.0, 0.0,0.4)

# Draw the pie chart

axesObject.pie(populationShare, explode=explodeTuple,

        labels=pieLabels,

        autopct='%1.2f',

        startangle=90)

# axesObject.pie(populationShare,

#         labels=pieLabels,

#         autopct='%1.5f',

#         startangle=90)

 

# Aspect ratio - equal means pie is a circle

axesObject.axis('equal')

 

plt.show()