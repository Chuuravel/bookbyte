from django import forms

# 로그인폼
class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, 
                               label="아이디",
                                widget=forms.TextInput(
                                    attrs = {"placeholder":"사용자명(3자리 이상)"}
                                ))
    
    password = forms.CharField(min_length=4, 
                               label="비밀번호",
                                widget=forms.PasswordInput(
                                    attrs = {"placeholder":"비밀번호(4자리 이상)"}
                                ))

#회원가입폼
class SignupForm(forms.Form):
    username = forms.CharField(min_length=3, label="아이디")
    password1 = forms.CharField(widget=forms.PasswordInput, min_length=4, label="비밀번호")
    password2 = forms.CharField(widget=forms.PasswordInput, min_length=4, label="비밀번호 확인")
    
    genre_choices = [
        ('인문학','인문학'),
        ('에세이','에세이'),
        ('사회과학','사회과학'),
        ('소설/시/희곡','소설/시/희곡'),
        ('만화','만화'),
        ('자기계발','자기계발'),
        ('경제경영','경제경영'),
        ('수험서/자격증','수험서/자격증'),
        ('역사','역사'),
        ('어린이','어린이'),
        ('예술/대중문화','예술/대중문화'),
        ('외국어','외국어'),
        ('과학','과학'),
        ('좋은부모','좋은부모'),
        ('유아','유아'),
        ('고전','고전'),
        ('청소년','청소년'),
        ('건강/취미','건강/취미'),
        ('컴퓨터/모바일','컴퓨터/모바일'),
        ('종교/역학','종교/역학'),
        ('요리/살림','요리/살림'),
        ('여행','여행'),
        ('대학교재/전문서적','대학교재/전문서적'),
    ]

    genre = forms.ChoiceField(
        label="선호하는 장르(중복선택가능)",
        choices=genre_choices,
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )