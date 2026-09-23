import customtkinter as ctk
from board import Board
from player import Player
from computerplayer import ComputerPlayer
# 1. ضبط مظهر الواجهة (Dark Mode)
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

# 2. إنشاء النافذة الرئيسية
window =ctk.CTk()
window.title("Tic Tac Toe")
window.geometry("360x520")
window.resizable(width=False, height=False)

# 3. تهيئة كائنات اللعبة من ملفاتك
board = Board()
human = Player(name="Player 1", symbol="x")
computer = ComputerPlayer(symbol="o")

# 3. إضافة العنوان العلوي لحالة اللعبة
status_label = ctk.CTkLabel(
    master=window,
    text=f"{human.name}'s Turn (X)",
    font=("Arial", 22, "bold")
)
# الدالة pack تضع العنصر داخل النافذة، و pady تترك مسافة فارغة من الأعلى والأسفل
status_label.pack(pady=20)


# 1. دالة التحقق من نهاية اللعبة (فوز أو تعادل)
def check_game_over(player):
    if board.check_win():
        status_label.configure(text=f"🏆 {player.name} Wins!")
        # إيقاف جميع الأزرار المتبقية عند نهاية اللعبة
        for btn in buttons:
            btn.configure(command=None)
        return True
    elif len(board.position_list) == 9:
        status_label.configure(text="🤝 It's a Draw!")
        return True
    return False


# 2. دالة تنفذ دور الكمبيوتر
def computer_turn():
    #count the length of th list to now if there is new move added
    prev_count = len(board.position_list)

    # استدعاء الذكاء الاصطناعي لتعديل اللوحة
    computer.make_move(board)

    # لمعرفة الخانة التي اختارها الكمبيوتر وتحديث زِرّها في الواجهة
    if len(board.position_list) > prev_count:
        chosen_index = board.position_list[-1]
        buttons[chosen_index].configure(
            text=computer.symbol.upper(),
            text_color="#000000",  # أزرق جذاب للرمز O
            command=None
        )

    # التحقق من فوز الكمبيوتر أو التعادل
    if not check_game_over(computer):
        status_label.configure(text=f"{human.name}'s Turn (X)")


# 3. تحديث دالة ضغط الزر للاعب البشري
def on_button_click(index):
    if index in board.position_list:
        return

    # تنفيذ حركة اللاعب البشري
    board.position_list.append(index)
    board.board_list[index] = human.symbol
    buttons[index].configure(
        text=human.symbol.upper(),
        text_color="#FF4444",
        command=None
    )

    # التحقق هل فاز البشري؟ إذا لم يفز، يلعب الكمبيوتر
    if not check_game_over(human):
        status_label.configure(text=f"{computer.name}'s Turn (O)")
        window.after(400, computer_turn)  # تأخير 0.4 ثانية قبل رد الكمبيوتر


# 8. دالة إعادة تشغيل اللعبة
def reset_game():
    global board
    board = Board()  # إعادة إنشاء لوحة فارغة جديدة
    status_label.configure(text=f"{human.name}'s Turn (X)")

    for i, btn in enumerate(buttons):
        btn.configure(
            text=f"{i + 1}",
            text_color="#FFFFFF",
            command=lambda idx=i: on_button_click(idx)
        )
grid_frame = ctk.CTkFrame(master=window)
grid_frame.pack(pady=20, padx=20)

buttons = []
for i in range(9):
    row, col = divmod(i, 3)  # تحسب الصف والعمود تلقائياً من 0 إلى 8
    btn = ctk.CTkButton(
        master=grid_frame,
        text=f"{i + 1}",
        width=80,
        height=80,
        font=("Arial", 44),
        command=lambda index=i: on_button_click(index),
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    buttons.append(btn)
# 10. زر إعادة التشغيل في أسفل النافذة
restart_btn = ctk.CTkButton(
    master=window,
    text="Restart Game 🔄",
    font=("Arial", 16, "bold"),
    fg_color="#2B2B2B",
    hover_color="#3A3A3A",
    command=reset_game
)
restart_btn.pack(pady=20)
# 3. تشغيل النافذة
window.mainloop()