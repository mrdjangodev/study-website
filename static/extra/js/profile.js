const form = document.getElementById('profile-edit-form')
// 
// last-name-id
// username-id
const imgBox = document.getElementById('image-box')
const image = document.getElementById('image')

const csrf = document.getElementsByName('csrfmiddlewaretoken')
const first_name = document.getElementById('first-name-id')
const last_name = document.getElementById('last-name-id')
const user_name = document.getElementById('username-id')
const bio = document.getElementById('bio-id')
const phone = document.getElementById('phone-id')
const url = window.window.location.href

console.log("profile.js is working")

image.addEventListener('change', ()=>{
    const image_data = image.files[0]
    const url_image = URL.createObjectURL(image_data)
    console.log(url_image)
    imgBox.innerHTML = `<img src="${url_image}" >`
})

form.addEventListener('submit', (e)=>{
    e.preventDefault()
    
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('first_name', first_name.value)
    fd.append('last_name', last_name.value)
    fd.append('user_name', user_name.value)
    fd.append('bio', bio.value)
    fd.append('phone_number', phone.value)

    fd.append('image', $('#image')[0].files[0])
    const new_url = url.slice(0, url.indexOf('accounts/')+('accounts/').length) + 'change_user_info/'
   
    $.ajax({
        cache: false,
        contentType: false,
        // The following is necessary so jQuery won't try to convert the object into a string
        processData: false,
        type: 'POST',
        url: new_url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function(response){
            console.log(response)
        },
        error: function(error){
            console.log(error)
        }
    });
})