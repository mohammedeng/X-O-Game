# تعريف الخطوط الثمانية الممكنة للفوز مرة واحدة فقط (خارج الدالة أو داخلها)
WINNING_COMPOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # الصفوف (Rows)
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # الأعمدة (Columns)
    (0, 4, 8), (2, 4, 6)               # الأقطار (Diagonals)
]

# تعريف الألوان (ANSI Codes)
RED = "\033[91m"    # لون للأحمر (X)
BLUE = "\033[94m"   # لون للأزرق (O)
RESET = "\033[0m"   # إعادة اللون الافتراضي للتيرمينال
ANGELS =(0,2,6,8)


class Board:
    def __init__(self):

        self.board_list=[i for i in range(1,10)]
        self.position_list=[]

    def get_colored_symbol(self,val):
        """تلوين الرمز بناءً على قيمته دون تغيير النص الأصلي"""
        if val.upper() == 'X':
            return f"{RED}X{RESET}"
        elif val.upper() == 'O':
            return f"{BLUE}O{RESET}"
        return val
    def display_board(self):
        # إنشاء قائمة جديدة تحتوي على الخانات الملونة للعرض فقط
        colored_b = [self.get_colored_symbol(str(item)) for item in self.board_list]

        print("\n")
        print(f"        {colored_b[0]} | {colored_b[1]} | {colored_b[2]} ")
        print("       ---+---+---")
        print(f"        {colored_b[3]} | {colored_b[4]} | {colored_b[5]} ")
        print("       ---+---+---")
        print(f"        {colored_b[6]} | {colored_b[7]} | {colored_b[8]} ")
        print("\n")


    def check_win(self):
        """ترجع True إذا كانت هناك 3 رموز متطابقة في أي خط فوز"""
        return any(self.board_list[a] == self.board_list[b_idx] == self.board_list[c] for a, b_idx, c in WINNING_COMPOS)