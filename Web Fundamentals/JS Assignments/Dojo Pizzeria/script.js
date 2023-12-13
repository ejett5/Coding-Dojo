//global imports
Math.random


function pizzaOven(crustType, sauceType, cheeses, toppings){
    var pizza = {};
    pizza.crustType = crustType;
    pizza.toppings = toppings;
    pizza.cheeses = cheeses;
    pizza.sauceType = sauceType;
    return pizza;

}

var p1 = pizzaOven("thin", "[pepperoni, peppers, bacon]", "mozarella", "tomato basil");
console.log(p1)

var p2 = pizzaOven("deep dish", "[pepperoni, sausage]", "mozarella", "traditional");
console.log(p2)

var p3 = pizzaOven("hand tossed", "[mushrooms, olives, onions]", "[mozarella, feta]", "marinara");
console.log(p3)