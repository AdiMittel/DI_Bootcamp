function readUserNumber(){
    let startNum =+prompt('Enter a number')
    return startNum 
}

createSong()
function createSong(){
    let num = readUserNumber()
    let subtracer = 1
    do {
        if(subtracer === 1){
            console.log(`${num} bottles of beer on the wall,\n${num} bottles of beer. ${subtracer} down and pass it around,\n${num-=subtracer} bottles of beer on the wall.`);
            subtracer++
        }
        else{
            if (num - subtracer < 0) {
                break
            }else{
                console.log(`${num} bottles of beer on the wall,\n${num} bottles of beer.Take ${subtracer} down and pass them around,\n${num-=subtracer} bottles of beer on the wall.`);
                subtracer++
            }
        }

    } while (num > 0);
}