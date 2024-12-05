from dotenv import load_dotenv
from openai import OpenAI
#! 创建用户
load_dotenv() #!获取.venv中的信息
name = input("请输入你喜欢的作品（电影、游戏）等等：")
character = input("请输入"+name+"中的一个角色：")
systemprompt = "我希望你能像"+ name +"中的 "+ character +" 一样行动。我希望你以"+ character +"的语调、方式和词汇回答和回复。不要写任何解释。只回答像"+ character +"一样。你必须了解"+ character +"的全部知识。"
ask = "你好"+character+"，请问1+1等于多少？"
client = OpenAI(
    api_key = "sk-UmAVI68tJ5kZlqIInoRXm8ACnS1TNWNPilCFmoBX4Czg1h0v",
    base_url="https://api.moonshot.cn/v1"
)

completion = client.chat.completions.create(
    model = "moonshot-v1-8k",
    messages = [
        {"role":"system", "content":systemprompt},
        {"role":"user", "content":ask}
    ],
    temperature = 0.3
)
print(completion.choices[0].message.content)
