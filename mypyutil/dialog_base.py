from enum import Enum

class Speaker(Enum):
    OP = 0
    CU = 1 # customer first
    BOT = 2

class DialogBase:

    def __init__(self, dialog_id):
        self.dialog_id = dialog_id
        self.utt_list = []
        self.turn = -1

    def __iter__(self):
        return self.utt_list.__iter__()

    def __repr__(self):
        out = [f"dialog_id {self.dialog_id}, turn {self.turn}"]
        for utt in self.utt_list:
            out.append(utt.__repr__())
        return "<" + "\n".join(out) + ">"

    def __len__(self):
        return len(self.utt_list)

    def append(self, utt):
        self.utt_list.append(utt)

    def set_turn(self):
        self.turn = self.count_turn()

    def count_turn(self):
        turn = 0
        bef_speaker = ""
        for utt in self.utt_list:
            if bef_speaker == Speaker.CU and utt.speaker == Speaker.OP:
                turn += 1
            # for next
            bef_speaker = utt.speaker
        return turn

    # assert: only once switch BOT to OP #TODO fix
    def narrow_down_to_manned_part(self):
        # get i_first_op, i_re_bot
        i_first_op = -1
        i_re_bot = -1
        for i, utt in enumerate(self.utt_list):
            if i_first_op == -1:
                if utt.speaker == Speaker.OP:
                    i_first_op = i
            else:
                if utt.speaker == Speaker.BOT:
                    i_re_bot = i
                    break
        # adjust range
        i_start = i_first_op
        while i_start > 0:
            i_start -= 1
            if self.utt_list[i_start].speaker == Speaker.BOT:
                i_start += 1
                break
        if i_re_bot == -1:
            i_re_bot = len(self.utt_list)
        self.utt_list = self.utt_list[i_start:i_re_bot]
        self.set_turn()



class UtteranceBase:

    def __init__(self, speaker, text):
        assert type(speaker) == Speaker, f"speaker {type(speaker)} is {speaker}"
        self.speaker = speaker
        self.text = text.strip()

    def __repr__(self):
        out = f"{self.speaker}: {self.text}"
        return out

    def get_text(self):
        return self.text

