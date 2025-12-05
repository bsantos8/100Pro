//valor dolar em 12/2025
let dollar = 5.34

let usdInput = document.querySelector("#usd")
let brlInput = document.querySelector("#brl")

usdInput.addEventListener("input", function() {
    let usd = parseFloat(usdInput.value)
    let brl = usd * dollar
    if (isNaN(brl)) {
        brlInput.value = ""
        return
    }
    brlInput.value = brl.toFixed(2)
})

brlInput.addEventListener("input", function() {
    let brl = parseFloat(brlInput.value)
    let usd = brl / dollar
    if (isNaN(usd)) {
        usdInput.value = ""
        return
    }
    usdInput.value = usd.toFixed(2)
})

usdInput.value = "1.00" 
usdInput.dispatchEvent(new Event("input"))


