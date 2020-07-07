import matplotlib.pyplot as plt
def main():
    #create a simple line graph
    #create a coordinate for x and y
    x = [0,1,2,3,4,5]
    y = [1,6,4,5,6,4]
    #build the graph
    plt.plot(x, y, marker='d')
    #add a title 
    plt.title('Sample data')
    #x axis discription (adding lables to the axis)
    plt.xlabel('Age')
    plt.ylabel('Result')
    #set the axis's limits
    plt.xlim(xmin= 0, xmax= 6)
    plt.ylim(ymin= 0, ymax= 6)
    #customize the tick markers
    plt.xticks([0,1,2,3,4,5], ['a','b','c','d','e','f'])
    plt.yticks([0,1,2,3,4,5,6], ['A', 'B', 'C', 'D', 'E', 'F','G'])
    #add a grid
    plt.grid(True)
    #display it
    plt.show()

main()    

