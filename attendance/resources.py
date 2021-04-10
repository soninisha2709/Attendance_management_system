from import_export import resources
from .models import Attendance_Master , Student_Data , FacultyData

class AttendanceResources(resources.ModelResource):
    class Meta:
        model = Attendance_Master

class studentResources(resources.ModelResource):
    class Meta:
        model = Student_Data

class FacultyResources(resources.ModelResource):
    class Meta:
        model = FacultyData