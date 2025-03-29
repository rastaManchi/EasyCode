// function rectangle_area(width, height) {
//     let result = width * height
//     console.log(result)
// }
// function calculateTriangleArea(base, height){
//     return 0.5 * base * height;
// }
// function calculateCircleArea(radius) {
//     return Math.PI * radius * radius;
// }


// rectangle_area(5, 10)
// rectangle_area(10, 10)
// let rei_result = calculateTriangleArea(1, 10)
// let circle_result = calculateCircleArea(5)
// console.log(rei_result)
// console.log(circle_result)


// console.log(8%2==0)


// function ischetnoe(number) {
//     if (number%2==0) {
//         return 'четное'
//     }
//     else {
//         return 'нечетное'
//     }
// }

// console.log(ischetnoe(21))
 

function a(price, sale) {
    return price*(1-sale/100)
}
console.log(a(100, 15))

const input = document.getElementById('calc')
input.addEventListener('input', function () {
    alert('Не вводи ')
})


function calculateDiscountedPrice(originalPrice, discountPercentage) {
    const discountAmount = (originalPrice * discountPercentage) / 100;
    const discountedPrice = originalPrice - discountAmount;
    return discountedPrice;
}
