import zroya
import time

# Initialization is required. But in real usage, check the return code, please.
zroya.init("python12", "blha", "blajsk", "askjdk", "asfdcs")

# Template for question
ask_template = zroya.Template(zroya.TemplateType.ImageAndText4)
ask_template.setFirstLine("Hi, I am NotifyBot.")
ask_template.setSecondLine("It is nice to meet you.")
ask_template.setThirdLine("How are you?")
# ask_template.setImage("./files/image.png")
ask_template.addAction("I'm OK, I guess")
ask_template.addAction("Fine")

# Response for Fine
fine_template = zroya.Template(zroya.TemplateType.Text1)
fine_template.setFirstLine("Glad to hear that!")

# Response for OK
ok_template = zroya.Template(zroya.TemplateType.Text1)
ok_template.setFirstLine("I'm sorry to hear that!")


# prepare handler
def onAction(nid, action_id):
    global fine_template, ok_template

    if action_id == 0:
        zroya.show(ok_template)
    else:
        zroya.show(fine_template)

# Show question
zroya.show(ask_template, on_action=onAction)

# Keep application running, unless onAction handler is never executed.
time.sleep(10)