"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from app.models import book
from django.template import RequestContext
from django.contrib import auth

from django import forms
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    email = forms.EmailField(label='e-mail',widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'e-mail'}))
    password1 = forms.CharField(label='Password',
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    password2= forms.CharField(label='confirm',
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    book_list_all = book.objects.all()
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'book_list_all':book_list_all,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def register(request):
    if request.method=='POST':
        errors=[]
        form=RegisterForm(request.POST)

        if not form.is_valid():
            return render(request, "app/register.html",{'form':form,'errors':errors})
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password1 = form.cleaned_data['password1']
        password2= form.cleaned_data['password2']
        if password1!=password2:
            errors.append("两次输入的密码不一致!")
            return render(request, "app/register.html",{'form':form,'errors':errors})
        filterResult=User.objects.filter(username=username)
        if len(filterResult)>0:
           errors.append("用户名已存在")
           return render(request, "app/register.html",{'form':form,'errors':errors})
        user = User.objects.create_user(username,email,password1)
        user.save()
        #登录前需要先验证
        newUser=auth.authenticate(username=username,password=password1)
        if newUser is not None:
            auth.login(request, newUser)
            return HttpResponseRedirect("/")
    else:
        form =RegisterForm()
        return render(request, "app/register.html",{'form':form,'title':'注册','year':datetime.now().year})

    return render(request, "app/register.html")


class BookForm_1_dianyuan(forms.Form):
    class_choices = (
        ('高等数学（A）（1）', '高等数学（A）（1）'),
        ('线性代数（B类）', '线性代数（B类）'),
        ('离散数学', '离散数学'),
        ('程序设计思想与方法', '程序设计思想与方法'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_3_dianqi(forms.Form):
    class_choices = (
        ('大学物理（A类）（2）', '大学物理（A类）（2）'),
        ('基本电路理论', '基本电路理论'),
        ('数字电子技术', '数字电子技术'),
        ('数理方法', '数理方法'),
        ('大学物理实验（2）', '大学物理实验（2）'),
        ('基本电路实验', '基本电路实验'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_3_cekong(forms.Form):
    class_choices = (
        ('大学物理（A类）（2）', '大学物理（A类）（2）'),
        ('基本电路理论', '基本电路理论'),
        ('数字电子技术', '数字电子技术'),
        ('数理方法', '数理方法'),
        ('大学物理实验（2）', '大学物理实验（2）'),
        ('基本电路实验', '基本电路实验'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_3_zidonghua(forms.Form):
    class_choices = (
        ('大学物理（A类）（2）', '大学物理（A类）（2）'),
        ('基本电路理论', '基本电路理论'),
        ('数字电子技术', '数字电子技术'),
        ('数理方法', '数理方法'),
        ('大学物理实验（2）', '大学物理实验（2）'),
        ('基本电路实验', '基本电路实验'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_4_dianqi(forms.Form):
    class_choices = (
        ('模拟电子技术', '模拟电子技术'),
        ('嵌入式系统原理与实验（A类）', '嵌入式系统原理与实验（A类）'),
        ('信号与系统（B类)', '信号与系统（B类）'),
        ('电磁场', '电磁场'),
        ('电子技术实验', '电子技术实验'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_4_cekong(forms.Form):
    class_choices = (
        ('模拟电子技术', '模拟电子技术'),
        ('嵌入式系统原理与实验（A类）', '嵌入式系统原理与实验（A类）'),
        ('信号与系统（B类)', '信号与系统（B类）'),
        ('电子技术实验', '电子技术实验'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_4_zidonghua(forms.Form):
    class_choices = (
        ('模拟电子技术', '模拟电子技术'),
        ('嵌入式系统原理与实验（A类）', '嵌入式系统原理与实验（A类）'),
        ('信号与系统（B类)', '信号与系统（B类）'),
        ('电子技术实验', '电子技术实验'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_5_dianqi(forms.Form):
    class_choices = (
        ('自动控制原理B', '自动控制原理B'),
        ('电力电子技术基础', '电力电子技术基础'),
        ('电机学', '电机学'),
        ('电气工程基础（1）', '电气工程基础（1）'),
        ('数字信号处理（B类）', '数字信号处理（B类）'),
        ('数据库（C类）', '数据库（C类）'),
        ('软件工程（C类）', '软件工程（C类）'),
        ('计算机通讯与网络', '计算机通讯与网络'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_5_cekong(forms.Form):
    class_choices = (
        ('电磁场', '电磁场'),
        ('自动控制原理B', '自动控制原理B'),
        ('测试与控制电路', '测试与控制电路'),
        ('传感器原理', '传感器原理'),
        ('精密仪器设计（1）', '精密仪器设计（1）'),
        ('工程力学', '工程力学'),
        ('现代图学', '现代图学'),
        ('可靠性设计', '可靠性设计'),
        ('工业测控技术与系统', '工业测控技术与系统'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_5_zidonghua(forms.Form):
    class_choices = (
        ('模式识别导论', '模式识别导论'),
        ('数字图像处理基础', '数字图像处理基础'),
        ('数字信号处理（A类）', '数字信号处理（A类）'),
        ('自动化仪表', '自动化仪表'),
        ('电力电子技术', '电力电子技术'),
        ('自动控制原理A', '自动控制原理A'),
        ('机器人学', '机器人学'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_6_dianqi(forms.Form):
    class_choices = (
        ('电气工程基础（2）', '电气工程基础（2）'),
        ('电力系统继电保护', '电力系统继电保护'),
        ('电力系统自动化', '电力系统自动化'),
        ('电力系统暂态分析', '电力系统暂态分析'),
        ('电机控制技术', '电机控制技术'),
        ('电气与电子测量技术', '电气与电子测量技术'),
        ('DSP实践', 'DSP实践'),
        ('可编程控制器原理及应用', '可编程控制器原理及应用'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_6_cekong(forms.Form):
    class_choices = (
        ('检测技术A', '检测技术A'),
        ('精密仪器设计（2）', '精密仪器设计（2）'),
        ('仪器总线与虚拟仪器', '仪器总线与虚拟仪器'),
        ('误差理论与数据处理', '误差理论与数据处理'),
        ('单片机与嵌入式仪器', '单片机与嵌入式仪器'),
        ('数字信号处理', '数字信号处理'),
        ('生物医学信息检测', '生物医学信息检测'),
        ('机器人技术基础', '机器人技术基础'),
        ('电子测量技术与仪器', '电子测量技术与仪器'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_6_zidonghua(forms.Form):
    class_choices = (
        ('检测技术B', '检测技术B'),
        ('数据结构B', '数据结构B'),
        ('非线性系统', '非线性系统'),
        ('现代控制理论（B类）', '现代控制理论（B类）'),
        ('过程控制系统', '过程控制系统'),
        ('运动控制系统', '运动控制系统'),
        ('计算机控制技术', '计算机控制技术'),
        ('IT项目管理', 'IT项目管理'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_7_dianqi(forms.Form):
    class_choices = (
        ('电磁场数值计算', '电磁场数值计算'),
        ('微机控制技术', '微机控制技术'),
        ('现代电气技术讲座', '现代电气技术讲座'),
        ('介质工程与光纤技术', '介质工程与光纤技术'),
        ('电机设计', '电机设计'),
        ('电力系统潮流计算机分析', '电力系统潮流计算机分析'),
        ('电力系统优化运行与市场化', '电力系统优化运行与市场化'),
        ('电气设备的绝缘检测与故障诊断', '电气设备的绝缘检测与故障诊断'),
        ('电磁兼容技术', '电磁兼容技术'),
        ('电网数字化保护控制技术及应用', '电网数字化保护控制技术及应用'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_7_cekong(forms.Form):
    class_choices = (
        ('通信原理（B类）', '通信原理（B类）'),
        ('数据结构B', '数据结构B'),
        ('现代控制理论（A类）', '现代控制理论（A类）'),
        ('图像检测技术基础（中英文）', '图像检测技术基础（中英文）'),
        ('全球导航卫星系统（双语）', '全球导航卫星系统（双语）'),
        ('无损检测', '无损检测'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

class BookForm_7_zidonghua(forms.Form):
    class_choices = (
        ('操作系统（A类）', '操作系统（A类）'),
        ('金融建模及其R软件实例分析', '金融建模及其R软件实例分析'),
        ('系统设计中的人为因素', '系统设计中的人为因素'),
        ('控制系统仿真', '控制系统仿真'),
        ('单片机系统设计', '单片机系统设计'),
        ('数字程序控制系统', '数字程序控制系统'),
        ('数字系统设计技术', '数字系统设计技术'),
        ('传感器网络', '传感器网络'),
        ('线性规划与非线性规划', '线性规划与非线性规划'),
        ('JAVA语言', 'JAVA语言'),
        ('数据库原理与应用', '数据库原理与应用'),
        ('计算机网络（A类）', '计算机网络（A类）'),
        ('系统辨识基础', '系统辨识基础'),
        ('先进控制技术讲座', '先进控制技术讲座'),
    )
    name_book = forms.ChoiceField(choices=class_choices)
    discount_choices =(
        ('1', '一折'),
        ('2', '二折'),
        ('3', '三折'),
    )
    discount_book = forms.ChoiceField(choices=discount_choices)
    photo_book = forms.FileField()

def upload_book(request,book_grade,book_major):
    book_grade_dict={'1':'大一上','2':'大一下','3':'大二上','4':'大二下','5':'大三上','6':'大三下','7':'大四上'}
    book_major_dict={'dianyuan':'电院','xinan':'信安','ruanyuan':'软院','dianqi':'电气','cekong':'测控','zidonghua':'自动化'}
    book_form_dict ={'1dianyuan':BookForm_1_dianyuan,'3dianqi':BookForm_3_dianqi,'3cekong':BookForm_3_cekong,'3zidonghua':BookForm_3_zidonghua,
                     '4dianqi':BookForm_4_dianqi,'4cekong':BookForm_4_cekong,'4zidonghua':BookForm_4_zidonghua,
                     '5dianqi': BookForm_5_dianqi, '5cekong': BookForm_5_cekong, '5zidonghua': BookForm_5_zidonghua,
                     '6dianqi': BookForm_6_dianqi, '6cekong': BookForm_6_cekong, '6zidonghua': BookForm_6_zidonghua,
                     '7dianqi': BookForm_7_dianqi, '7cekong': BookForm_6_cekong, '7zidonghua': BookForm_7_zidonghua
                    }
    book_form_dict_key = book_grade+book_major
    BookForm = book_form_dict[book_form_dict_key]
    if request.user.is_authenticated:
        if request.method == 'POST':
            book_form = BookForm(request.POST, request.FILES)
            if book_form.is_valid():
                name = book_form.cleaned_data['name_book']
                grade =book_grade_dict[book_grade]
                discount = book_form.cleaned_data['discount_book']
                major = book_major_dict[book_major]
                photo =book_form.cleaned_data['photo_book']
                # acquire courrent user
                user = request.user
                book = user.book_set.create(name_book=name, grade_book=grade, discount_book=discount, major_book=major,
                                            photo_book=photo)
                book.save()
                return HttpResponseRedirect('/user_book_detail')
            else:
                book_form = BookForm()
                return HttpResponseRedirect('/upload_book')
        else:
            book_form = BookForm()
            return render(request, "app/upload_book.html", {'book_form': book_form,'title':'发布旧书','year':datetime.now().year,'grade':book_grade_dict[book_grade],'major':book_major_dict[book_major]})
    else:
        return HttpResponseRedirect('/login')

def upload_book_choice(request):
    if request.user.is_authenticated:
        return render(request,"app/upload_book_choice.html")
    else:
        return HttpResponseRedirect('/login')

def user_book_detail(request):
    if request.user.is_authenticated:
        user = request.user
        upoladed_book = user.book_set.all()
        context = {'uploaded_book_list':upoladed_book,
                   'title': '我的书籍',
                   'year': datetime.now().year,
                   }
        return render(request, 'app/user_book_detail.html', context)
    else:
        return HttpResponseRedirect('/login')

#通过传递参数book_id 来达到删除书的目的
def delete_book(request,book_id):
    book_id = book_id
    if request.user.is_authenticated:
        user = request.user
        book = user.book_set.filter(id=book_id)
        book.delete()
    else:
        return HttpResponseRedirect('/login')
    return HttpResponseRedirect('/user_book_detail')


