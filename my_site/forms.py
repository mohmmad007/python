from django import forms


class signin_form(forms.Form):
    user_name = forms.CharField(required=False, label='نام کاربری')
    first_name = forms.CharField(required=False, label='نام')
    last_name = forms.CharField(required=False, label='نام خانوادگی')
    password = forms.CharField(required=False, label='پسوورد')
    repassword = forms.CharField(required=False, label='تکرار پسوورد')
    email = forms.CharField(required=False, label='ایمیل')
    mobile = forms.CharField(required=False, label='شماره موبایل')
    code = forms.CharField(required=False, label='کد تایید')

    def clean_password(self):
        password = self.cleaned_data['password']
        if password:
            if len(password) < 6:
                raise forms.ValidationError(' پسوورد باید حداقل شش کاراکتر باشد')
            elif len(password) > 20:
                raise forms.ValidationError(' پسوورد باید حداکثر بیست کاراکتر باشد')
            else:
                return password
        else:
            raise forms.ValidationError(' پسوورد الزامی است')

    def clean_email(self):
        email = self.cleaned_data['email']
        if email:
            if len(email) > 50:
                raise forms.ValidationError(' ایمیل باید حداکثر پنجاه کاراکتر باشد')
            # if type(email) != forms.EmailField():
            #     raise forms.ValidationError(' ایمیل نادرست است')
            else:
                return email

        else:
            raise forms.ValidationError(' ایمیل الزامی است')

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if first_name:
            if len(first_name) < 6:
                raise forms.ValidationError(' نام باید حداقل شش کاراکتر باشد')
            elif len(first_name) > 20:
                raise forms.ValidationError(' نام باید حداکثر بیست کاراکتر باشد')
            else:
                return first_name

        else:
            raise forms.ValidationError(' نام الزامی است')

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if last_name:
            if len(last_name) < 6:
                raise forms.ValidationError(' نام خانوادگی باید حداقل شش کاراکتر باشد')
            elif len(last_name) > 20:
                raise forms.ValidationError(' نام خانوادگی باید حداکثر بیست کاراکتر باشد')
            else:
                return last_name

        else:
            raise forms.ValidationError(' نام خانوادگی الزامی است')

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        if user_name:
            if len(user_name) < 4:
                raise forms.ValidationError(' نام کاربری باید حداقل چهار کاراکتر باشد')
            elif len(user_name) > 25:
                raise forms.ValidationError(' نام کاربری باید حداکثر بیست و پنج کاراکتر باشد')
            else:
                return user_name
        else:
            raise forms.ValidationError(' نام کاربری الزامی است')

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if mobile:
            # a = str(mobile)
            # if a[0] != '0':
            #     if len(mobile) == 10:
            #         pass
            #         #رقم صفر رو به اول شماره موبایل اضافه کن
            #         #ریترن کن mobile رو
            #     else:
            #         raise forms.ValidationError(' شماره موبایل باید ده رقم باشد')

            # elif len(mobile) != 11:
            #     raise forms.ValidationError(' شماره موبایل باید یازده رقم باشد')
            # else:
            return mobile

        else:
            raise forms.ValidationError(' شماره موبایل الزامی است')

    # def clean(self):
    #     firstname = self.cleaned_data['user_name']
    #     if firstname:
    #         if len(firstname) < 5:
    #             raise forms.ValidationError('نام شما کم است')


#

class email_consulting(forms.Form):
    TYPE_CHOICES = (
        ('حضوری', 'حضوری'),
        ('آنلاین', 'آنلاین'))
    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect, label='نوع مشاوره')
    name = forms.CharField(max_length=20, required=True)
    type_consulting = forms.CharField(required=True, max_length=10, label='نوع مشاوره2')
    city = forms.CharField(max_length=20, required=True)
    mobile = forms.CharField(max_length=20, required=True)
    level_school = forms.CharField(required=True, max_length=10, label='تحصیلات')
    AGE_CHOICES = [(str(i), str(i)) for i in range(1, 100)]
    age = forms.ChoiceField(choices=AGE_CHOICES, widget=forms.Select)
    type_price = forms.CharField(required=True, max_length=10, label='نوع پرداخت')

    def clean_user_name(self):
        user_name = self.cleaned_data['user_name']
        if user_name:
            if len(user_name) < 4:
                raise forms.ValidationError(' نام کاربری باید حداقل شش کاراکتر باشد')


class feedback_form(forms.Form):
    phone = forms.CharField(max_length=11, required=True, label='شماره موبایل')
    email = forms.CharField(required=True, label='ایمیل')
    subject = forms.CharField(required=True, max_length=10, label='موضوغ')
    message = forms.CharField(required=True, label='پیام', widget=forms.Textarea)
    name = forms.CharField(max_length=20, required=True)


class login_form(forms.Form):
    user_name = forms.CharField(max_length=20, required=True, label='نام کاربری')
    password = forms.CharField(max_length=20, required=True, label='پسوورد')


# class CreateForm(forms.Form):
class suggestion_form(forms.Form):
    name = forms.CharField(max_length=20, required=True, label='نام')
    suggest = forms.CharField(max_length=500, required=True, label='نظر')



from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['photo']