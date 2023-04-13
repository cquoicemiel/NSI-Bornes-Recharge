const freeButton = document.getElementById("free")
const chargedButton = document.getElementById("charged")
const map = document.getElementById("map")
const amount = document.getElementById("amount")
const type = document.getElementById("type")

const totalStations = 21
const freeStations = 7
const chargedStations = 14

amount.textContent = totalStations.toString()

freeButton.addEventListener("click", () => {
    chargedButton.classList.remove("active")
    if(freeButton.classList.contains("active")){
        freeButton.classList.remove("active")
        map.src = "./carte.html"
        amount.textContent = totalStations.toString()
        type.textContent = ""
    }else{
        freeButton.classList.add("active")
        map.src = "./carte_free.html"
        amount.textContent = freeStations.toString()
        type.textContent = "gratuites"
    }
})
chargedButton.addEventListener("click", () => {
    freeButton.classList.remove("active")
    if(chargedButton.classList.contains("active")){
        chargedButton.classList.remove("active")
        map.src = "./carte.html"
        amount.textContent = totalStations.toString()
        type.textContent = ""
    }else{
        chargedButton.classList.add("active")
        map.src = "./carte_charged.html"
        amount.textContent = chargedStations.toString()
        type.textContent = "payantes"
    }
})


