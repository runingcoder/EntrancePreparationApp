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
    let counter = 0;	
    let data
    $.ajax({
            type: 'GET',
            url: `${url}/data`,
            success: function(response) {
                console.log(response)
                data = response.data
                var myList = '<ul>';
                data.forEach(el => {
                    for (const [question, answers] of Object.entries(el)) {
                        counter++;
                        //pretty useful code
                        quizBox.innerHTML += `
                        
<div class ='mb-3'>
<b class="h5">${counter}. ${question}</b>	
</div>`
                        answers.forEach(answer => {
                            quizBox.innerHTML += `


<div>
<input  type ='radio' class ='ans form-check-input' id = '${question}-${answer}' name ='${question}' value='${answer}'>

<label  class ='form-check-label' for='${question}'>${answer}</label>

</div>

<style>

div.mb-3{
font-size:1.4rem;}

input[type=radio] {
    height:20px;
    width:20px;
    margin-left:18px;
}


</style>
<br>
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
                const pc = response.pc
                const quizname = response.quizname                
                const results = response.results
                quizForm.hidden = true;
                scoreBox.innerHTML = `<span class="d-inline-block" style='font-size:40px;margin-left:15%;padding-bottom:50px'>
    ${response.passed? 'Braviii! ' : ' Oops! '}Your result is ${response.score.toFixed(2)} % <br> See the progress chart of ${quizname} here: <button type="button" id="start1-button" class="btn btn-secondary">Results</button> </span> `
    const startBtn1 = document.getElementById('start1-button')
    startBtn1.addEventListener(
        'click', () => {
            location.replace("http://127.0.0.1:8000/progress_chart/" + pc)
        })

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



