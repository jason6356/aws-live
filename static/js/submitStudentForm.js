//Write a function that will get form data and submit as a POST request to /registerStudent
//if success then we will get a alert saying "Successfully Registered"
//if failed then we will get a alert saying "Failed"
function registerStudent() {
  var xhr = new XMLHttpRequest()
  xhr.open("POST", "/student/register")
  const formData = new FormData()
  formData.append("student_id", student_id)
  xhr.onload = function () {
    if (this.status === 200) {
      alert("Successfully Deleted")
      location.reload()
    } else {
      alert("Failed")
    }
  }
  xhr.send(formData)
}
