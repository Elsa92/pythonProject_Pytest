import allure

def test_attach_text():
    allure.attach('这是一个纯文本', attachment_type=allure.attachment_type.TEXT)

def test_attachment_html():
    allure.attach('<body>这是一段htmlbody块</body>','html测试快', attachment_type=allure.attachment_type.HTML)

def test_attachment_photo():
    allure.attach.file('C:\\用户\\Elsa\\图片\\捕获.PNG', name='这是一个图片',attachment_type=allure.attachment_type.PNG)

# def test_attachment_video():
#     allure.attach.file('D:\\面试技巧.wmv', name='这是一个视频',attachment_type=allure.attachment_type.WMV)