import matplotlib.pyplot as plt
def main():
    #create the values
    value =  [20, 60, 80, 40]
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']
    #plot it 
    plt.pie(value, labels = slice_labels)
    #title
    plt.title('Sales by Quarter')
    #display
    plt.show()

main()    