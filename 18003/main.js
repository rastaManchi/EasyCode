
// let  player = {}

// player.name = "Булат";
// player.age = 22;
// player.position = "Holl";
// player.departament = "Web deportament";

// player.skills = ["JavaScript", "React", "CSS", "HTML"];
// player.expirience = [
//     {company: "NameCompany1", role: "...", years: 2},
//     {company: "NameCompany2", role: "...", years: 3}
// ]

// player.skills.push("NewSkill");
// console.log(player);

// delete player.expirience[0];
// console.log(player);

// for (let key in player) {
//     console.log(`${key}-------${player[key]}`);
// }



// const dictionary = {
//     'привет':'hello',
//     'мир':'world',
//     'дерево': 'tree'
// }

// function translate(word) {
//     return dictionary[word];
// }

// console.log(translate('привет'));
// console.log(translate('мир'))

const list_dict = [
    {russian: 'Яблоко', english: 'Apple'},
    {russian: 'Машина', english: 'Car'}
]

let current_word = 0

document.getElementById("english_word").textContent = list_dict[current_word].english

function checkTranslation() {
    let user_input = document.getElementById("userInput").value;
    if (user_input == list_dict[current_word].russian) {
        current_word++;
        document.getElementById("english_word").textContent = list_dict[current_word].english
    }
}