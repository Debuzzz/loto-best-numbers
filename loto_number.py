import requests
from bs4 import BeautifulSoup


def compute_values(Matrix):
    


def returned_values(Tab1, Tab2):
    
    Final_List = []

    L1 = compute_values(Tab1)
    for val in range(5):
        Final_List.append(L1[val])
    Final_List.append(L2[0])


def main() :

    first_page = requests.get('https://www.secretsdujeu.com/page/jeux_loto_statistiques.html')

    soup = BeautifulSoup(first_page.content, 'html.parser')

    res = soup.find_all('tbody')

    Table1_max_col = 14
    Table1_max_line = 49
    Table1 = [[0 for _ in range(Table1_max_col)] for _ in range(Table1_max_line)]

    index = 0
    toTest = str(res[0])

    for i in range(Table1_max_line):
        for j in range(Table1_max_col):
            val = ""
            while not str.isdigit(toTest[index]):
                index += 1

            while str.isdigit(toTest[index]):
                val += toTest[index]
                index += 1
            Table1[i][j] = int(val)

    second_page = requests.get('https://www.secretsdujeu.com/page/jeux_loto_statistiques.html')

    soup = BeautifulSoup(second_page.content, 'html.parser')

    res = soup.find_all('tbody')

    Table2_max_col = 12
    Table2_max_line = 10
    Table2 = [[0 for _ in range(Table2_max_col+2)] for _ in range(Table2_max_line)]

    index = 0
    toTest = str(res[0])

    for i in range(Table1_max_line):
        for j in range(Table1_max_col):
            val = ""
            while not str.isdigit(toTest[index]):
                index += 1

            while str.isdigit(toTest[index]):
                val += toTest[index]
                index += 1
            Table2[i][j] = int(val)

    return (Table1, Table2)

# EXEC

(Tab1, Tab2) = main()



# END
