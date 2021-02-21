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

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(10)
my_new_car.update_odometer(11)
my_new_car.read_odometer()