// let knight = ['Sir Lancelot', 100, 50, ['sword', 'shield']];
// let mage = ['Gandalf', 80, 120, ['staff', 'spell book']];


// let knight = {
//     name: 'Sir Lancelot',
//     health: 100,
//     strength: 50,
//     inventory: ['sword', 'shield']
// };

// let mage = {
//     name: 'Gandalf',
//     health: 80,
//     mana: 120,
//     inventory: ['staff', 'spell book']
// };


let developerCard = {}

developerCard.name = "Bulat";
developerCard.age = 23;
developerCard.position = "Frontend Developer";
developerCard.department = "Web Development";
developerCard.email = "alice.johnson@company.com";
developerCard.phone = "+1-555-1234";

developerCard.skills = ["Kali", "Python", "Django", "JS"]
developerCard.experience = [
    { company: "Tech Solutions", role: "Junior Developer", years: 2 },
    { company: "Web Innovators", role: "Developer", years: 3 }
];

developerCard.skills.push("C#")

for (let i in developerCard) {
    console.log(`${i} - ${developerCard[i]}`)
}