from django import forms
import attendance.models as m 
from django import forms
import attendance.models as m 


class studentForm(forms.ModelForm):
      class Meta:
          model = m.Student_Data
          fields = '__all__'

class facultyForm(forms.ModelForm):
      class Meta:
          model = m.FacultyData
          fields = '__all__'

class subjectForm(forms.ModelForm):
    class Meta:
        model = m.Subject_Table
        fields = "__all__"

class complainForm(forms.ModelForm):
    class Meta:
        model = m.complain_table
        fields = '__all__'

class attendaceForm(forms.ModelForm):
    class Meta:
        model = m.Attendance_Master
        fields = "__all__"