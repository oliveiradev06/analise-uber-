import pandas as pd
from IPython.display import display

df = pd.read_csv('ncr_ride_bookings.csv')
print(df)


df.describe()

df.info()

df.columns

df.rename(columns={
    'Date' : 'Data',
   'Time' : 'Tempo',
   'Booking ID': 'ID da Reserva',
   'Customer ID' : 'ID do Cliente',
   'Vehicle Type' : 'Tipo de Veículo',
   'Pickup Location' : 'Local de Busca',
   'Drop Location' : 'Local de Entraga',
   'Cancelled Rides By Customer' : 'Corridas Canceladas Por Passageiros',
   'Cancelled Rides By Driver' : 'Corridas Canceladas por Motoristas',
    'Incomplete Rides' : 'Corridas Incompletas',
     'Incomplete Rides Reason' : 'Corridas Canceladas por Razão',
      'Booking Values' : 'Valor da Corrida',
      'Ride  Distance': 'Distancia da Corrida',
      'Driver Ratings': 'Clacificações do Motorista',
      'Customer Rating': 'Avaliação do Cliente',
      'Payment Method': 'Método de Pagamento' 
   

},inplace=True)

display(df.columns)

