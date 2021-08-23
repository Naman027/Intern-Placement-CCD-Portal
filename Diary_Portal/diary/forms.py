from django import forms

class save_changes(forms.Form):
    POC = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':1, 'cols': 55}))
    CPOC = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':1, 'cols': 55}))
    Remark = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':55}))

class add_company(forms.Form):
    CompanyName = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':1, 'cols': 55}))
    POC = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':1, 'cols': 55}))
    CPOC = forms.CharField(max_length=100, widget=forms.Textarea(attrs={'rows':1, 'cols': 55}))
    Remark = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':55}))

class authentication(forms.Form):
    Username = forms.CharField(max_length=100)
    Password = forms.CharField(max_length=100,widget=forms.PasswordInput)

class change_username_password(forms.Form):
    Current_Username = forms.CharField(max_length=100)
    Current_Password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    New_Username = forms.CharField(max_length=100)
    New_Password = forms.CharField(max_length=100,widget=forms.PasswordInput)
    Confirm_Password = forms.CharField(max_length=100,widget=forms.PasswordInput)

