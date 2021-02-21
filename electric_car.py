class Car():
  """Uma tentativa simples de representar um carro."""

  def __init__(self, make, model, year):
    """Inicializa os atributos que descrevem um carro."""
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0
  
  def get_descriptive_name(self):
    """Devolve um nome descritivo, fotmatado de modo elegante."""
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()

  def read_odometer(self):
    """Exibe um frase que mostra a mihagem do carro."""
    print("This car has " + str(self.odometer_reading) + " miles on it.")
  
  def update_odometer(self, mileage):
    """
    Define o valor de leitura do hodômetro com o valor especificado.
    Rejeita a alteração se for tentativa de definir um valor menor 
    para o hodômetro
    """
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll an odometer!")

  def increment_odometer(self, miles):
    """soma a quantidade especificada ao valor de leitura do hodômetro."""
    self.odometer_reading += miles

class ElectricCar(Car):
  """Representa aspectos específicos de veículos elétricos."""

  def __init__(self, make, model, year):
    """Inicializando os atributos da classe-pai."""
    super().__init__(make, model, year)
    self.battery_size = 70
  
  def describe_battery(self):
    """Exibe uma frase que descreve a capacidade da bateria."""
    print("This car has a " + str(self.battery_size) + "-kWh battery")  

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()