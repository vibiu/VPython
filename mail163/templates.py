# send_email_xml = \
#     '<?xml version="1.0"?><object><string name="id">c:1462487475453</string>' \
#     '<object name="attrs"><string name="account">"{fromuser}"&lt;{fromuser}@163.com&gt;</string>' \
#     '<boolean name="showOneRcpt">false</boolean>' \
#     '<array name="to"><string>"{touser}@163.com"&lt;{touser}@163.com&gt;</string></array>' \
#     '<array name="cc"/><array name="bcc"/><string name="subject">{subject}</string>' \
#     '<boolean name="isHtml">true</boolean>' \
#     '<string name="content">' \
#     '&lt;div style="line-height:1.7;color:#000000;font-size:14px;font-family:Arial"&gt;'\
#     '{content}&lt;/div&gt;</string>'\
#     '<int name="priority">3</int>'\
#     '<boolean name="saveSentCopy">true</boolean>'\
#     '<string name="charset">GBK</string>'\
#     '</object><boolean name="returnInfo">false</boolean>'\
#     '<string name="action">deliver</string>'\
#     '<int name="saveTextThreshold">1048576</int></object>'

send_email_xml = """<?xml version="1.0"?>
<object>
    <string name="id">c:1462487475453</string>
    <object name="attrs">
        <string name="account">"{fromuser}"&lt;{fromuser}@163.com&gt;</string>
        <boolean name="showOneRcpt">false</boolean>
        <array name="to">
            <string>"{touser}@163.com"&lt;{touser}@163.com&gt;</string>
        </array>
        <array name="cc"/>
        <array name="bcc"/>
        <string name="subject">{subject}</string>
        <boolean name="isHtml">true</boolean>
        <string name="content">
            &lt;div style="line-height:1.7;color:#000000;font-size:14px;font-family:Arial"&gt;
                {content}
            &lt;/div&gt;
        </string>
        <int name="priority">3</int>
        <boolean name="saveSentCopy">true</boolean>
        <string name="charset">GBK</string>
    </object>
    <boolean name="returnInfo">false</boolean>
    <string name="action">deliver</string>
    <int name="saveTextThreshold">1048576</int>
</object>"""

get_info_xml = \
    '<?xml version="1.0"?><object><int name="fid">1</int>'                      \
    '<string name="order">date</string><boolean name="desc">true</boolean>'     \
    '<int name="limit">20</int><int name="start">0</int>'                       \
    '<boolean name="skipLockedFolders">fals</boolean>'                          \
    '<string name="topFlag">top</string><boolean name="returnTag">true</boolean>'\
    '<boolean name="returnTotal">true</boolean></object>'

if __name__ == '__main__':
    print send_email_xml
