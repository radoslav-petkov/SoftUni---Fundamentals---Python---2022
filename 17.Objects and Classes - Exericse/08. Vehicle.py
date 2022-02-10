class Vehicle:
    def __init__(self,type,model,price) -> None:
        self.type = type
        self.model = model
        self.price = price
        self.owner = None

    def buy(self,money: int,owner: str) -> str:
        if self.owner != None:
            output = "Car already sold"
        else:
            if money >= self.price:
                change = money - self.price
                self.owner = owner
                output = f"Successfully bought a {self.type}. Change: {change:.2f}"
            else:
                output = "Sorry, not enough money"

        return output

    def sell(self):
        if self.owner != None:
            self.owner = None
            pass
        else:
            return "Vehicle has no owner"

    def __repr__(self) -> str:
        if self.owner != None:
            output = f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            output = f"{self.model} {self.type} is on sale: {self.price}"
        return output


# Test code
vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type,model,price)
print(vehicle.buy(15000,"Peter"))
print(vehicle.buy(35000,"George"))
print(vehicle)
vehicle.sell()
print(vehicle)