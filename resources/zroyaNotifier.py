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
        global fine_template, ok_template

        if action_id == 0:
            zroya.show(ok_template)
        else:
            zroya.show(fine_template)

    # Show question
    zroya.show(ask_template, on_action=onAction)

    # Keep application running, unless onAction handler is never executed.
    time.sleep(10)
    