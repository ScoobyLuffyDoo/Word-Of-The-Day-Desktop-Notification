from turtle import onclick
import zroya
import time


@log_action(test=)
class UseZroyaPopup:
    def __init__(self,context) -> dict:
        context = self.context 
        new: bytes =''
    zroya.init("Word Of The Day", "a", "b", "c","d")
    
    # Template for question
    ask_template = zroya.Template(zroya.TemplateType.ImageAndText4)
    ask_template.setFirstLine("Word Of The Day")
    ask_template.setSecondLine(self.context['word'] )
    # ask_template.setImage("./files/image.png")
    ask_template.addAction("Descriptions")
    ask_template.addAction("Usage")

    # Response for Fine
    fine_template = zroya.Template(zroya.TemplateType.Text1)
    fine_template.setFirstLine("Descriptions!")
    fine_template.setSecondLine(self.context['description'] )

    # Response for OK
    ok_template = zroya.Template(zroya.TemplateType.Text1)
    ok_template.setFirstLine("Usage")
    ok_template.setSecondLine(slef.context['usage'] )

    # prepare handler
    def onAction(nid, action_id):
    def __init__(self,context):
        self.context = context 

    def ZoraToast(self):
        global fine_template, ok_template
        zroya.init("Word Of The Day", "a", "b", "c","d")
        
        ask_template = zroya.Template(zroya.TemplateType.ImageAndText4)
        ask_template.setFirstLine("Word Of The Day")
        ask_template.setSecondLine(self.context ['word'] )
        ask_template.setImage("./content/logo.png")
        ask_template.addAction("Descriptions")
        ask_template.addAction("Usage")

        descriptions_template = zroya.Template(zroya.TemplateType.Text2)
        descriptions_template.setFirstLine("description")
        descriptions_template.setSecondLine(self.context['description'] )
        
        usage_template = zroya.Template(zroya.TemplateType.Text2)
        usage_template.setFirstLine("Usage!")
        usage_template.setSecondLine(self.context['usage'] )

        # prepare handler
        def onAction(nid, action_id):    
            if action_id == 0:
                zroya.show(descriptions_template, on_click = openWordOfTheDay)
            else:
                zroya.show(usage_template, on_click = openWordOfTheDay)

        def openWordOfTheDay(notification_id):
            print('was clicked')
        # Show question
        zroya.show(ask_template, on_action=onAction)

        # Keep application running, unless onAction handler is never executed.
        time.sleep(10)
    