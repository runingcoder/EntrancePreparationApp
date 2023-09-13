function randomArrayShuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;
    while (0 !== currentIndex) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }
    return array;
}
function myFunction() {
    document.getElementById("fixedsidebar").style.display = "none";
}
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
    success: function (response) {
        data = response.data;
        var myList = '<ul>';
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)) {
                counter++;
                // Pretty useful code
                quizBox.innerHTML += `                    
                    <div class='mb-3'>
                        <b class="h5">${counter}. ${question}</b>
                    </div>`;

                randomArrayShuffle(answers);
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                        <div>
                            <input type='radio' class='ans form-check-input' id='${question}-${answer}' name='${question}' value='${answer}'>
                            <label class='form-check-label' for='${question}'>${answer}</label>
                        </div>
                        <style>
                            div.mb-3 {
                                font-size: 1.4rem;
                            }
                            input[type=radio] {
                                height: 20px;
                                width: 20px;
                                margin-left: 18px;
                            }
                        </style>
                        <br>`;
                });
            }
        });
        activateTimer(response.time);
    },
    error: function (error) {
        console.log(error);
    }
});

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


    const currentUrl = new URL(window.location.href);
    const baseUrl = currentUrl.protocol + "//" + currentUrl.hostname + (currentUrl.port ? ':' + currentUrl.port : '');
    async function postData() {
        try {
            let response = await $.ajax({
                type: 'POST',
                url: `${url}/save`,
                data: data
            });

            console.log("successfully retrieved response to a new page. Result id is ", response.resultID)
            const resultID = response.resultID
            const newUrl = new URL('viewResult/' + resultID, baseUrl);
            window.location.href = newUrl;
        } catch (error) {
            console.log(error)
        }
    }

    postData();
}



quizForm.addEventListener('submit', e => {
    e.preventDefault()

    sendData()
})



