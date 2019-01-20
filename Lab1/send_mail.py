from gmail import GMail, Message
gmail = GMail("minhphuongtruong1804@gmail.com","TRUONGBUA1804")
from random import choice

sickness_list = ["thương hàn", "kiết lị", "tiêu chảy"]
template = '''
<p>Ch&agrave;o sếp,</p>
<p>H&ocirc;m nay em ngủ dậy, thấy đau bụng, b&aacute;c sĩ bảo em bị Ebola.</p>
<p>Sếp cho em nghỉ l&agrave;m nh&eacute;&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-cry.gif" alt="cry" /></p>
<p>Nh&acirc;n vi&ecirc;n của sếp&nbsp;<img src="https://html5-editor.net/tinymce/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></p>
'''
sickness = choice(sickness_list)
symptom = "đau bụng"

content = template.replace("{{sick}}", sickness).replace("{{symptom}}", symptom)

message = Message("Xin nghỉ làm",to="minhphuongtruong1804@gmail.com",html=content)
gmail.send(message)