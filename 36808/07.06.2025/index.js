function sale(originalPrice, discount) {
    return originalPrice * (1-discount/100)
}

let price = sale(1000, 10)
alert(price)