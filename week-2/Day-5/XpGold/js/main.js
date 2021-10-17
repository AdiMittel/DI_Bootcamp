let calculator = []

function number(num){
    num = parseInt(num)
    calculator.push(num)
    return calculator
}

function operator(oper){
    parseInt(oper)
    calculator.push(oper)
    return calculator
}

function equal() {
    let equation = calculator.join('')
    console.log(equation);
}