// const lion = {
//     name: 'Симба',
//     sound: 'p-p-p',
//     makesound: function() {
//         console.log(`${this.name} издает звук ${this.sound}`)
//     }
// }

// const elephant = {
//     name: 'Дамбо',
//     sound: 'тууууу-тууууу',
//     makesound: function() {
//         console.log(`${this.name} издает звук ${this.sound}`)
//     }
// }

// lion.makesound();
// elephant.makesound();

// class Animal {
//     constructor(name, sound) {
//         this.name = name;
//         this.sound = sound;
//     }

//     makeSound() {
//         console.log(`${this.name} издает звук ${this.sound}`)
//     }
// }

// const simba = new Animal('Симба', 'р-р-р');
// const dumbo = new Animal('Дамбо', 'тууууу-тууууу');

// simba.makeSound();
// dumbo.makeSound();


// class Car {
//     constructor(brand, model, year) {
//         this.brand = brand;
//         this.model = model;
//         this.year = year;
//         this.mileage = 0;
//     }

//     drive(distance) {
//         this.mileage += distance;
//         console.log(`${this.brand} ${this.model} проехал ${distance} км. Общий пробег: ${this.mileage} км.`)
//     }    
// }

// const MyCar = new Car('Toyota', 'Corolla', 2020)
// MyCar.drive(50)
// MyCar.drive(100)

// class ElectricCar extends Car {
//     constructor(brand, model, year, batteryCapacity) {
//         super(brand, model, year);
//         this.batteryCapacity = batteryCapacity;
//         this.batteryLevel = 50;
//     }

//     charge(amount) {
//         this.batteryLevel = Math.min(this.batteryLevel + amount, 100);
//         console.log(`${this.brand} ${this.model} заряжен на ${this.batteryLevel}%`)
//     }
// }

// const MyElectricCar = new ElectricCar('Tesla', 'Model Y', 2021, 50000);
// MyElectricCar.drive(50);
// MyElectricCar.drive(200);
// MyElectricCar.charge(20);
// MyElectricCar.charge(100);


class Timer {
    constructor() {
        this.hoursinput = document.getElementById('hours');
        this.minutesinput = document.getElementById('minutes');
        this.secondsinput = document.getElementById('seconds');
        this.display = document.getElementById('timer-display');
        this.startButton = document.getElementById('start-button');
        this.intervalid = null;


        this.startButton.addEventListener('click', () => {
            this.startTimer();
        })
    }

    startTimer() {
        let totalSeconds = parseInt(this.hoursinput.value || 0) * 3600 + parseInt(this.minutesinput.value || 0)*60 + parseInt(this.secondsinput.value || 0);
        console.log(totalSeconds);

        if (totalSeconds <= 0) {
            alert("Укажите число больше 0 секунд")
            return;
        }

        this.updateDisplay(totalSeconds);


        this.intervalid = setInterval(() => {
            totalSeconds--;
            this.updateDisplay(totalSeconds);

            if (totalSeconds <= 0) {
                clearInterval(this.intervalid);
            }
        }, 1000);

    }

    updateDisplay(totalSeconds) {
        const hours = Math.floor(totalSeconds/3600);
        const minutes = Math.floor((totalSeconds % 3600) / 60);
        const seconds = totalSeconds % 60;

        this.display.textContent = String(hours).padStart(2, '0') + ':' +
        String(minutes).padStart(2, '0') + ':' +
        String(seconds).padStart(2, '0');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new Timer();
})

