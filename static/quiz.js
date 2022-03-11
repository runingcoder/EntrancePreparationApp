    const url = window.location.href
    const quizBox = document.getElementById('quiz-box')
    const scoreBox = document.getElementById('score-box')
    const resultBox = document.getElementById('result-box')
    const timerBox = document.getElementById('timer-box')
    const activateTimer = (time) => {
        if (time.toString().length < 2) {
            timerBox.innerHTML = `<b>0${time}:00</b>`
        } else {
            timerBox.innerHTML = `<b>${time}:00</b>`
        }

        let minutes = time - 1
        let seconds = 60
        let displaySeconds
        let displayMinutes

        const timer = setInterval(() => {
            seconds--
            if (seconds < 0) {
                seconds = 59
                minutes--
            }
            if (minutes.toString().length < 2) {
                displayMinutes = '0' + minutes
            } else {
                displayMinutes = minutes
            }
            if (seconds.toString().length < 2) {
                displaySeconds = '0' + seconds
            } else {
                displaySeconds = seconds
            }
            if (minutes === 0 && seconds === 0) {
                timerBox.innerHTML = "<b>00:00</b>"
                setTimeout(() => {
                    clearInterval(timer)
                    alert('Time over')
                    sendData()
                }, 500)
            }
            if (quizForm.hidden == true) {
                clearInterval(timer)

            }

            timerBox.innerHTML = ` Remaining Time:: <b>${displayMinutes}:${displaySeconds}</b>`
        }, 1000)
    }
    let data
    $.ajax({
            type: 'GET',
            url: `${url}/data`,
            success: function(response) {
                console.log(response)
                data = response.data
                data.forEach(el => {
                    for (const [question, answers] of Object.entries(el)) {
                        //pretty useful code
                        quizBox.innerHTML += `
<hr>
<div class ='mb-3

'>
<b>${question}</b>
</div>`
                        answers.forEach(answer => {
                            quizBox.innerHTML += `

<div>
<input  type ='radio' class ='ans' id = '${question}-${answer}' name ='${question}' value='${answer}'>

<label for='${question}'>${answer}</label>
</div>
<style>

div.mb-3{
    margin-left:30px;
font-size:1.4rem;}
input[type=radio] {
    margin-left:60px;
    height:20px;
    width:20px;
}

</style>

`
                        })
                    }
                });
                activateTimer(response.time)
            },
            error: function(error) {
                console.log(error)
            }
        })
        // for submit button response, the following code exists
    const quizForm = document.getElementById('quiz-form')
    const csrf = document.getElementsByName('csrfmiddlewaretoken')
    const sendData = () => {
        const elements = [...document.getElementsByClassName('ans')]

        const data = {}
        data['csrfmiddlewaretoken'] = csrf[0].value,
            elements.forEach(el => {
                if (el.checked) {
                    data[el.name] = el.value
                } else {
                    if (!data[el.name]) {
                        data[el.name] = null
                    }
                }
            });
        $.ajax({
            type: 'POST',
            url: `${url}/save`,
            data: data,
            success: function(response) {
                const results = response.results
                console.log(response)
                console.log(results)

                console.log(results)

                console.log(results)


                quizForm.hidden = true;


                scoreBox.innerHTML = `"<span class="d-inline-block text-truncate" style='font-size:40px;color:blue;font-weight:bold;margin-left:25%;padding-bottom:50px'>
    ${response.passed? 'Braviii! ' : ' Oops! '}Your result is ${response.score.toFixed(2)} %</span>`



                results.forEach(res => {
                    const resDiv = document.createElement("div")
                    for (const [question, resp] of Object.entries(res)) {

                        resDiv.innerHTML += question
                        const cls = ['container', 'p-3', 'text-light', 'h6']
                        resDiv.classList.add(...cls)

                        if (resp == 'not answered') {
                            resDiv.innerHTML += '- not answered'
                            resDiv.classList.add('bg-danger')
                        } else {
                            const answer = resp['answered']
                            const correct = resp['correct_answer']

                            if (answer == correct) {
                                resDiv.classList.add('bg-success')
                                resDiv.innerHTML += ` answered: ${answer}`
                            } else {
                                resDiv.classList.add('bg-danger')
                                resDiv.innerHTML += ` | correct answer: ${correct}`
                                resDiv.innerHTML += ` | answered: ${answer}`
                            }
                        }
                    }
                    resultBox.append(resDiv)

                })

            },
            error: function(error) {
                console.log(error)
            }
        })
    }

    quizForm.addEventListener('submit', e => {
        e.preventDefault()

        sendData()
    })



