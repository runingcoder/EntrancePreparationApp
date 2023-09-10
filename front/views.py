from multiprocessing import context
import pdb
from django.http import HttpResponse
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
import csv


from django.db import transaction


# def import_data(request):
#     # Specify the path to your CSV file
#     csv_file_path = "/home/achyut42/Desktop/minorProject/csv/front_mocktest.csv"

#     with open(csv_file_path, "r") as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             text = row["text"]
#             test_number = int(row["test_number"])
#             mock_test = MockTest(text=text, test_number=test_number)
#             mock_test.save()


#     return HttpResponse("Data imported successfully!")
def import_quiz_data(request):
    # Specify the path to your CSV file
    csv_file_path = "/home/achyut42/Desktop/minorProject/csv/front_quiz.csv"

    with open(csv_file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            quiz = Quiz(
                id=row["id"],
                name=row["name"],
                number_of_questions=row["number_of_questions"],
                time=row["time"],
                required_score_to_pass=row["required_score_to_pass"],
                difficulty=row["difficulty"],
                mock_id=row["mock_id"],
            )
            quiz.save()

    return HttpResponse("Quiz data imported successfully!")


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
        if quizname == "Ran":
            progresschartid = 3
        score = 0
        multiplier = 100 / quiz.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            a_selected = request.POST.get(q.text)
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
        def fetch_subject_results(mock_startswith, subject_name):
            results = Result.objects.filter(
                user_id=request.user.id,
                quiz__mock__text__startswith=mock_startswith,
                quiz__name=subject_name,
            )
            labels = []
            data = []
            count = 0

            for item in results:
                count += 1
                labels.append(count)
                data.append(item.score)

            return {"data": data, "labels": labels, "count": count}

        if pk == "IOE":
            physics_data = fetch_subject_results("IOE", "Physics")
            chemistry_data = fetch_subject_results("IOE", "Chemistry")
            maths_data = fetch_subject_results("IOE", "Maths")
            english_data = fetch_subject_results("IOE", "English")
            aptitude_data = fetch_subject_results("IOE", "Aptitude")

            value = {
                "data": physics_data["data"],
                "labels": physics_data["labels"],
                "data1": chemistry_data["data"],
                "labels1": chemistry_data["labels"],
                "data2": maths_data["data"],
                "labels2": maths_data["labels"],
                "labels3": english_data["labels"],
                "data3": english_data["data"],
                "labels4": aptitude_data["labels"],
                "data4": aptitude_data["data"],
                "count1": physics_data["count"],
                "count2": chemistry_data["count"],
                "count3": maths_data["count"],
                "count4": english_data["count"],
                "count5": aptitude_data["count"],
            }
            return Response(value)

        if pk == "IOM":
            physics_data = fetch_subject_results("IOM", "Physics")
            chemistry_data = fetch_subject_results("IOM", "Chemistry")
            zoology_data = fetch_subject_results("IOM", "Zoology")
            botany_data = fetch_subject_results("IOM", "Botany")

            value = {
                "data5": physics_data["data"],
                "labels5": physics_data["labels"],
                "data6": chemistry_data["data"],
                "labels6": chemistry_data["labels"],
                "data7": zoology_data["data"],
                "labels7": zoology_data["labels"],
                "labels8": botany_data["labels"],
                "data8": botany_data["data"],
                "count5": physics_data["count"],
                "count6": chemistry_data["count"],
                "count7": zoology_data["count"],
                "count8": botany_data["count"],
            }
            return Response(value)

        if pk == "GK":
            subjects = ["General knowledge", "Books", "Science And Nature", "Geography"]
            data_dict = {}

            for i, subject in enumerate(subjects):
                subject_data = fetch_subject_results("Ran", subject)
                data_dict[f"data{i + 9}"] = subject_data["data"]
                data_dict[f"labels{i + 9}"] = subject_data["labels"]
                data_dict[f"count{i + 9}"] = subject_data["count"]

            return Response(data_dict)


def progressChart(request, pk):
    if pk == 1:
        return render(request, "progress_chart_IOE.html")
    if pk == 2:
        return render(request, "progress_chart_IOM.html")
    if pk == 3:
        return render(request, "progress_chart_GK.html")


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
