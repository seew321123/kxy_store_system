from django import forms
from .models import Project
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','client','client_human','client_pn','project_inf']
        labels = {'name':'项目名称','client':'客户名称','client_human':'客户对接人','client_pn':'客户联系方式','project_inf':'项目详情信息'}