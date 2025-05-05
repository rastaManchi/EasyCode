class Car {
    constructor(model, color, price, speed, mileage) {
        this.model = model
        this.color = color
        this.price = price
        this.speed = speed
        this.mileage = mileage
    }

    drive(km) {
        console.log(`${this.model} преодолела ${km}км и пробег стал ${this.mileage+km}`)
        this.mileage += km
    }
}

const car1 = new Car('Supra', 'black', 5000000, 350, 25000)
console.log(car1)
car1.drive(500)