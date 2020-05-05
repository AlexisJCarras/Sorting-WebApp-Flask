import matplotlib.pyplot as plt
def Visualise (data, name):  
    y_test = data
    x_length = len(data)
    x = range(x_length)

    y = [i for i, _ in enumerate(y_test)]

    plt.bar(x,data , color = 'blue')
    plt.xlabel(" ")
    plt.ylabel("Input")
    plt.title("Bar chart with input")

    plt.savefig(name + '.png', format="png")
    


    # format = "png"
    # sio = cStringIO.StringIO()
    # pyplot.savefig(sio, format=format)
    # msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY) # Needed this on windows, IIS
    # sys.stdout.write(sio.getvalue())



if __name__ == "__main__":
    Visualise([10,2,3,4,6,7])



