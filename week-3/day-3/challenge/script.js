let keyValue = document.getElementById('input')
let invalidKeys = [1,2,3,4,5,6,7,8,9,0]
let i = 0
function hideNumbers(event) {
    return /[a-z]/i.test(event.key)
}

keyValue.addEventListener('keyup',hideNumbers())