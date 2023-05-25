from django.shortcuts import render
import csv

# Create your views here.
def taskdetails(request):
    if request.method == 'POST':
        taskname = request.POST.get('taskname')
        taskid = request.POST.get('taskid')
        taskstatus = request.POST.get('taskstatus')
        with open('taskdetails.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([taskname, taskid, taskstatus])
    return render(request, 'taskdetails.html',)