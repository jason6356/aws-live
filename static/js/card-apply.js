//Get the card list
const cards = document.querySelectorAll(".card")

//Add event listener to each card
cards.forEach((card) => {
  const cardButton = card.querySelector("button")
  card.addEventListener("click", () => {
    const id = card.getAttribute("id")
    console.log("Sending id : ", id)
    //Send a post request to the server
    const xhr = new XMLHttpRequest()
    xhr.open("POST", "/student/apply")
    const formData = new FormData()
    formData.append("id", id)
    xhr.onload = function () {
      if (this.status === 200) {
        alert("Successfully Applied")
        location.reload()
      } else {
        alert("Failed")
      }
    }
    xhr.send(formData)
  })
})
