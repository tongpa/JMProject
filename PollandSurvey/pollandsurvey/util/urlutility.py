import logging;

log = logging.getLogger(__name__); 
class URLUtility(object):
    URL_REPLY = "http://{0}/ans/reply/{1}.{2}.{3}.0.html"
    URL_REPLY_QUESTIONNAIRE = "/ans/questionnaire/{key}"
    URL_QUESTIONNAIRE = "http://{nameserver}" + URL_REPLY_QUESTIONNAIRE #/ans/questionnaire/{1}" 
    
    URL_GETDATAQUESTION = '/ans/getDataPreview/{key}'
    URL_WELCOME = '/ans/welcome/{key}'
    URL_EXPIRED = '/expired'
    URL_THANKYOU = '/thankyou'
    URL_HOME = '/'
    URL_GOODBYE = '/ans/thankyou/{key}';
