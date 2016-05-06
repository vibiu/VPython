import requests
import re
from templates import get_info_xml, send_email_xml


class LoginUser():
    domain = 163
    login_url = "https://mail.163.com/entry/cgi/ntesdoor?" \
        "funcid=loginone&iframe=1&passtype=1&product=mail163&uid=None"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        """let the user login, must be called before any mail operate"""

        data = {
            "savelogin": 0,
            "password": self.password,
            "username": self.username,
            "url2": "http://mail.163.com/errorpage/error163.htm"
        }
        self.login_info = requests.post(self.login_url, data=data)
        self.cookies = self.login_info.cookies
        try:
            self.sid = self.cookies.get('Coremail').split('%')[1]
        except AttributeError as e:
            return None
        return self

    def get_url(self, url):
        """send request in get method using requests
        :param url: str, url
        """

        response = requests.get(url, cookies=self.cookies)
        return response

    def post_url_data(self, url, data, headers=None):
        """send request in post method using requests
        :param url: str, url
        :param data: dict, query data
        :param headers: dict, request headers
        """

        if headers:
            response = requests.post(
                url, data=data, cookies=self.cookies, headers=headers)
        else:
            response = requests.post(url, data=data, cookies=self.cookies)
        return response

    def get_redirect_url(self):
        """get the redirect url of 163 site"""

        urlpattern = re.compile("top.location.href = \"(.+?)\";</script>")
        redirect_url = urlpattern.findall(self.login_info.content)[0]

        res = self.get_url(redirect_url)
        return res

    def get_mails_info(self):
        """get the mails infomation"""

        post_data = get_info_xml
        email_url = "http://mail.163.com/js6/s?"\
            "sid={0}&func=mbox:listMessages".format(self.sid)
        headers = {"Accept": "text/javascript"}

        res = self.post_url_data(email_url, post_data, headers)
        return res

    def sent_mail(self, touser, subject="test subject", content='testword'):
        """send single mail
        :param touser: str, the user to send
        :param subject: str, email subject
        :param content: str, email content
        """

        email_url = 'http://mail.163.com/js6/s?sid={0}&func=mbox:compose&cl_compose=1'\
            '&cl_send=1&l=compose&action=deliver'.format(self.sid)

        post_data = {
            "fromuser": self.username,
            "touser": touser,
            "subject": subject,
            "content": content
        }
        post_xml = send_email_xml.format(**post_data)
        post_param = {"var": post_xml}

        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        res = self.post_url_data(email_url, post_param, headers)
        return res

    def get_logout_url(self):
        """ get the logout url list"""

        urlpattern = re.compile(
            "<link rel=\"stylesheet\" href=\"(.+?)\" type=\"text/css\" />")
        logout_url = \
            'http://uswebmail.mail.163.com/js6/logout.jsp?sid={0}' \
            '&uid={1}@163.com&username={2}'.format(
                self.sid, self.username, self.username)
        res = self.get_url(logout_url)
        url_list = urlpattern.findall(res.content)
        return url_list

    def logout(self):
        """logout use the logout url list"""

        url_list = self.get_logout_url()
        for url in url_list:
            res = self.get_url(url)
        return True


def checkout_mail(username, password):
    """offer a UI show that you have got the mail infomation"""

    user = LoginUser(username, password)
    loginuser = user.login()
    if loginuser:
        print "{} login ok!".format(username)
        print loginuser.get_mails_info().content
        loginuser.logout()
        print 'logout ok!'
    else:
        print '{0}\'s password {1} invalid'.format(username, password)


def read_email_count():
    """read email username and password from the mailinfo.txt
    :return type: genratorm, (username,password)
    """

    mailpattern = re.compile('(.+?)@(163|126)\.com\s+?pswd:(.+?)\n')
    with open('mailinfo.txt', "r") as mail_txt:
        mail_str = mail_txt.read()
        mail_list = mailpattern.findall(mail_str)
    return ((mail[0], mail[2]) for mail in mail_list)


def scan_mail():
    """scan to check if my email was recovered"""

    for mail in read_email_count():
        checkout_mail(mail[0], mail[1])


def send_email(username, password, touser, subject, content):
    """send a mail
    :param username: str, username
    :param password: str, password
    :param touser: str, the user to send
    :param subject: str, email subject
    :param content: str, email content
    """

    user = LoginUser(username, password)
    loginuser = user.login()
    print 'sending email'
    loginuser.sent_mail(
        touser, subject=subject, content=content)
    print 'send ok'
    try:
        loginuser.logout()
        print 'logout'
    except:
        print 'logout failed'


if __name__ == '__main__':
    scan_mail()
    pass
