import datetime
import pandas as pd
import functions as fn

path = "C:\\COVID-19 Data Analysis\\"

kl_data_set = pd.read_csv(path + "kerala_dataset.csv")
kl_data_set.fillna(int(0), inplace = True)
kl_data_set['Date'] = [datetime.datetime.strptime(dt, '%d-%b-%y').date() for dt in kl_data_set.Date]
kl_data_set.set_index('Date', inplace = True)
kl_field_dict = {1:'Confirmed', 2:'Recovered', 3:'Deceased', 4:'Daily_Cases', 5:'Daily_Recovered', 6:'Daily_Deceased', 8:'Tested'}

in_data_set = pd.read_csv(path + "india_dataset.csv")
in_data_set.fillna(int(0), inplace = True)
in_data_set['Date'] = [datetime.datetime.strptime(dt, '%d-%b-%y').date() for dt in in_data_set.Date]
in_data_set.set_index('Date', inplace = True)
in_field_dict = {1:'Total Confirmed', 2:'Total Recovered', 3:'Total Deceased', 4:'Daily Confirmed',  5:'Daily Recovered', 6:'Daily Deceased'}

kl_dis_data_set = pd.read_csv(path + "kerala_district_dataset.csv")
kl_dis_data_set.fillna(int(0), inplace = True)
kl_dis_data_set['Date'] = [datetime.datetime.strptime(dt, '%d-%b-%y').date() for dt in kl_dis_data_set.Date]
kl_dis_data_set.set_index('Date', inplace = True)
kl_dis_dict = { 1:'Alappuzha', 2:'Ernakulam', 3:'Idukki', 4:'Kannur', 5:'Kasaragod', 6:'Kollam', 7:'Kottayam', 8:'Kozhikode', 9:'Malappuram', 10:'Palakkad',
               11:'Pathanamthitta', 12:'Thiruvananthapuram', 13:'Thrissur', 14:'Wayanad'}
kl_dis_fdict = {1:'Confirmed', 2:'Recovered', 3:'Deceased'}

kl_data_set.drop('Other', 1, inplace = True)
kl_data_set.drop('State', 1, inplace = True)
in_data_set.drop('Date_YMD', 1, inplace = True)

def plot_menu():
    print( '''Enter the corresponding number to chose the option to plot the data from:
           1.Kerala
           2.Kerala District wise
           3.National
           ''')

    pltmenu_choice = input("Option: ")

    if( pltmenu_choice == '1'):
        print('''\nChose the fields to be plotted:
            1.Confirmed Cases
            2.Recovered
            3.Deceased
            4.Daily Cases
            5.Daily Recovered
            6.Daily Deaths
            7.Tested
        ''')
        feild_list = list(map(int, input("Enter the options separated by space: ").split()))
        print(feild_list)
        fn.plot(kl_data_set, feild_list, kl_field_dict, "Kerala COVID-19 Data")

    elif( pltmenu_choice == '2'):
        print('''\nEnter the corresponding numbers of the districts whose data should be plotted:
            1.Alappuzha
            2.Ernakulam
            3.Idukki
            4.Kannur
            5.Kasaragod
            6.Kollam
            7.Kottayam
            8.Kozhikode
            9.Malappuram
            10.Palakkad
            11.Pathanamthitta
            12.Thiruvananthapuram
            13.Thrissur
            14.Wayanad
            15.ALL DISTRICTS
        ''')
        district_list = list(map(int, input("Enter the options separated by space: ").split()))
        if(district_list == [15]):
            district_list = [*range(1,15)]
        print('''\nChose the data to be plotted(chose only one option):
            1.Confirmed Cases
            2.Recovered
            3.Deceased
                ''')
        field = int(input("Enter the option: "))
        fn.dis_plot(kl_dis_data_set,district_list,kl_dis_dict, kl_dis_fdict[field],"District Data")

    elif( pltmenu_choice == '3'):
        print('''\nChose the datas to be plotted
            1.Confirmed Cases
            2.Recovered
            3.Deceased
            4.Daily Cases
            5.Daily Recovered
            6.Daily Deaths
        ''')
        feild_list = list(map(int, input("Enter the options separated by space: ").split()))
        fn.plot(in_data_set, feild_list, in_field_dict, "India COVID-19 Data")
    else:
        print("Invalid Input")

def retrieve_menu():
    print('''\nChose the dataset for data to be retrieved from:
            1.Kerala
            2.National
            3.Kerala District wise
            4.Kerala and National
    ''')
    ret_menu_choice = input("Option: ")
    print("\nEnter date/range of date of the data to be retreived in the format '14-May-20'/'05-Jun-20 15-Jun-20':")
    date_string = input().split()
    date_range = [datetime.datetime.strptime(dt, '%d-%b-%y').date() for dt in date_string]

    if(ret_menu_choice == '1'):
        if(len(date_range) == 1):
            print("\nKerala Data ", date_range[0].strftime("%d-%b-%Y"))
        elif(len(date_range) == 2): 
            print("\nKerala Data", date_range[0].strftime("%d-%b-%Y"),"to", date_range[1].strftime("%d-%b-%Y"), "\n")
        else:
            print()
        fn.retrieve(kl_data_set, date_range)

    elif(ret_menu_choice == '2'):
        print("\nIndia Data", date_range[0].strftime("%d-%b-%Y"), end =' ')
        if(len(date_range) == 2): 
           print("to", date_range[1].strftime("%d-%b-%Y"), "\n")
        else:
            print()
        fn.retrieve(in_data_set, date_range)

    elif(ret_menu_choice == '3'):
        print("\nKerala District Data", date_range[0].strftime("%d-%b-%Y"), end =' ')
        if(len(date_range) == 2): 
           print("to", date_range[1].strftime("%d-%b-%Y"), "\n")
        else:
            print()
        fn.retrieve(kl_dis_data_set, date_range)

    elif(ret_menu_choice == '4'):
        print("\nKerala Data", date_range[0].strftime("%d-%b-%Y"), end =' ')
        if(len(date_range) == 2): 
           print("to", date_range[1].strftime("%d-%b-%Y"), "\n")
        else:
            print()
        fn.retrieve(kl_data_set, date_range)

        print("\nIndia Data", date_range[0].strftime("%d-%b-%Y"), end =' ')
        if(len(date_range) == 2): 
           print("to", date_range[1].strftime("%d-%b-%Y"), "\n")
        else:
            print()
        fn.retrieve(in_data_set, date_range)
    else:
        print("Invalid Input")

def main():
    print('''Chose the required Option
    1.Plot Data
    2.Retreive Data
    3.EXIT
    ''')
    choice = input("Enter Option: ")
    if(choice == '1'):
        plot_menu()
    elif(choice == '2'):
        retrieve_menu()
    elif( choice == '3' or not choice):
        return 'exit'
    else:
        print("Invalid Input")

if __name__=="__main__": 
    print("----------------------------------------------------------------------------------------".center(120))
    print("COVID-19 DATA ANALYSER".center(120))
    print("----------------------------------------------------------------------------------------".center(120))
    print("\n")
    while(True):
        if(main() == 'exit'):
            break
        print("----------------------------------------------------\n")



