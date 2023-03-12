import easygui

nz_word = easygui.eneterbox("Please enter the NZ word", "Word to check")
letters = list(nz_word)
letters.remove("u")
easygui.msgbox(f"The American spelling of{nz_word } is {''.join(letters)}",
               "Result")
if play_again  == "no":
    break
list
