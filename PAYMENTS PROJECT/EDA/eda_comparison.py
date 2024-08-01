import pandas as pd 

# Ruta al archivo CSV
path = r'C:\Users\Onofre\Documents\IRONHACK\DataScience\PAYMENTS PROJECT\project_dataset\extract - cash request - data analyst.csv'
path2 = r'C:\Users\Onofre\Documents\IRONHACK\DataScience\PAYMENTS PROJECT\project_dataset\extract - fees - data analyst - .csv'

# Cargar los datos
requests = pd.read_csv(path, delimiter=",")

# Cargar los datos
fees = pd.read_csv(path2, delimiter=",")


# print(requests.sort_values(by='id', ascending=False).head(30))
# print(fees.sort_values(by='cash_request_id', ascending=False).head(30))
# value_counts = fees['cash_request_id'].value_counts()
# print(value_counts)

search = fees[fees['cash_request_id'] == 12225.0]
print(search)