from django.shortcuts import render
from .models import Report
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ReportSerializer

from django.core.mail import EmailMultiAlternatives, send_mail, get_connection ,EmailMessage
from django.template.loader import render_to_string
from django.core.mail.message import EmailMessage

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from dohamaldjango.permissions import IsInGroup_ahmashim, IsInGroup_tehnaim

from check.models import Check
from check.serializers import CheckSerializer
from django.http import JsonResponse
# Create your views here.
class ReportRetrieve(generics.RetrieveAPIView):
    permission_classes= [IsAuthenticatedOrReadOnly] ##change to isingrouptehnaimorreadonly

    queryset = Report.objects.all()
    serializer_class = ReportSerializer
class ReportList(generics.ListAPIView):
    permission_classes= [IsAuthenticatedOrReadOnly] ##change to isingrouptehnaimorreadonly

    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportCreate(generics.CreateAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_tehnaim]

    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportUpdate(generics.UpdateAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_tehnaim]

    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDelete(generics.DestroyAPIView):
    permission_classes= [IsAuthenticated, IsInGroup_tehnaim]

    queryset = Report.objects.all()
    serializer_class = ReportSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated, IsInGroup_tehnaim])

def SendEmail(request,*args,**kwargs):
    #subject =  request.POST.get('subject)
    # subject = 'hello'
    # # from_email = 's8704173@army.idf.il' #change to VC
    # from_email = 'h0383vcmng@army.idf.il'
    # # to_email = 'h0383vcmng@army.idf.il'
    # to_email = 's8704173@army.idf.il'
    # text_content = 'This is an important message.'
    # html_content = '<p> this is an <strong> important </strong> message. </p>'

    subject =  request.POST.get('subject')
    from_email =  request.POST.get('from_email')
    to_email =  request.POST.get('to_email')
    text_content =  request.POST.get('text_content')
    html_content =  request.POST.get('html_content')
    print(subject,from_email,to_email,text_content,html_content)
    # msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
    # msg.attach_alternative(html_content,"text/html")
    # msg.send()
    
    send_mail(
        subject = subject,
        message = text_content,
        from_email = from_email,
        recipient_list = [to_email],
        html_message=html_content,
        fail_silently = False,
    )

    # msg = EmailMessage('RC','here is the message',to=['s8704173@army.idf.il'])
    # msg.send()

    # my_host = 'hm.mail.idf'
    # my_port = 587
    # my_username = ''
    # my_password = ''
    # my_use_tls = True
    # connection = get_connection(
    # host = my_host,
    # port = my_port,
    # username= my_username,
    # password = my_password,
    # use_tls = my_use_tls,
    # )
    # send_mail('diditwork?','test message', from_email, [to_email],connection = connection)
    # data=[]
    return JsonResponse({'message': 'mail sent'})
    # return Response()



# @api_view(['GET'])
# @permission_classes([IsAuthenticatedOrReadOnly])
# def ReportkGetRecentByCheckName(request,*args,**kwargs):
#     ### get the reports by check name- all check names must be the same
#     checks = Check.objects.filter(title=kwargs['pk'])
#     data=checks
#     # checkData={
#     #         'Title': check[0].title,
#     #         'location':check[0].location,
#     #         'checkId': check[0].id,
#     #         'mahlaka': check[0].mahlaka,
#     #     }
#     # data.append(checkData)
#     serializer = CheckSerializer
#     # data = serializer.serialize(checks)
#     # return Response(data)
#     return JsonResponse(list(data),safe = False)
# def recentReport(reports):
#     # recent_report = {}
#     # for report in reports[::-1]:
#     #     recent_report = report
#     return recent_report
@permission_classes([IsAuthenticatedOrReadOnly])
class ReportkGetRecentByCheckName(generics.ListAPIView):
    serializer_class = ReportSerializer
    model = Report
    def get_queryset(self):
        data = []
        check_name = self.kwargs['pk']
        checks = Check.objects.filter(title = check_name)
        for check in checks:
            reports = Report.objects.filter(checkId = check).order_by('submitDate')[::-1]
            if reports:
                data.append(reports[0])
        queryset = data
        return queryset