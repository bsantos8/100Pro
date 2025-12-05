function alertar() {
    alert("OLA!")
}

//variavel botao que armazena o id botaoe dentro dele o que se quer fazer
let botao = document.querySelector("#botao")


botao.addEventListener("click", () => {
    alertar()
})

//armazenar o input
let usdInput = document.querySelector("#usd")
let brlInput = document.querySelector("#brl")

//adicionar ações
usdInput.addEventListener("keyup", () =>
    console.log(usdInput.value) //mostra o que estasendo digitado no console
)

brlInput.addEventListener("keyup", () =>
    console.log("apertou")
)