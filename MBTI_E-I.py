import tkinter
import tkinter.font as TkFont

RESULT = [
    "당신은 최고의 인싸입니다.", #외향100
    "당신은 주변의 사람들이 끊이지 않습니다.",
    "당신은 활발한 성격을 가지고 있습니다.",
    "당신은 대인관계가 원만한 사람입니다.",
    "당신은 차분한 성격을 지니고 있습니다.",
    "당신은 소수와의 관계를 오랫동안 유지할수 있습니다. ",
    "당신은 매우 신중한 사람입니다",         #내향100
]

def click_btn():
    pts = 0
    for i in range(6):
        if bvar[i].get() == True:
            pts = pts+1
    IE = int(100 * pts /6) #퍼센트 구하기
    EI = 100-IE
    text.delete("1.0", tkinter.END)
    text.insert("1.0", "<진단결과>\n당신의 내성적인 성격은" + str(IE) + "%입니다." + 
                "\n당신의 외향적인 성격은" + str(EI) + "%입니다.\n" + RESULT[pts])

root = tkinter.Tk()
root.title("자신의 성격 알아보기")
root.resizable(False,False)
canvas = tkinter.Canvas(root, width=1000, height=560) #캔버스 크기
canvas.pack()
test = tkinter.PhotoImage(file = "MBTI.png") #
canvas.create_image(500,280,image=test) #이미지크기


Extravert = tkinter.PhotoImage(file="EXTRAVERT.png") #width=140,height=200
canvas.create_image(115,350,image=Extravert)

Introvert = tkinter.PhotoImage(file="INTROVERT.png") #width=140, height=150
canvas.create_image(885,330, image=Introvert)

BFont = TkFont.Font(family="Arial", weight="bold", size = 32)
button = tkinter.Button(text="진단하기", relief="solid",font=BFont, command=click_btn, bg='#A9BCF5',fg="#0B0B61")
button.place(x=400, y=450) #버튼

text = tkinter.Text(width = 50, height = 4, font=("Times New Roman", 18), bg="white")
text.place(x=220, y=25) #텍스창

bvar = [None] * 6
cbtn = [None] * 6
ITEM = [ #I를 중심으로한 질문들
    "친구들과 노는것보다 혼자가 좋다",
    "활발한 사람들 사이에서 기빨린다",
    "집순이 혹은 집돌이다",
    "친구들과의 약속이 깨지면 오히려 좋다",
    "직원에게 원하는것이 있어도 잘 말하지 못한다",
    "새로운 사람과 친해지는데 많은 시간이 필요하다",
]

for i in range(6):
    bvar[i] = tkinter.BooleanVar()
    bvar[i].set(False)
    cbtn[i] = tkinter.Checkbutton(text=ITEM[i],
font=("Modern", 12), variable=bvar[i], bg="#A9BCF5")
    cbtn[i].place(x=360, y=170 + 45 * i)
    
root.mainloop()