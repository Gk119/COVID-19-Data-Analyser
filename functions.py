import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

def plot(data_set, field_list, field_dict, title):        
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=40))

    for field in field_list:
        plt.plot(np.array(data_set.index), np.array(data_set[field_dict[field]]), label = field_dict[field])

    plt.title(title)
    plt.gcf().autofmt_xdate()
    plt.legend()
    plt.grid()
    plt.show()

def dis_plot(data_set, dis_list, dis_dict, field, title):        
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b-%y'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=40))
 
    for dis in dis_list:
        dates = np.array(data_set.loc[data_set['District'] == dis_dict[dis]].index)
        values = np.array(data_set.loc[data_set['District'] == dis_dict[dis]][field])
        plt.plot(dates, values, label = dis_dict[dis])
    
    plt.gcf().autofmt_xdate()
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

def retrieve(data_set, date_range):
    if(len(date_range) == 1):
        print(data_set.loc[date_range[0]])
    elif(len(date_range) == 2):
        print(data_set[date_range[0]: date_range[1]])
