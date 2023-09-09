from multiprocessing import context
import pdb
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from rest_framework.views import APIView
from django.views.generic.list import ListView
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.http.response import JsonResponse
from .forms import CaptchaTestForm, CreateUserForm
import requests
from decouple import config
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url


from django.db import transaction


def ajax_refresh_captcha(request):
    to_json_response = dict()
    to_json_response["new_cptch_key"] = CaptchaStore.generate_key()
    to_json_response["new_cptch_image"] = captcha_image_url(
        to_json_response["new_cptch_key"]
    )
    return JsonResponse(to_json_response)


@transaction.atomic
def getapi(request):
    response = requests.get(
        "https://opentdb.com/api.php?amount=50&category=22&difficulty=medium&type=multiple"
    )
    for ques in response.json()["results"]:
        question = Question.objects.create(text=ques["question"], quiz_id="12")
        Answer.objects.create(
            text=ques["correct_answer"], correct=1, question_id=question.id
        )
        for ans in ques["incorrect_answers"]:
            Answer.objects.create(text=ans, correct=0, question_id=question.id)
    return JsonResponse({"message": "sucessfully imported"})


def index1(request):
    return render(request, "index1.html")


def index(request):
    return render(request, "index.html")


def reading_material(request):
    return render(request, "reading_materials.html")


def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account successfully created for " + username)

            return redirect("login")

    context = {"form": form}
    return render(request, "register.html", context)


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # yo get gareko, is associated with the name in the form that is posted/submitted(in the login)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")

    context = {}
    return render(request, "login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("login")


def terms(request):
    return render(request, "terms.html")


def privacy(request):
    return render(request, "privacy.html")


def services(request):
    return render(request, "services.html")


def about(request):
    return render(request, "about.html")


@login_required(login_url="login")
def send_email_contact(request):
    # this feature doesn't work because Google disbaled the access for less secure apps on May 30th, 2022.
    form = CaptchaTestForm(request.POST)
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.user.email
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        if form.is_valid():
            print("Captcha validation success")
            data = {
                "name": name,
                "email": email,
                "subject": subject,
                "message": message,
            }
            message = """ New message: {} 
            From: {}
            
            """.format(
                data["subject"], data["email"]
            )

            send_mail(data["message"], message, "", [config("EMAIL_RECEPIENT_USER")])
            messages.success(
                request,
                "Message succesfully sent. We will reach out to you as soon as possible! ",
            )
        else:
            print("Captcha validation failed")
            messages.error(request, "Message not sent due to captcha error")

    return render(request, "contact.html", {"form": form})


# stuff related with is_ajax deprecated and hence, used an alternative solution,
# and don't rely on Chatgpt for these things, just search stackoverflow as it only has code till 2021.
def is_ajax(request):
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


@login_required(login_url="login")
def save_quiz_view(request, pk):
    if is_ajax(request=request):
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop("csrfmiddlewaretoken")

        for k in data_.keys():
            question = Question.objects.filter(text=k).first()
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        quizn = quiz.mock.text
        quizname = str(quizn[:3])
        if quizname == "IOE":
            progresschartid = 1
        if quizname == "IOM":
            progresschartid = 2
        # if quizname == "GK":
        #     progresschartid =3
        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)
            # import pdb
            # pdb.set_trace()

            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append(
                    {str(q): {"correct_answer": correct_answer, "answered": a_selected}}
                )
            else:
                results.append({str(q): "not answered"})

        score_ = score * multiplier
        Result.objects.create(quiz=quiz, user=user, score=score_)

        if score_ >= quiz.required_score_to_pass:
            return JsonResponse(
                {
                    "passed": True,
                    "score": score_,
                    "results": results,
                    "quizname": quizname,
                    "pc": progresschartid,
                }
            )
        else:
            return JsonResponse(
                {
                    "passed": False,
                    "score": score_,
                    "results": results,
                    "quizname": quizname,
                    "pc": progresschartid,
                }
            )


class ChartData(APIView):
    def get(self, request, pk=None):
        if pk == "IOE":
            result_physics = Result.objects.filter(
                user_id=request.user.id,
                quiz__mock__text__startswith="IOE",
                quiz__name="Physics",
            )
            result_chemistry = Result.objects.filter(
                user_id=request.user.id,
                quiz__mock__text__startswith="IOE",
                quiz__name="Chemistry",
            )
            result_maths = Result.objects.filter(
                user_id=request.user.id,
                quiz__mock__text__startswith="IOE",
                quiz__name="Maths",
            )
            result_english = Result.objects.filter(
                user_id=request.user.id,
                quiz__mock__text__startswith="IOE",
                quiz__name="English",
            )
            result_aptitude = Result.objects.filter(
                user_id=request.user.id,
                quiz__mock__text__startswith="IOE",
                quiz__name="Aptitude",
            )

            labels = []
            data = []
            labels1 = []
            data1 = []
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            count5 = 0
            data2 = []
            labels2 = []
            labels3 = []
            data3 = []
            labels4 = []
            data4 = []

            for item in result_physics:
                count1 += 1
                labels.append(count1)
                data.append(item.score)

            for item in result_chemistry:
                count2 += 1
                labels1.append(count2)
                data1.append(item.score)
            for item in result_maths:
                count3 += 1
                labels2.append(count3)
                data2.append(item.score)
            for item in result_english:
                count4 += 1
                labels3.append(count4)
                data3.append(item.score)
            for item in result_aptitude:
                count5 += 1
                labels4.append(count5)
                data4.append(item.score)

            value = {
                "data": data,
                "labels": labels,
                "data1": data1,
                "labels1": labels1,
                "data2": data2,
                "labels2": labels2,
                "labels3": labels3,
                "data3": data3,
                "labels4": labels4,
                "data4": data4,
            }
            return Response(value)
        if pk == "IOM":
            result_physics = Result.objects.filter(
                user_id=request.user.id,
                quiz__mock__text__startswith="IOM",
                quiz__name="Physics",
            )
            result_chemistry = Result.objects.filter(
                user_id=request.user.id,
                quiz__mock__text__startswith="IOM",
                quiz__name="Chemistry",
            )
            result_zoology = Result.objects.filter(
                user_id=request.user.id,
                quiz__mock__text__startswith="IOM",
                quiz__name="Zoology",
            )
            result_botany = Result.objects.filter(
                user_id=request.user.id,
                quiz__mock__text__startswith="IOM",
                quiz__name="Botany",
            )

            labels5 = []
            data5 = []
            labels6 = []
            data6 = []
            count5 = 0
            count6 = 0
            count7 = 0
            count8 = 0

            data7 = []
            labels7 = []
            labels8 = []
            data8 = []

            for item in result_physics:
                count5 += 1
                labels5.append(count5)
                data5.append(item.score)

            for item in result_chemistry:
                count6 += 1
                labels6.append(count6)
                data6.append(item.score)
            for item in result_zoology:
                count7 += 1
                labels7.append(count7)
                data7.append(item.score)
            for item in result_botany:
                count8 += 1
                labels8.append(count8)
                data8.append(item.score)

            value = {
                "data5": data5,
                "labels5": labels5,
                "data6": data6,
                "labels6": labels6,
                "data7": data7,
                "labels7": labels7,
                "labels8": labels8,
                "data8": data8,
            }
            return Response(value)


def progressChart(request, pk):
    if pk == 1:
        return render(request, "progress_chart_IOE.html")
    if pk == 2:
        return render(request, "progress_chart_IOM.html")


def ioe_page(request, pk):
    mock = MockTest.objects.filter(text__startswith=pk[:3])
    context = {"mock": mock}
    return render(request, "ioe_page.html", context)


def random_page(request, pk):
    mock = MockTest.objects.get(text=pk)

    context = {"mock": mock}
    return render(request, "random_page.html", context)


def iom_page(request, pk):
    mock = MockTest.objects.filter(text__startswith=pk[:3])
    context = {"mock": mock}
    return render(request, "iom_page.html", context)


@login_required(login_url="login")
def mocktest(request):
    mock = MockTest.objects.distinct("text")

    context = {"mock": mock}
    return render(request, "mock_test.html", context)


def ioe_quizlist(request, pk):
    quiz = Quiz.objects.filter(mock_id=pk)
    return render(request, "ioe_quiz.html", {"quiz": quiz})


def iom_quizlist(request, pk):
    quiz = Quiz.objects.filter(mock_id=pk)
    return render(request, "iom_quiz.html", {"quiz": quiz})


def random_quizlist(request, pk):
    quiz = Quiz.objects.filter(mock_id=pk)
    return render(request, "random_quiz.html", {"quiz": quiz})


@login_required(login_url="login")
def quizview(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    context = {"quiz": quiz}
    return render(request, "quiz_view.html", context)


@login_required(login_url="login")
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    questions = []
    for q in quiz.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse(
        {
            "data": questions,
            "time": quiz.time,
        }
    )
