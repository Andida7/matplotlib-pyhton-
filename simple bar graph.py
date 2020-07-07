#this program displays a simple bar graph
import matplotlib.pyplot as plt
def main():
    #create coordinates
    
    left_edges = [0, 10, 20, 30, 40]
    heights = [100, 200, 300, 400, 500]
    #change the bar width
    bar_width = 5

    #plot it and color the bars and align it to the left
    plt.bar(left_edges, heights, bar_width,align = 'edge', color=('r', 'g', 'b', 'c', 'k'))
    #add x and y lables
    plt.xlabel('Years')
    plt.ylabel('Sales')
    #title
    plt.title('Sales by Year')
    plt.xlim(xmin= 0)
    
    # Customize the tick marks.
    plt.xticks([2.5, 12.5, 22.5, 32.5, 42.5],
                ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],
                ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])
    
    #diplay it 
    plt.show()

main()