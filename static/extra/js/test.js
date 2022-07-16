console.log('Test is working')
const saveBtn = document.getElementById('button-to-save')
const testForm = document.getElementById('test-form')
const elements = [...document.getElementsByClassName('answer')]
const time = testForm.getAttribute('time-data')
const course_id = testForm.getAttribute('data-course-id')
const section_id = testForm.getAttribute('data-section-id')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const url = window.window.location.href
console.log(time)

const pk = testForm.getAttribute('data-test-id')
const new_url = url.slice(0, url.indexOf('/test')) + '/score/' + pk 

const activateTimer = (time) =>{
    console.log(time)


    let minutes = time-1
    let seconds = 60
    let displaySeconds
    let displayMinutes

    const timer = setInterval(()=>{
        seconds --
        if (seconds<0){
            seconds = 59
            minutes --
        }
        if (minutes.toString().length < 2){
            displayMinutes = '0'+minutes
        }
        else{
            displayMinutes = minutes
        }
        if (seconds.toString().length < 2){
            displaySeconds = '0'+seconds
        }
        else{
            displaySeconds = seconds
        }
        if (minutes===0 && seconds===0){
            console.log("Time is Up")
            clearInterval(timer)
            alert("Time is Up")
            sendData()
            window.location.href = new_url
        }
    }, 1000)
}


$.ajax({
    type: 'GET', 
    url : url,
    success: function(response){
        console.log("Ajax ishlayabdi")
        if (time > 0){
            activateTimer(time)
            }   
    },
    error: function(error){
        console.log(error)
    }
})


const sendData = () => {
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el=>{
        if (el.checked){
            data[el.name] = el.value
        }
        else{
            if (!data[el.name]){
                data[el.name] = null
            }
        }
    })
    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function(response){
            console.log('Sended')
        },
        error: function(error){
            console.log('error: ', error)
        }
    })
}


testForm.addEventListener('submit', e=>{
    e.preventDefault()

    sendData()
    window.location.href = new_url
})     


saveBtn.addEventListener('submit', e=>{
    e.preventDefault()
    sendData()
    window.location.href = new_url
})