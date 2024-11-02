
let  player = {}

player.name = "Булат";
player.age = 22;
player.position = "Holl";
player.departament = "Web deportament";

player.skills = ["JavaScript", "React", "CSS", "HTML"];
player.expirience = [
    {company: "NameCompany1", role: "...", years: 2},
    {company: "NameCompany2", role: "...", years: 3}
]

player.skills.push("NewSkill");
console.log(player);

delete player.expirience[0];
console.log(player);

for (let key in player) {
    console.log(`${key}-------${player[key]}`);
}



const dictionary = {
    'привет':'hello',
    'мир':'world'
}

function translate(word) {
    return dictionary[word];
}

console.log(translate('привет'));
console.log(translate('мир'))
