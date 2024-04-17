from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth.models import User
from .models import signin_model
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import date, datetime
from khayyam import JalaliDate, JalaliDatetime, TehranTimezone
import csv
from datetime import date
import random

save_user = False
image_true=False


def home(request):

    return render(request, 'Migration/post/home.html', {'save_user': save_user,'image_true':image_true})


def work(request):
    return render(request, 'Migration/post/work.html', {'save_user': save_user,'image_true':image_true})


def study(request):
    return render(request, 'Migration/post/study.html', {'save_user': save_user,'image_true':image_true})


def life(request):
    return render(request, 'Migration/post/life.html', {'save_user': save_user,'image_true':image_true})


def vissa(request):
    return render(request, 'Migration/post/vissa.html', {'save_user': save_user,'image_true':image_true})


def usa(request):
    return render(request, 'Migration/post/countries/usa.html', {'save_user': save_user,'image_true':image_true})


def germany(request):
    return render(request, 'Migration/post/countries/germany.html', {'save_user': save_user,'image_true':image_true})


def about(request):

    return render(request, 'Migration/post/about.html', {'save_user': save_user,'image_true':image_true})


def feedback(request):
    sent = False
    if request.method == "POST":
        form = feedback_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            emails = cd['email']
            subject = cd['subject']
            message = cd['message']
            phone = cd['phone']
            msg = "name:{0}\nphone:{1}\nemail:{2}\nmessage:\n{3}".format(name, phone, emails, message)
            send_mail(subject, msg, 'lopmotop@gmail.com', ['lopmotop@gmail.com'], fail_silently=False)
            sent = True
    else:
        form = feedback_form()

    return render(request, 'Migration/post/feedback.html', {'save_user': save_user, 'forms': form,'image_true':image_true})


def consulting(request):
    if not save_user:
        return redirect("my_site:signin")
    print('consulting')

    my_range = range(1, 100)
    context = {
        'my_range': my_range
    }

    sent = False
    if request.method == "POST":
        print('e-post')
        form = email_consulting(request.POST)
        if form.is_valid():
            print('e-valid')

            cd = form.cleaned_data
            name = cd['name']
            type_consulting = cd['type_consulting']
            level_school = cd['level_school']
            type = cd['type']
            age = cd['age']
            type_price = cd['type_price']
            mobile = cd['mobile']
            city = cd['city']

            msg = ("name: {0}\nphone: {1}\ncity: {2}\ntype_consulting: {3}"
                   "\nlevel_school: {4}\ntype: {5}"
                   "\ntype_price: {6}\nage {7}").format(
                name, mobile, city, type_consulting, level_school, type, type_price, age)

            send_mail("فرم مشاوره", msg, 'lopmotop@gmail.com',
                      ['lopmotop@gmail.com'], fail_silently=False)
            sent = True
    else:
        print('e-get')

    form = email_consulting()
    return render(request, 'Migration/post/consulting.html',
                  {'save_user': save_user, 'sent': sent, "context": context,'image_true':image_true})


# send_code = 0

code = 0


def Verification_code_view(request):
    # global code
    # import random
    # code = random.randint(100000, 999999)
    # print(code)
    # global send_code
    # import random
    # code = random.randint(100000, 999999)
    # print(code)
    # form=signin_form(request.POST)
    # if form.is_valid():
    #     email=form.cleaned_data['email']
    #     print(email)
    # send_code = True
    # return redirect('my_site:signin')
    return render(request, 'Migration/forms/signin.html')


def signin(request):
    print('yes')
    global code
    global save_user
    if not save_user:
        print('NO save')
        # user = request.user
        # try:
        #     account = signin_model.objects.get(users=user)
        #
        # except:
        #
        if request.method == "POST":
            form = signin_form(request.POST)
            print('post')
            if form.is_valid():
                print('valid-post')
                cd = form.cleaned_data
                if cd['repassword'] == cd["password"]:

                    if cd['code'] == '':
                        print('shet')
                        import random
                        code = random.randint(100000, 999999)
                        print(code)
                        dict_form= [cd['user_name'], cd['first_name'], cd['last_name'], cd['password'], cd['repassword'],
                                    cd['email'], cd['mobile']]

                        send_mail('کد تایید', 'کد تایید شما برای ثبت نام در سایت مهاجر\n' + str(code),
                                  'lopmotop@gmail.com',
                                  [cd['email']],
                                  fail_silently=False)

                        return render(request,'Migration/forms/signin.html',{'form':form,'dict_form':dict_form})
                    else:
                        print("code", code)
                        if str(code) == str(cd['code']):

                            user = User.objects.create_user(cd["user_name"], cd["email"], cd["password"])
                            user.first_name = cd["first_name"]
                            user.last_name = cd["last_name"]
                            account = signin_model.objects.create(users=user)
                            user.first_name = cd['first_name']
                            user.last_name = cd['last_name']
                            account.first_name = cd['first_name']
                            account.last_name = cd['last_name']
                            account.password = cd['password']
                            account.email = cd['email']
                            account.mobile = cd['mobile']
                            account.user_name = cd['user_name']
                            user.save()
                            account.save()
                            save_user = True
                            user = authenticate(request, username=cd["user_name"], password=cd["password"])
                            if user is not None:
                                login(request, user)
                                messages.success(request, "خوش اومدی")  # ایجاد پیام موفقیت
                                return render(request, 'Migration/post/home.html',{'save_user': save_user, 'forms': form,'image_true':image_true})
                        else:
                            messages.error(request, "کد تایید نادرست است")  # ایجاد پیام موفقیت
                            return render(request, 'Migration/post/home.html', {'save_user': save_user, 'forms': form,'image_true':image_true})

#                         # if cd['code'] != '':
#                         #     print('shet')
#                         #     if str(code) == str(cd['code']):
#                         #         print('shetttt')


#
#
#                         # return render(request, 'Migration/forms/signin.html',
#                         #               {'save_user': save_user, 'forms': form, 'account': account})

                    # if str(code)==str(cd['code']):
                    #     user.save()
                    #     account.save()
                    #     save_user = True
                    #     user = authenticate(request, username=cd["user_name"], password=cd["password"])
                    #
                    #     if user is not None:
                    #         login(request, user)
                    #
                    #     return render(request, 'Migration/forms/signin.html', {'save_user': save_user, 'forms': form})
                    # else:
                    #     messages.error(request, "کد تایید نادرست است")  # ایجاد پیام موفقیت
                    #     return render(request, 'Migration/post/home.html', {'save_user': save_user, 'forms': form})

                else:
                    not_correct_password = True
                    return render(request, 'Migration/forms/signin.html',
                    {'save_user': save_user, "not_correct_password": not_correct_password, 'forms': form,'image_true':image_true})
                # else:
                #     return render(request, 'Migration/forms/signin.html', {"forms": form})
            else:
                return render(request, 'Migration/forms/signin.html', {"forms": form,'image_true':image_true})

        else:
            # global send_code
            # if send_code:
            #     import random
            #     code = random.randint(100000, 999999)
            #
            form = signin_form()
            print("get")
            return render(request, 'Migration/forms/signin.html', {"forms": form,'image_true':image_true})
    else:
        return redirect("my_site:consulting")


def view_login(request):
    global save_user
    if request.method == "POST":
        form = login_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # from django.db.models import Q
            #
            # if signin_model.objects.filter(Q(user_name=cd['user_name']) & Q(password=cd['password'])).exists():
            #     print('open')
            user = authenticate(request, username=cd["user_name"], password=cd["password"])
            if user is not None:
                login(request, user)
                save_user = True
                messages.success(request, 'با موق=فقیت وارد شدید.')
                return redirect('my_site:home')
        else:
            messages.error(request, 'یکی از فیلدها نادرست است.')
    else:
        form = login_form()
    return render(request, 'Migration/forms/login.html', {'save_user': save_user, 'forms': form,'image_true':image_true})


def logout_view(request):
    global save_user
    logout(request)
    save_user = False
    return render(request, 'Migration/post/home.html', {'save_user': save_user,'image_true':image_true})


def profile(request):
    if save_user:
        return render(request, 'Migration/post/profile.html', {'save_user': save_user})
    else:
        return render(request, 'Migration/post/home.html', {'save_user': save_user,'image_true':image_true})


def look_profile(request):
    user = request.user
    account = signin_model.objects.get(users=user)
    if save_user:
        return render(request, 'Migration/post/look_profile.html', {'save_user': save_user, 'account': account,'image_true':image_true})
    else:
        return render(request, 'Migration/post/home.html', {'save_user': save_user, 'account': account,'image_true':image_true})


def edit_profile(request):
    user = request.user
    try:
        account = signin_model.objects.get(users=user)

    except:

        account = signin_model.objects.create(users=user)

    if request.method == "POST":
        form = signin_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user.first_name = cd['first_name']
            user.last_name = cd['last_name']
            account.first_name = cd['first_name']
            account.last_name = cd['last_name']
            account.password = cd['password']
            account.email = cd['email']
            account.mobile = cd['mobile']
            account.user_name = cd['user_name']
            account.save()
            user.save()
            user = authenticate(request, user_name=account.user_name, password=account.password)
            if user is not None:
                login(request, user)

            # print("ok")

            return redirect('my_site:home')
        else:
            # print(form.cleaned_data['name'],
            #       form.cleaned_data['last_name'],
            #       form.cleaned_data['address'],
            #       form.cleaned_data['gender'],
            #       )
            return render(request, 'Migration/post/edit_profile.html', {'forms': form, 'account': account,'image_true':image_true})
    else:
        # print("get")
        form = signin_form()
        return render(request, 'Migration/post/edit_profile.html', {'forms': form, 'account': account,'image_true':image_true})


def suggestion(request):
    file_path = r"D:/project/python/Migration/my_site/templates/Migration/post/suggest_data.csv"

    if request.method == "POST":
        form = suggestion_form(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            suggest = cd['suggest']
            name = cd['name']

            now = datetime.now()
            d1 = now.strftime("%H:%M")
            d2 = str(JalaliDate(date(now.year, now.month, now.day)))
            d3 = str(d1) + '  ' + d2

            with open(file_path, "a+", encoding="utf-8") as output:
                output.write(str('\n' + d3 + "," + name + "," + suggest))

            messages.success(request, "پیام شما با موفقیت ثبت شد")  # ایجاد پیام موفقیت

        else:
            messages.error(request, "یکی از فیلد ها نادرست است")
        return redirect('my_site:suggestion')  # برای جلوگیری از ارسال مجدد فرم

    else:
        with open(file_path, encoding="utf-8") as file:
            data = csv.reader(file)
            dt = list(data)
        return render(request, 'Migration/forms/suggestion.html', {'dt': dt,'image_true':image_true})
#
#
# from .forms import UserProfileForm
#
# def upload_photo(request):
#     global image_true
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES)
#         if form.is_valid():
#             image_true=True
#             form.save()
#     else:
#         form = UserProfileForm()
#
#     return render(request, 'Migration/forms/image_profile.html', {'form_image': form,'iamgetrue':image_true})
#
