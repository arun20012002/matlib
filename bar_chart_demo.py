import matplotlib.pyplot as pl
x=['Year1','Year2','Year3','Year4','Year5','Year6']
y=[10,20,30,40,50,60]

#HorizontalBar
pl.barh(x,y,color='c')
pl.xlabel("Years")
pl.ylabel("Values")
pl.title("Bar chart Demo")
pl.show()

#pl.bar(x,y,color=['r','g','y','b','c','b'],      width=[0.5,0.2,0.3,0.1,0.3,0.1])
#pl.bar(x,y,color='c',width=0.5)
#

#HorizontalBar
#pl.barh(x,y,color='c')


