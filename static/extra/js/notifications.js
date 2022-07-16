// console.log('Notifications is working')
// const ads_id = [...document.getElementsByClassName('note')]
// const markBtn = document.getElementById('mark-read-all-btn')
// const url = window.location.href
// // + 'ads/' + 'mark_read_all/'
// const new_url = url.slice(0, url.indexOf('/'))

// const new_path = ''
// s_url = url.split('/')
// const current_url = ''

// console.log(typeof current_url)
// console.log(typeof s_url[2])
// const string = "My string is here"
// console.log(typeof string[4])
// for (let i = 0; i < s_url.length; i++) {
//     if (i >=2) {
//         console.log(s_url[i])
//     }
//     else{
//         console.log(s_url[i])
//         new_path = new_path + s_url[i]
//     }
// }

// console.log(url)
// console.log(new_url)
// console.log('new_path: ', new_path)
// const sendData = () => {
//     const data = {}
//     data['path'] = url
//     // var numb = 0
//     // ads_id.forEach(ad=>{
//     //     numb++
//     //     data[`key${numb}`] = ad
//     // })
//     $.ajax({
//         type: 'GET',
//         url: new_url,
//         data: data,
//         cache: false,
//         // contentType: false,
//         // The following is necessary so jQuery won't try to convert the object into a string
//         processData: false,
//         success: function(response){
//             console.log('Sended: ', data)
//         },
//         error: function(error){
//             console.log('error: ', error)
//         }
//     })
// }

// markBtn.addEventListener('click', e=>{
//     e.preventDefault()
//     sendData()
// })